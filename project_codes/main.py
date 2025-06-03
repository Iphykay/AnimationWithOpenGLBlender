module_name = 'Final_Project'

'''
Version: 1.1.0

Description:
    A helicopter

Authors:
    Iphy Kelvin

Date Created     : 4/27/2025
Date Last Updated: 4/27/2025

Doc:


Notes:
    <***>
'''


# CUSTOM IMPORTS
from helicopterRenderer import bigRotor, smallRotor, helicopter

# OTHER IMPORTS
import pygame      as pyg
from pygame.locals import *
from OpenGL.GL     import *
from OpenGL.GLU    import *
from OpenGL.GLUT   import *

# USER INTERFACE
screenWidth  = 1200
screenHeight = 800
display      = (screenWidth, screenHeight)

# CONSTANTS
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
ORANGE  = (255, 165, 0)
YELLOW  = (255, 255, 0)
BLUE    = (0, 0, 255)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY    = (64, 64, 64)
PURPLE  = (128, 0, 128)


class Helicopter:
    def __init__(self):
        pass
    #

    def setColor(self, color):
        r = float(color[0])/255.0
        g = float(color[1])/255.0
        b = float(color[2])/255.0
        return glColor3f(r, g, b)
    #

    def draw_helicopter(self):
        glPushMatrix()
        self.setColor(YELLOW)
        glEnable(GL_DEPTH_TEST)
        glTranslatef(0.0, 12.0, 0.0)
        glRotatef(-180.0, 1.0, 0.0, 0.0)
        glScalef(2.5, 2.5, 1.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        helicopter()

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        self.setColor(GRAY)

        helicopter()
        glDisable(GL_POLYGON_OFFSET_FILL)
        glPopMatrix()
    #

    def draw_bigrotor(self, angle):
        glPushMatrix()
        self.setColor(WHITE)
        glEnable(GL_DEPTH_TEST)
        glTranslatef(0.0, 11.8, 2.0)
        glRotatef(-180.0, 1.0, 0.0, 0.0)
        glRotatef(angle, 0.0, 0.0, 1.0)
        glScalef(2.9, 2.9, 1.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        bigRotor()

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        self.setColor(GRAY)
        bigRotor()
        
        glDisable(GL_POLYGON_OFFSET_FILL)
        glPopMatrix()
    #

    def draw_smallrotor(self, angle):
        glPushMatrix()
        self.setColor(WHITE)
        glEnable(GL_DEPTH_TEST)
        glTranslatef(1.0, 28.7, 3.0)
        glRotatef(90.0, 0.0, 1.0, 0.0)
        glRotatef(angle, 0.0, 0.0, 1.0)  # rotate the rotor along the z-axis
        glScalef(1.0, 1.0, 1.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        smallRotor()

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        self.setColor(GRAY)
        smallRotor()
        
        glDisable(GL_POLYGON_OFFSET_FILL)
        glPopMatrix()
    #


def main():
    pyg.init()
    pyg.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Create the window caption
    pyg.display.set_caption('Movie Scene')

    # To manage how ffast the screen updates
    clock = pyg.time.Clock()

    glMatrixMode(GL_PROJECTION) 
    gluPerspective(90, (display[0]/display[1]), 0.1, 60)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    # Camera Position
    myX = 30; myY= 0; myZ = 0
    myHeading = 90.0
    myPitch   = 0.0
    gluLookAt(myX, myY, myZ, 0, 0, 0, 0, 0, 1)

    helcpta = Helicopter()

    angle = 0.0

    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
            # if
        # for

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(myX, myY, myZ, 0, 0, 0, 0, 0, 1)

        helcpta.draw_helicopter()
        helcpta.draw_bigrotor(angle)
        helcpta.draw_smallrotor(angle)
        pyg.display.flip()
        clock.tick(60)

        angle += -150.0
    # while
    pyg.quit()


if __name__ == '__main__':
    main()