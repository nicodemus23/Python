import pygame
import pyrr
import math
import numpy as np
from pygame.math import Vector3
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the number of subdivisions for the sphere
subdivisions = 32

# Create empty lists to store vertex data
sphere_vertices = []
sphere_normals = []
sphere_texcoords = []

# Generate vertices, normals, and texture coordinates for the sphere
for y in range(subdivisions + 1):
    for x in range(subdivisions + 1):
        phi = math.pi * y / subdivisions
        theta = 2 * math.pi * x / subdivisions

        # Calculate vertex position
        x_pos = math.sin(phi) * math.cos(theta)
        y_pos = math.cos(phi)
        z_pos = math.sin(phi) * math.sin(theta)

        # Calculate normal (same as vertex position for a sphere)
        nx = x_pos
        ny = y_pos
        nz = z_pos

        # Calculate texture coordinates using spherical mapping
        u = 0.5 + math.atan2(z_pos, x_pos) / (2 * math.pi)
        v = 0.5 - math.asin(y_pos) / math.pi

        # Append vertex data to the lists
        sphere_vertices.append((x_pos, y_pos, z_pos))
        sphere_normals.append((nx, ny, nz))
        sphere_texcoords.append((u, v))
# Convert lists to numpy arrays for better performance
sphere_vertices = np.array(sphere_vertices, dtype=np.float32)
sphere_normals = np.array(sphere_normals, dtype=np.float32)
sphere_texcoords = np.array(sphere_texcoords, dtype=np.float32)

##############################################################################################

#vertex shader
vertex_shader_code = '''
#version 330 core 

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aNormal;
layout(location = 2) in vec2 aTexCoord;

out vec3 FragPos;
out vec3 Normal;
out vec2 TexCoord;

uniform mat4 model; 
uniform mat4 view;
uniform mat4 projection;

void main()
{
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    TexCoord = aTexCoord;
    
    gl_Position = projection * view * vec4(FragPos, 1.0);
}
'''

# fragment shader
fragment_shader_code = '''
#version 330 core

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoord;

out vec4 FragColor;

uniform sampler2D diffuseMap;
uniform sampler2D roughnessMap;
uniform sampler2D emissiveMap;
uniform sampler2D glossinessMap;
uniform sampler2D metallicMap;
uniform sampler2D normalMap;
uniform sampler2D opacityMap;
uniform sampler2D occlusionMap;

uniform vec3 lightPos;
uniform vec3 lightColor;
uniform vec3 viewPos;

void main()
{
    vec3 diffuse = texture2D(diffuseMap, TexCoord).rgb;
    float roughness = texture2D(roughnessMap, TexCoord).r;
    vec3 emissive = texture2D(emissiveMap, TexCoord).rgb * 3.0;
    float glossiness = texture2D(glossinessMap, TexCoord).r;
    float metallic = texture2D(metallicMap, TexCoord).r;
    vec3 normal = texture2D(normalMap, TexCoord).rgb * 5.0 - 1.0;
    float opacity = texture2D(opacityMap, TexCoord).r;
    float occlusion = texture2D(occlusionMap, TexCoord).r;
    
    vec3 N = normalize(Normal);
    vec3 L = normalize(lightPos - FragPos);
    vec3 V = normalize(viewPos - FragPos);
    vec3 H = normalize(L + V);
    
    float NdotL = max(dot(N, L), 0.0);
    float NdotV = max(dot(N, V), 0.0);
    float NdotH = max(dot(N, H), 0.0);
    
    vec3 ambient = diffuse * occlusion;
    vec3 diffuseColor = diffuse * NdotL; 
    diffuseColor *= lightColor;
    
    float specularIntensity = pow(NdotH, glossiness * 100.0);
    vec3 specularColor = vec3(0.04) * specularIntensity * lightColor;
    
    vec3 color = ambient + diffuseColor + specularColor + emissive;
    
    FragColor = vec4(color, opacity);
}
'''
#vec3 color = (ambient + diffuseColor + specularColor) * lightColor;

##############################################################################################

pygame.init()

width = 800
height = 600

# Set the position of the circle
circle_x = width // 2
circle_y = height // 2  

# Create a window with the specified width and height and make it resizable and double buffered 
window = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE) 
pygame.display.set_caption("Lame Game")

# enable depth testing and blending
glEnable(GL_DEPTH_TEST) # Enable depth testing for 3D rendering 
glEnable(GL_BLEND) # Enable blending
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # Set the blending function   


# Set up projection matrix
glMatrixMode(GL_PROJECTION) # Set the matrix mode to projection which is used to define the properties of the camera that views the objects in the world coordinate frame
#glLoadIdentity() # Load the identity matrix to reset the projection matrix
#glOrtho(0, width, height, 0, -1, 1) # Set the orthographic projection matrix
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW) # Set the matrix mode to modelview which is used to place objects in the world coordinate frame
#glLoadIdentity() # Load the identity matrix to reset the modelview matrix


glViewport(0, 0, width, height) # Set the viewport to the entire window

# load and compile shader program
vertex_shader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader, vertex_shader_code)
glCompileShader(vertex_shader)

fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader, fragment_shader_code)
glCompileShader(fragment_shader)

shader_program = glCreateProgram()
glAttachShader(shader_program, vertex_shader)
glAttachShader(shader_program, fragment_shader)
glLinkProgram(shader_program)

# checks to see if the shader program compiled and linked 
success = glGetProgramiv(shader_program, GL_LINK_STATUS)
if not success:
    info_log = glGetProgramInfoLog(shader_program)
    print(f"Shader program linking failed: {info_log.decode()}")
else:
    print("Shader program linked successfully")

# check for compilation and linking errors
success = glGetShaderiv(vertex_shader, GL_COMPILE_STATUS)
if not success:
    info_log = glGetShaderInfoLog(vertex_shader)
    print(f"Vertex shader compilation failed: {info_log.decode()}")
    
success = glGetShaderiv(fragment_shader, GL_COMPILE_STATUS)
if not success:
    info_log = glGetShaderInfoLog(fragment_shader)
    print(f"Fragment shader compilation failed: {info_log.decode()}")
    
success = glGetProgramiv(shader_program, GL_LINK_STATUS)
if not success:
    info_log = glGetProgramInfoLog(shader_program)
    print(f"Shader program linking failed: {info_log.decode()}")
    
# Create a Vertex Buffer Object (VBO) and Vertex Array Object (VAO) for the sphere
sphere_vbo = glGenBuffers(1)
sphere_vao = glGenVertexArrays(1)

glBindVertexArray(sphere_vao)
glBindBuffer(GL_ARRAY_BUFFER, sphere_vbo)
glBufferData(GL_ARRAY_BUFFER, len(sphere_vertices) * 4 * (3 + 3 + 2), None, GL_STATIC_DRAW)
glBufferSubData(GL_ARRAY_BUFFER, 0, len(sphere_vertices) * 4 * 3, np.array(sphere_vertices, dtype=np.float32).flatten())
glBufferSubData(GL_ARRAY_BUFFER, len(sphere_vertices) * 4 * 3, len(sphere_normals) * 4 * 3, np.array(sphere_normals, dtype=np.float32).flatten())
glBufferSubData(GL_ARRAY_BUFFER, len(sphere_vertices) * 4 * (3 + 3), len(sphere_texcoords) * 4 * 2, np.array(sphere_texcoords, dtype=np.float32).flatten())

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(len(sphere_vertices) * 4 * 3))

glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(len(sphere_vertices) * 4 * (3 + 3)))

glBindVertexArray(0)

# DIFFUSE MAP
diffuse_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_diffuse.jpg")
diffuse_texture_data = pygame.image.tostring(diffuse_texture_image, "RGBA", 1)
diffuse_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE0) # Activate texture unit 0
glBindTexture(GL_TEXTURE_2D, diffuse_texture_id) # Bind the texture to the texture target
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) # Set the texture minification filter
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # Set the texture magnification filter
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, diffuse_texture_image.get_width(), diffuse_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, diffuse_texture_data) # Load the texture data
glGenerateMipmap(GL_TEXTURE_2D) # Generate mipmaps for the texture

# ROUGHNESS MAP
roughness_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_roughness.jpg")
roughness_texture_data = pygame.image.tostring(roughness_texture_image, "RGBA", 1)
roughness_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE1) # Activate texture unit 1
glBindTexture(GL_TEXTURE_2D, roughness_texture_id) # Bind the texture to the texture target
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) # Set the texture minification filter
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # Set the texture magnification filter
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, roughness_texture_image.get_width(), roughness_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, roughness_texture_data) # Load the texture data
glGenerateMipmap(GL_TEXTURE_2D) # Generate mipmaps for the texture

# EMISSIVE MAP
emissive_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_emissive.jpg")
emissive_texture_data = pygame.image.tostring(emissive_texture_image, "RGBA", 1)
emissive_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE2)  # Activate texture unit 2
glBindTexture(GL_TEXTURE_2D, emissive_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, emissive_texture_image.get_width(), emissive_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, emissive_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Load and bind glossiness texture map
glossiness_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_glossiness.jpg")
glossiness_texture_data = pygame.image.tostring(glossiness_texture_image, "RGBA", 1)
glossiness_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE3)  # Activate texture unit 3
glBindTexture(GL_TEXTURE_2D, glossiness_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, glossiness_texture_image.get_width(), glossiness_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, glossiness_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Load and bind metallic texture map
metallic_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_metallic.jpg")
metallic_texture_data = pygame.image.tostring(metallic_texture_image, "RGBA", 1)
metallic_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE4)  # Activate texture unit 4
glBindTexture(GL_TEXTURE_2D, metallic_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, metallic_texture_image.get_width(), metallic_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, metallic_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Load and bind normal texture map
normal_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_normal.jpg")
normal_texture_data = pygame.image.tostring(normal_texture_image, "RGBA", 1)
normal_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE5)  # Activate texture unit 5
glBindTexture(GL_TEXTURE_2D, normal_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, normal_texture_image.get_width(), normal_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, normal_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Load and bind opacity texture map
opacity_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_opacity.jpg")
opacity_texture_data = pygame.image.tostring(opacity_texture_image, "RGBA", 1)
opacity_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE6)  # Activate texture unit 6
glBindTexture(GL_TEXTURE_2D, opacity_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, opacity_texture_image.get_width(), opacity_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, opacity_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Load and bind occlusion texture map
occlusion_texture_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_ao.jpg")
occlusion_texture_data = pygame.image.tostring(occlusion_texture_image, "RGBA", 1)
occlusion_texture_id = glGenTextures(1)
glActiveTexture(GL_TEXTURE7)  # Activate texture unit 7
glBindTexture(GL_TEXTURE_2D, occlusion_texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, occlusion_texture_image.get_width(), occlusion_texture_image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, occlusion_texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

# Get location of shader uniforms
diffuse_map_loc = glGetUniformLocation(shader_program, "diffuseMap") # Get the location of the diffuse map uniform in the shader program 
roughness_map_loc = glGetUniformLocation(shader_program, "roughnessMap")
emissive_map_loc = glGetUniformLocation(shader_program, "emissiveMap")
glossiness_map_loc = glGetUniformLocation(shader_program, "glossinessMap")
metallic_map_loc = glGetUniformLocation(shader_program, "metallicMap")
normal_map_loc = glGetUniformLocation(shader_program, "normalMap")
opacity_map_loc = glGetUniformLocation(shader_program, "opacityMap")
occlusion_map_loc = glGetUniformLocation(shader_program, "occlusionMap")

object_position = Vector3(0, 0, 0) # Set the position of the object
object_rotation = Vector3(0, 0, 0) # Set the rotation of the object 
object_scale = Vector3(1, 1, 1) # Set the scale of the object

#only need if not using shader based lighting
#Light source
# glEnable(GL_LIGHTING) 
# glEnable(GL_LIGHT0) # Enable light source 0
# glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1, 0)) # Set the position of light source 0
# glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1)) # Set the ambient color of light source 0
# glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1)) # Set the diffuse color of light source 0
# glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1)) # Set the specular color of light source 0

# #Materials
# glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1)) # Set the ambient color of the material
# glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8, 1)) # Set the diffuse color of the material
# glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1)) # Set the specular color of the material
# glMaterialf(GL_FRONT, GL_SHININESS, 50) # Set the shininess of the material

# Load and set up the background
background_image = pygame.image.load(r"C:\Users\Nic\Documents\Neumont\6_Spring 2024\CSC181\Python\Textures\cgaxis_yellow_stained_glass_43_22_8K\yellow_stained_glass_43_22_diffuse.jpg")
background_data = pygame.image.tostring(background_image, "RGBA", True)
background_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, background_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, background_image.get_width(), background_image.get_height(),0, GL_RGBA, GL_UNSIGNED_BYTE, background_data)
glGenerateMipmap(GL_TEXTURE_2D)

######################################## TEST CODE ########################################
def render_cube():
    vertices = [
    -0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 0.0,
        0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 0.0,
        0.5,  0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 1.0,
        0.5,  0.5, -0.5, 0.0, 0.0, -1.0, 1.0, 1.0,
    -0.5,  0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 1.0,
    -0.5, -0.5, -0.5, 0.0, 0.0, -1.0, 0.0, 0.0,

    -0.5, -0.5,  0.5, 0.0, 0.0, 1.0, 0.0, 0.0,
        0.5, -0.5,  0.5, 0.0, 0.0, 1.0, 1.0, 0.0,
        0.5,  0.5,  0.5, 0.0, 0.0, 1.0, 1.0, 1.0,
        0.5,  0.5,  0.5, 0.0, 0.0, 1.0, 1.0, 1.0,
    -0.5,  0.5,  0.5, 0.0, 0.0, 1.0, 0.0, 1.0,
    -0.5, -0.5,  0.5, 0.0, 0.0, 1.0, 0.0, 0.0,

    -0.5,  0.5,  0.5, -1.0, 0.0, 0.0, 1.0, 0.0,
    -0.5,  0.5, -0.5, -1.0, 0.0, 0.0, 1.0, 1.0,
    -0.5, -0.5, -0.5, -1.0, 0.0, 0.0, 0.0, 1.0,
    -0.5, -0.5, -0.5, -1.0, 0.0, 0.0, 0.0, 1.0,
    -0.5, -0.5,  0.5, -1.0, 0.0, 0.0, 0.0, 0.0,
    -0.5,  0.5,  0.5, -1.0, 0.0, 0.0, 1.0, 0.0,

        0.5,  0.5,  0.5, 1.0, 0.0, 0.0, 1.0, 0.0,
        0.5,  0.5, -0.5, 1.0, 0.0, 0.0, 1.0, 1.0,
        0.5, -0.5, -0.5, 1.0, 0.0, 0.0, 0.0, 1.0,
        0.5, -0.5, -0.5, 1.0, 0.0, 0.0, 0.0, 1.0,
        0.5, -0.5,  0.5, 1.0, 0.0, 0.0, 0.0, 0.0,
        0.5,  0.5,  0.5, 1.0, 0.0, 0.0, 1.0, 0.0,

    -0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 0.0, 1.0,
        0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 1.0, 1.0,
        0.5, -0.5,  0.5, 0.0, -1.0, 0.0, 1.0, 0.0,
        0.5, -0.5,  0.5, 0.0, -1.0, 0.0, 1.0, 0.0,
    -0.5, -0.5,  0.5, 0.0, -1.0, 0.0, 0.0, 0.0,
    -0.5, -0.5, -0.5, 0.0, -1.0, 0.0, 0.0, 1.0,

    -0.5,  0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0,
        0.5,  0.5, -0.5, 0.0, 1.0, 0.0, 1.0, 1.0,
        0.5,  0.5,  0.5, 0.0, 1.0, 0.0, 1.0, 0.0,
        0.5,  0.5,  0.5, 0.0, 1.0, 0.0, 1.0, 0.0,
    -0.5,  0.5,  0.5, 0.0, 1.0, 0.0, 0.0, 0.0,
    -0.5,  0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0
    ]

    vertices = np.array(vertices, dtype=np.float32)

    cube_vao = glGenVertexArrays(1)
    glBindVertexArray(cube_vao)

    cube_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cube_vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, None)

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    glBindVertexArray(0)

    glBindVertexArray(cube_vao)
    glDrawArrays(GL_TRIANGLES, 0, 36)
    glBindVertexArray(0)

    glDeleteVertexArrays(1, [cube_vao])
    glDeleteBuffers(1, [cube_vbo])
    
########################################### END TEST CODE ########################################



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
        
    # Light Rotation
    light_rotation_x = 0.0
    light_rotation_y = 0.0
    light_rotation_z = 0.0

    # Update light rotation based on user input (i, j, k, l, n, m keys)
    if keys[pygame.K_i]:
        light_rotation_x += 1
    if keys[pygame.K_k]:
        light_rotation_x -= 1
    if keys[pygame.K_j]:
        light_rotation_y += 1
    if keys[pygame.K_l]:
        light_rotation_y -= 1
    if keys[pygame.K_n]:
        light_rotation_z += 1
    if keys[pygame.K_m]:
        light_rotation_z -= 1
    
    euler_angles = pyrr.euler.create(
        math.radians(light_rotation_x),
        math.radians(light_rotation_y),
        math.radians(light_rotation_z)
    )

    light_rotation_matrix = pyrr.matrix44.create_from_eulers(euler_angles)

    light_position = pyrr.Vector3([1.0, 1.0, 1.0])
    light_position = pyrr.matrix44.apply_to_vector(light_rotation_matrix, light_position)
    
    # Convert the pyrr.Vector3 object to a tuple
    light_position_tuple = tuple(light_position)
    
    # Set the light position uniform
    glUseProgram(shader_program)
    glUniform3f(glGetUniformLocation(shader_program, "lightPos"), *light_position_tuple)
    
    light_intensity = 1.0

    # Update light intensity based on user input (+ or - keys)
    if keys[pygame.K_PLUS]:
        light_intensity += 0.1
    if keys[pygame.K_MINUS]:
        light_intensity -= 0.1
        if light_intensity < 0.1:
            light_intensity = 0.1
    
# Render the scene

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the color and depth buffers
    glUseProgram(shader_program) # Use the shader program

    # Set the shader uniforms for the texture maps
    glUniform1i(diffuse_map_loc, 0) # Set the diffuse map uniform to 0
    glUniform1i(roughness_map_loc, 1)
    glUniform1i(emissive_map_loc, 2)
    glUniform1i(glossiness_map_loc, 3)
    glUniform1i(metallic_map_loc, 4)
    glUniform1i(normal_map_loc, 5)
    glUniform1i(opacity_map_loc, 6)
    glUniform1i(occlusion_map_loc, 7) # Set the occlusion map uniform to 7
        
    #Render background
    # glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    # glBindTexture(GL_TEXTURE_2D, background_id)
    # glBegin(GL_QUADS)
    # glTexCoord2f(0, 0)
    # glVertex3f(-1, -1, -5)
    # glTexCoord2f(1, 0)
    # glVertex3f(1, -1, -5)
    # glTexCoord2f(1, 1)
    # glVertex3f(1, 1, -5)
    # glTexCoord2f(0, 1)
    # glVertex3f(-1, 1, -5)
    # glEnd()
    
    glClear(GL_DEPTH_BUFFER_BIT) # Clear the depth buffer to render the transparent object correctly

    
    # Set up the model, view, and projection matrices
    model_matrix = glGetFloatv(GL_MODELVIEW_MATRIX).flatten()
    translation_matrix = pyrr.matrix44.create_from_translation(pyrr.Vector3(object_position))
    rotation_matrix_x = pyrr.matrix44.create_from_x_rotation(math.radians(object_rotation.x))
    rotation_matrix_y = pyrr.matrix44.create_from_y_rotation(math.radians(object_rotation.y))
    rotation_matrix_z = pyrr.matrix44.create_from_z_rotation(math.radians(object_rotation.z))
    scale_matrix = pyrr.matrix44.create_from_scale(pyrr.Vector3(object_scale))
    model_matrix = pyrr.matrix44.multiply(translation_matrix, rotation_matrix_x)
    model_matrix = pyrr.matrix44.multiply(model_matrix, rotation_matrix_y)
    model_matrix = pyrr.matrix44.multiply(model_matrix, rotation_matrix_z)
    model_matrix = pyrr.matrix44.multiply(model_matrix, scale_matrix)
    
    # view_matrix = pyrr.matrix44.create_look_at(
    # eye=pyrr.Vector3([0.0, 0.0, 3.0]),
    # target=pyrr.Vector3([0.0, 0.0, 0.0]),
    # up=pyrr.Vector3([0.0, 1.0, 0.0])
    # )
    
    # Set up the view matrix
    eye_position = pyrr.Vector3([0.0, 0.0, 3.0])
    target_position = pyrr.Vector3(object_position)
    up_vector = pyrr.Vector3([0.0, 1.0, 0.0])

    view_matrix = pyrr.matrix44.create_look_at(
    eye=eye_position,
    target=target_position,
    up=up_vector
    )

    projection_matrix = pyrr.matrix44.create_perspective_projection(
        fovy=45.0, aspect=(width / height), near=0.1, far=50.0
    )

    # Send matrices to the shader
    model_loc = glGetUniformLocation(shader_program, "model")
    view_loc = glGetUniformLocation(shader_program, "view")
    proj_loc = glGetUniformLocation(shader_program, "projection")

    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_matrix)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view_matrix)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection_matrix)
    
    # DON'T USE: #########
    # model_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    # view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    # projection_matrix = glGetFloatv(GL_PROJECTION_MATRIX)
    # glUniformMatrix4fv(glGetUniformLocation(shader_program, "model"), 1, GL_FALSE, model_matrix)
    # glUniformMatrix4fv(glGetUniformLocation(shader_program, "view"), 1, GL_FALSE, view_matrix)
    # glUniformMatrix4fv(glGetUniformLocation(shader_program, "projection"), 1, GL_FALSE, projection_matrix)
    ###########
    
    # Set the light position, color, and view position uniforms
    glUniform3f(glGetUniformLocation(shader_program, "lightPos"), 1.0, 1.0, 1.0)
    #glUniform3f(glGetUniformLocation(shader_program, "lightColor"), 1.0, 1.0, 1.0)
    # Set the light color uniform dynamically
    glUniform3f(glGetUniformLocation(shader_program, "lightColor"), light_intensity, light_intensity, light_intensity)
    glUniform3f(glGetUniformLocation(shader_program, "viewPos"), 0.0, 0.0, 0.0)
    
    # Render object
    glTranslatef(*object_position) # Translate the object to the specified position
    glRotatef(object_rotation.x, 1, 0, 0) # Rotate the object around the x-axis
    glRotatef(object_rotation.y, 0, 1, 0) # Rotate the object around the y-axis
    glRotatef(object_rotation.z, 0, 0, 1) # Rotate the object around the z-axis
    glScalef(*object_scale) # Scale the object
    
    # Render transparent, refractive sphere
    # glEnable(GL_TEXTURE_2D) # Enable texturing
    # glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    # glBindTexture(GL_TEXTURE_2D, texture_id) # Bind the texture to the texture target
    # glPushMatrix() # Push the current matrix onto the matrix stack
    
    # Render cube
    render_cube()
    
    # Render sphere
    # glBindVertexArray(sphere_vao)
    # glDrawArrays(GL_TRIANGLES, 0, len(sphere_vertices))
    # glBindVertexArray(0)
    
    print("Sphere Vertices:")
    print(sphere_vertices)
    print("\nSphere Normals:")
    print(sphere_normals)
    print("\nSphere Texture Coordinates:")
    print(sphere_texcoords)

    # Check if vertices were drawn
    restart_index = glGetIntegerv(GL_PRIMITIVE_RESTART_INDEX)
    print(f"Restart index: {restart_index}")

    # Check for OpenGL errors
    error = glGetError()
    if error != GL_NO_ERROR:
        print(f"OpenGL error occurred: {error}")
    
    pygame.display.flip() # Update the window to show the circle at the updated position and the background color
            
pygame.quit() # Quit Pygame

############################################################################################3

#OLD CODE
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