import pygame
import time
import random



crashed = False
width, height = 800,600
black, white, red = [(0, 0, 0), (255, 255, 255), (255, 0, 0)]

carImg = pygame.image.load('PyGame/Images/car.png')
car_width = 80

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Nigga')
clock = pygame.time.Clock()

def dogeCount(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Doged: "+str(score), True, black)
    gameDisplay.blit(text, (0, 0))

def things(tx, ty, tw, th, color):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    pygame.draw.rect(gameDisplay, (r, g, b), [tx, ty, tw, th])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def textobjects(str, font):
    surface = font.render(str, True, black)
    return surface, surface.get_rect()

def messageDisplay(str):
    text = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = textobjects(str, text)
    TextRect.center = (width/2, height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def crash():
    messageDisplay('You Crashed')


def gameLoop():
    x = width*0.45
    y = height*0.8
    score = 0
    x_speed = 0
    y_speed = 0
    thingX = random.randrange(0, width)
    thingY = -600
    thing_speed = 4
    thingW, thingH = [100, 100]
    gameExit = False

    pygame.init()
    while not gameExit :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed=-5
                elif event.key == pygame.K_RIGHT:
                    x_speed=5
                if event.key == pygame.K_UP:
                    y_speed=-5
                elif event.key == pygame.K_DOWN:
                    y_speed=5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        x+=x_speed
        y+=y_speed

        gameDisplay.fill(white)
        things(thingX, thingY, thingW, thingH, black)
        thingY+=thing_speed


        car(x, y)
        dogeCount(score)

        if x<0 or x+car_width>width:
            crash()

        if thingY > height:
            thingY = -100
            thingX = random.randrange(0, width)
            score+=1
            thing_speed+=1
        if thingY+100>y and thingY<y+80 and thingX<x+car_width and thingX+thingW>x:
            crash()


        pygame.display.update()
        clock.tick(60)
    
gameLoop()
pygame.quit()
quit()
