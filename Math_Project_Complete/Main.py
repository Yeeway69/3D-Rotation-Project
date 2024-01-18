
import pygame
import sys
from Graphics.Cube import Cube
from Controllers.KeyboardController import handle_keyboard_events
from UI.MainUI import update_ui
from Math.Transformations import quaternion_from_euler_angles, rotation_matrix_from_euler_angles, euler_angles_from_quaternion, rotation_vector_from_euler_angles, get_euler_angles, normalize_angle
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Cube Visualization')

# Create a Cube object
cube = Cube()

# Function to get user input for Euler angles (placeholder)
def get_user_input_euler_angles():
    # TODO: Implement actual user input logic
    # Return roll, pitch, yaw as radians
    
    return 0, 0, 0  # Placeholder values



# Main loop

running = True



while running:
     
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:  # Rotate left
            cube.rotate_y(-math.radians(5))  # Rotate by 5 degrees
           elif event.key == pygame.K_RIGHT:  # Rotate right
            cube.rotate_y(math.radians(5))
           elif event.key == pygame.K_UP:  # Rotate up
            cube.rotate_x(-math.radians(5))
           elif event.key == pygame.K_DOWN:  # Rotate down
            cube.rotate_x(math.radians(5))
    
    
    
    # Update cube's orientation based on user input
    # TODO: Replace this with actual input handling logic
    roll, pitch, yaw = cube.get_euler_angles()
    rotation_matrix = rotation_matrix_from_euler_angles(roll, pitch, yaw)
    cube.apply_rotation(rotation_matrix)
    # Convert Euler angles to quaternion
    quaternion = quaternion_from_euler_angles(roll, pitch, yaw)

    screen.fill((0, 0, 0))  # Fill the screen with black (or any other color that contrasts with the cube)
    
    # Define the left and right zones
    left_zone_width = screen.get_width() // 2
    right_zone_width = screen.get_width() - left_zone_width
     # Draw the left zone background
    left_zone_surface = pygame.Surface((left_zone_width, screen.get_height()))
    left_zone_surface.fill((50, 50, 50))  # A different shade for the cube's zone
    screen.blit(left_zone_surface, (0, 0))
    # # Draw the cube
    # cube.draw(screen)
    # Draw the cube in the left zone
    cube.draw(screen.subsurface((0, 0, left_zone_width, screen.get_height())))
    # Update UI in the right zone
    update_ui(screen.subsurface((left_zone_width, 0, right_zone_width, screen.get_height())), cube, roll, pitch, yaw)
    

    # Update cube and UI
    update_ui(screen, cube, roll, pitch, yaw)

    # Update the display
    pygame.display.flip()
    
 # Cap the frame rate
    pygame.time.Clock().tick(60)  # Cap at 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()