import pyglet
from pyglet import clock
from pyglet.gl import *

import numpy as np


x = 0
win = pyglet.window.Window(resizable=True)
evt = pyglet.app.EventLoop()
clock.tick()

@evt.event
def idle():
    on_draw()
    return pyglet.event.EVENT_HANDLED


@evt.event
def on_window_close(window):
    evt.exit()
    return pyglet.event.EVENT_HANDLED


@win.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width/2, width/2, -height/2, height/2, -200, 200)
    glMatrixMode(gl.GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED



def drawCube(x, y, z, size):
    cubeVL = pyglet.graphics.vertex_list(8, 'v3f', 'c3B')
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(x,y,z)
    cubeVL.vertices = [-size, size, size, size, size, size, size,-size, size, -size,-size, size, -size, size,-size, size, size,-size, size,-size,-size, -size,-size,-size]
    cubeVL.colors = np.repeat([255, 0, 0], 8)
    cubeVL.draw(pyglet.gl.GL_LINE_LOOP)
    glPopMatrix()

 
@win.event
def on_draw():
    global x
    x+=1
    win.clear()
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST);
    drawCube(x, 0, 0, 50)


clock.schedule(on_draw)
pyglet.app.run()
evt.run()




