import cv2
import numpy as np
import matplotlib.pyplot as plt
import threading
import colorsys

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __mul__(self, k):
        return Point(self.x*k, self.y*k)
    
    def __eq__(self, other):
            return self.x==other.x and self.y==other.y
        
    def __str__(self):
            return "({0}, {1})".format(self.x, self.y)

rw = 2
p = 0
scale = 1
start = Point()
end = Point()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vout = cv2.VideoWriter('maze2.avi', fourcc, 20.0, (1024, 768))
mX, mY = [0,0]
dir4 = [Point( 0,-1),Point(-1, 0), Point( 0, 0), Point( 1, 0),Point( 0, 1)]
dir8 = [Point(-1,-1), Point( 0,-1), Point( 1,-1),
        Point(-1, 0), Point( 0, 0), Point( 1, 0),
        Point(-1, 1), Point( 0, 1), Point( 1, 1)]

def BFS_Search(s, e):

    print("Starting BFS Search")
    
    global img, h, w
    const = h*w//42
    found = False
    visited_color = [25,200,255]
    path_color = [255, 255, 255]
    
    q = []
    v = [[0 for j in range(w)] for i in range(h)]
    parent  = [[Point() for j in range(w)] for i in range(h)]
    
    q.append(start)
    v[s.y][s.x] = 1

    while len(q)>0:
        p = q.pop(0)
        for d in dir4:
            cell = p+d
            if (cell.y>=0 and cell.y<h and
                cell.x>=0 and cell.x<w and
                v[cell.y][cell.x]==0 and
                (img[cell.y][cell.x][0]!=0 or img[cell.y][cell.x][1]!=0 or img[cell.y][cell.x][2]!=0)):
                q.append(cell)
                v[cell.y][cell.x] =  v[p.y][p.x]+1
                if img[cell.y][cell.x][0] == 255:
                    img[cell.y][cell.x] = list( reversed( [i*255 for i in colorsys.hsv_to_rgb(v[cell.y][cell.x]/const,1,1)] ))
                parent[cell.y][cell.x] = p
                if cell==e:
                    found = True
                    del q[:]
                    break

    path = []
    if found:
        p = e
        while p!=s:
            path.append(p)
            p = parent[p.y][p.x]
        path.append(p)
        path.reverse()

        for p in path[1:len(path)-1]:
            img[p.y][p.x] = path_color
        print("Path found")
    else:
        print("Path not found")

    print("Completed BFS Search")

def mouse_event(event,x,y,flags,param):

    global start, end, scale, img, p, mX, mY

    if event == cv2.EVENT_MOUSEMOVE:
        mX, mY = x, y

    if event == cv2.EVENT_LBUTTONUP:
        scale+=1

    if event == cv2.EVENT_RBUTTONUP and scale>=1:
        scale-=1

    if event == cv2.EVENT_MOUSEWHEEL:
        pX, pY = [ int(mX/scale), int(mY/scale)]
        if p==0:
            cv2.rectangle(img,(pX-rw,pY-rw),(pX+rw,pY+rw),(0, 0, 255),-1)
            start = Point(pX, pY)
            print("Start =", start)
            p+=1
        elif p==1:
            cv2.rectangle(img,(pX-rw,pY-rw),(pX+rw,pY+rw),(0, 225, 50),-1)
            end = Point(pX, pY)
            print("End =", end)
            p+=1

def disp():

    global scale, img, w, h, vout
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_event)
    while 1:
        vout.write(img)
        resi = cv2.resize(img,(scale*w, scale*h), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('image', resi)
        cv2.waitKey(1)


img = cv2.imread('OpenCV/Images/hardest_maze.png', cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(img , cv2.COLOR_GRAY2BGR)
h, w = img.shape[:2]
print("Select start and End points by clicking")

t = threading.Thread(target=disp, args = ())
t.daemon = True
t.start()

while p<2:
    pass

BFS_Search(start, end)
print("Press any key to continue...")
cv2.waitKey(1000)
cv2.destroyAllWindows()


