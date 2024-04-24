import pygame
from pygame.math import Vector3
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

width = 800
height = 600

# Set the position of the circle
circle_x = width // 2
circle_y = height // 2  

# Create a window with the specified width and height and make it resizable and double buffered 
window = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE) 
pygame.display.set_caption("Lame Game")

glEnable(GL_DEPTH_TEST) # Enable depth testing for 3D rendering 
glEnable(GL_BLEND) # Enable blending
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # Set the blending function   

glViewport(0, 0, width, height) # Set the viewport to the entire window
glMatrixMode(GL_PROJECTION) # Set the matrix mode to projection which is used to define the properties of the camera that views the objects in the world coordinate frame
glLoadIdentity() # Load the identity matrix to reset the projection matrix
#glOrtho(0, width, height, 0, -1, 1) # Set the orthographic projection matrix
# set the perspective projection matrix
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW) # Set the matrix mode to modelview which is used to place objects in the world coordinate frame
glLoadIdentity() # Load the identity matrix to reset the modelview matrix

#Lighting
glEnable(GL_LIGHTING) 
glEnable(GL_LIGHT0) # Enable light source 0
glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1, 0)) # Set the position of light source 0
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1)) # Set the ambient color of light source 0
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1)) # Set the diffuse color of light source 0
glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1)) # Set the specular color of light source 0

#Materials
glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1)) # Set the ambient color of the material
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8, 1)) # Set the diffuse color of the material
glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1)) # Set the specular color of the material
glMaterialf(GL_FRONT, GL_SHININESS, 50) # Set the shininess of the material

#Load Texture
texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_diffuse.jpg")
texture_data = pygame.image.tostring(texture_image, "RGBA", 1)
texture_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_id) # Bind the texture to the texture target
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) # Set the texture minification filter
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # Set the texture magnification filter
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture_image.get_width(), texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data) # Load the texture data
glGenerateMipmap(GL_TEXTURE_2D)

# Load and set up the background
background_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_diffuse.jpg")
background_data = pygame.image.tostring(background_image, "RGBA", True)
background_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, background_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, background_image.get_width(), background_image.get_height(),0, GL_RGBA, GL_UNSIGNED_BYTE, background_data)
glGenerateMipmap(GL_TEXTURE_2D)


object_position = Vector3(0, 0, -2) # Set the position of the object
object_rotation = Vector3(0, 0, 0) # Set the rotation of the object 
object_scale = Vector3(1, 1, 1) # Set the scale of the object

# Set the title of the window
running = True # A flag to keep track of whether the game is running
while running: # The main game loop
    for event in pygame.event.get(): # Get all the events that have occurred
        if event.type == pygame.QUIT:   # If the event is a quit event
            running = False        # Set the running flag to False to exit the loop
        # Add this block of code before the rendering code
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            object_rotation.y -= 1
        if keys[pygame.K_RIGHT]:
            object_rotation.y += 1
        if keys[pygame.K_UP]:
            object_rotation.x -= 1
        if keys[pygame.K_DOWN]:
            object_rotation.x += 1
        if keys[pygame.K_q]:
            object_scale *= 1.01
        if keys[pygame.K_e]:
            object_scale /= 1.01
        if keys[pygame.K_w]:
            object_position.y += 0.1
        if keys[pygame.K_s]:
            object_position.y -= 0.1
        if keys[pygame.K_a]:
            object_position.x -= 0.1
        if keys[pygame.K_d]:
            object_position.x += 0.1
        if keys[pygame.K_z]:
            object_position.z += 0.1
        if keys[pygame.K_x]:
            object_position.z -= 0.1
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         object_rotation.y -= 10
        #     elif event.key == pygame.K_RIGHT:
        #         object_rotation.y += 10
        #     elif event.key == pygame.K_UP:
        #         object_rotation.x -= 10
        #     elif event.key == pygame.K_DOWN:
        #         object_rotation.x += 10
        #     elif event.key == pygame.K_q:
        #         object_scale *= 1.1
        #     elif event.key == pygame.K_e:
        #         object_scale /= 1.1
        #     elif event.key == pygame.K_w:
        #         object_position.y += 0.1
        #     elif event.key == pygame.K_s:
        #         object_position.y -= 0.1
        #     elif event.key == pygame.K_a:
        #         object_position.x -= 0.1
        #     elif event.key == pygame.K_d:
        #         object_position.x += 0.1
        #     elif event.key == pygame.K_z:
        #         object_position.z += 0.1
        #     elif event.key == pygame.K_x:
        #         object_position.z -= 0.1
                    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the color and depth buffers
    glLoadIdentity() # Load the identity matrix to reset the modelview matrix
    
    #Render background
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D, background_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -5)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, -5)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, -5)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, -5)
    glEnd()
    
    glTranslatef(*object_position) # Translate the object to the specified position
    glRotatef(object_rotation.x, 1, 0, 0) # Rotate the object around the x-axis
    glRotatef(object_rotation.y, 0, 1, 0) # Rotate the object around the y-axis
    glRotatef(object_rotation.z, 0, 0, 1) # Rotate the object around the z-axis
    glScalef(*object_scale) # Scale the object
    
    # Render transparent, refractive sphere
    glEnable(GL_TEXTURE_2D) # Enable texturing
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D, texture_id) # Bind the texture to the texture target
    glPushMatrix() # Push the current matrix onto the matrix stack
    quadric = gluNewQuadric() # Create a new quadric object
    gluQuadricNormals(quadric, GLU_SMOOTH) # Generate smooth normals for the quadric
    glColor4f(0.8, 0.8, 1.0, 0.5) # Set the color of the sphere with alpha value for transparency
    gluQuadricTexture(quadric, GL_TRUE) # Enable texture coordinates for the quadric
    gluSphere(quadric, 1, 32, 32) # Render a sphere with the quadric
    gluDeleteQuadric(quadric) # Delete the quadric object to free up memory
    glPopMatrix() # Pop the matrix stack to restore the previous matrix
    glDisable(GL_TEXTURE_2D) # Disable texturing
    
    
#clear window
    # window.fill((255, 255, 255)) # Fill the window with white
    # #pygame.display.update() # Update the window to show the white background
    
    # # move the circle
    # # Move the circle based on arrow key presses
    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT]:
    #     circle_x -= 3
    # if key[pygame.K_RIGHT]:
    #     circle_x += 3
    # if key[pygame.K_UP]:
    #     circle_y -= 3
    # if key[pygame.K_DOWN]:
    #     circle_y += 3

    # Draw the circle at the updated position
    #pygame.draw.circle(window, (0, 0, 255), (circle_x, circle_y), 50)
    # update the window to show the circle
    #pygame.display.update()
    
    pygame.display.flip() # Update the window to show the circle at the updated position and the background color
            
pygame.quit() # Quit Pygame