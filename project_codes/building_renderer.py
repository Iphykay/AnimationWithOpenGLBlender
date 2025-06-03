module_name = 'Building_renderer'

'''
Version: 1.1.0

Description:
    Puts parts of a building together and renders it

Authors:
    Iphy Kelvin

Date Created     : 5/13/2025
Date Last Updated: 4/13/2025

Doc:


Notes:
    <***>
'''

# CUSTOM IMPORTS
from building import building_vertices, building_edges, building_faces

# OTHER IMPORTS
from pygame.locals import *
from OpenGL.GL     import *
from OpenGL.GLU    import *
from OpenGL.GLUT   import *

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


def building():
    glBegin(GL_QUADS)
    for face in building_faces:
        for vertex in face:
            glVertex3fv(building_vertices[vertex])
        # for 
    # for
    glEnd()

    glBegin(GL_LINES)
    for edge in building_edges:
        for vertex in edge:
            glVertex3fv(building_vertices[vertex])
        # for
    # for 
    glEnd()
#
