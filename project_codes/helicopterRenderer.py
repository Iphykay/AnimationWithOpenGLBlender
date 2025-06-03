module_name = 'Helicopter_renderer'

'''
Version: 1.1.0

Description:
    Puts parts of a helicopter together and renders it

Authors:
    Iphy Kelvin

Date Created     : 4/27/2025
Date Last Updated: 4/27/2025

Doc:


Notes:
    <***>
'''


# CUSTOM IMPORTS
from smallrotors    import smallrotors_vertices, smallrotors_faces, smallrotors_edges
from bigrotors      import bigrotors_vertices, bigrotors_faces, bigrotors_edges
from mainhelicopter import helicopter_vertices, helicopter_edges, helicopter_faces

# OTHER IMPORTS
from pygame.locals import *
from OpenGL.GL     import *
from OpenGL.GLU    import *
from OpenGL.GLUT   import *

# USER INTERFACE

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


def bigRotor():
    glBegin(GL_QUADS)
    for face in bigrotors_faces:
        for vertex in face:
            glVertex3fv(bigrotors_vertices[vertex])
        # for 
    # for
    glEnd()

    glBegin(GL_LINES)
    for edge in bigrotors_edges:
        for vertex in edge:
            glVertex3fv(bigrotors_vertices[vertex])
        # for
    # for 
    glEnd()
#

def smallRotor():
    glBegin(GL_QUADS)
    for face in smallrotors_faces:
        for vertex in face:
            glVertex3fv(smallrotors_vertices[vertex])
        # for 
    # for
    glEnd()

    glBegin(GL_LINES)
    for edge in smallrotors_edges:
        for vertex in edge:
            glVertex3fv(smallrotors_vertices[vertex])
        # for
    # for 
    glEnd()
#

def helicopter():
    glBegin(GL_QUADS)
    for face in helicopter_faces:
        for vertex in face:
            glVertex3fv(helicopter_vertices[vertex])
        # for 
    # for
    glEnd()

    glBegin(GL_LINES)
    for edge in helicopter_edges:
        for vertex in edge:
            glVertex3fv(helicopter_vertices[vertex])
        # for
    # for 
    glEnd()
#


