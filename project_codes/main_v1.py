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
from building_renderer  import building

# OTHER IMPORTS
from numpy         import radians
from math          import cos, sin
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

    def degtoRadian(self, angle):
        return radians(angle)
    #

    def setColor(self, color):
        r = float(color[0])/255.0
        g = float(color[1])/255.0
        b = float(color[2])/255.0
        return glColor3f(r, g, b)
    #

    def updatePosition(self, x0, y0, z0, heading, pitch, inc):
        headingRad = self.degtoRadian(heading)
        pitchRad = self.degtoRadian(pitch)
        
        # Yaw
        x = x0 + inc * cos(headingRad)
        y = y0 + inc * sin(headingRad)
        z = z0
        
        y = y + inc * sin(pitchRad)
    
        return x, y, z
    #

    def draw_helicopter(self):
        glPushMatrix()
        self.setColor(YELLOW)
        glEnable(GL_DEPTH_TEST)
        glTranslatef(0.0, 12.0, 0.0)   # 0.0, 12.0, 0.0
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

    def move_helicopter(self, Mangle, angle):
        glPushMatrix()
        glRotatef(-Mangle, 0.0, 0.0, 1.0)
        glTranslatef(30.0, 0.0, 30.0)
        self.draw_helicopter()
        self.draw_bigrotor(angle)
        self.draw_smallrotor(angle)
        glPopMatrix()
    #


class buildings(Helicopter):
    def __init__(self):
        super().__init__()
    #

    def draw_building(self, angle, xT, yT, zT): 
        '''
        Outputs the building from blender

        Input:
        -----
        angle: angle to rotate the building
        xT   : translation in the x-direction
        yT   : translation in the y-direction
        zT   : translation in the z-direction
        '''
        glPushMatrix()
        self.setColor(GREEN)
        glRotatef(angle, 0.0, 0.0, 10.0)
        glTranslatef(xT, yT, zT)
        glScalef(1.5, 1.8, 1.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        building()

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        self.setColor(GRAY)
        building()

        glDisable(GL_POLYGON_OFFSET_FILL)
        glPopMatrix()
    #

    def position_building(self, angle, mxT, myT, mzT):

        # First row of building
        glPushMatrix()
        glTranslatef(mxT, myT, mzT)
        self.draw_building(angle, 0.0, 50.0, 0.0)
        self.draw_building(angle, 0.0, 20.0, 0.0)
        self.draw_building(angle, 0.0, -10.0, 0.0)
        glPopMatrix()

    def position_building2(self, angle, mxT, myT, mzT):
        # Second row of building
        glPushMatrix()
        glTranslatef(mxT, myT, mzT)
        self.draw_building(angle, 0.0, -50.0, 0.0)
        self.draw_building(angle, 0.0, -20.0, 0.0)
        self.draw_building(angle, 0.0, 5.0, 0.0)
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
    gluPerspective(90, (display[0]/display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    # Camera Position
    # myX = 30; myY= 0; myZ = 20
    # myHeading = 90.0
    # myPitch   = 0.0
    # gluLookAt(myX, myY, myZ, 0, 0, 0, 0, 0, 1)

    myX = 45; myY= 5; myZ = 65
    myHeading = 90.0
    myPitch   = 0.0
    gluLookAt(myX, myY, myZ, 0, 0, 0, 0, 0, 1)

    helcpta       = Helicopter()
    see_buildings = buildings()

    angle = Mangle = 0.0

    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
            # if
        # for

        """ Check for keyboard presses. """
        key = pyg.key.get_pressed()
        
        # Leave window
        if (key[pyg.K_ESCAPE] == True):
            running = False
            
        # Translations, forward, backwards, left, right.    
        if (key[pyg.K_UP] == True):
            glTranslatef(0,0,0.1)
            myX, myY, myZ = helcpta.updatePosition(myX, myY, myZ, myHeading, myPitch, 0.1)
            
        if (key[pyg.K_DOWN] == True):
            glTranslatef(0,0,-0.1)
            myX, myY, myZ = helcpta.updatePosition(myX, myY, myZ, myHeading, myPitch, -0.1)
        if (key[pyg.K_LEFT] == True):
           glTranslatef(0.1,0,0)
           myX, myY, myZ = helcpta.updatePosition(myX, myY, myZ, myHeading + 90, myPitch, 0.1)
           
        if (key[pyg.K_RIGHT] == True):
           glTranslatef(-0.1,0,0)
           myX, myY, myZ = helcpta.updatePosition(myX, myY, myZ, myHeading - 90, myPitch, 0.1)
        
        # Translations, up, down.
        if (key[pyg.K_PAGEUP] == True):
            glTranslatef(0,-0.1,0)
            myZ = myZ + 0.1
            
        if (key[pyg.K_PAGEDOWN] == True):
            glTranslatef(0,0.1,0)
            myZ = myZ - 0.1
            
            
        # Rotate left, right.
        if (key[pyg.K_KP4] == True):
            glRotatef(-0.3, 0, 1, 0)
            myHeading = myHeading + 0.3
            
        if (key[pyg.K_KP6] == True):
            glRotatef(0.3, 0, 1, 0)
            myHeading = myHeading - 0.3
           
            
        # Pitch nose down, nose up
        if (key[pyg.K_KP8] == True):
            glRotatef(0.3, 1, 0, 0)
            myPitch = myPitch - 0.3
            
        if (key[pyg.K_KP2] == True):
            glRotatef(-0.3, 1, 0, 0)
            myPitch = myPitch + 0.3

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(myX, myY, myZ, 0, 0, 0, 0, 0, 1)

        # # Helicopter
        helcpta.move_helicopter(Mangle, angle)

        # Buildings
        see_buildings.position_building(90.0, 10.0, 15.0, 0.0)
        see_buildings.position_building2(-90.0, 10.0, -15.0, 0.0)
        pyg.display.flip()
        clock.tick(20)

        angle += -150.0
        Mangle += 10.0
    # while
    pyg.quit()


if __name__ == '__main__':
    main()