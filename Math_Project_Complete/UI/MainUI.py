import pygame
import math
import numpy as np
from Math.Transformations import rotation_matrix_from_euler_angles, quaternion_from_euler_angles, euler_angles_from_quaternion, rotation_vector_from_euler_angles
def draw_text(screen, text, position, font_size=20, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def update_ui(screen, cube, roll, pitch, yaw):
    # Calculate the quaternion, rotation vector, and rotation matrix
    quaternion = quaternion_from_euler_angles(roll, pitch, yaw)
    rotation_vector = rotation_vector_from_euler_angles(roll, pitch, yaw)
    rotation_matrix = rotation_matrix_from_euler_angles(roll, pitch, yaw)

    # Convert numpy array to string for display
    quaternion_str = np.array2string(quaternion, precision=2, separator=', ')
    rotation_vector_str = np.array2string(rotation_vector, precision=2, separator=', ')
    rotation_matrix_str = np.array2string(rotation_matrix, precision=2, separator=', ', suppress_small=True)

    # Displaying the calculated attitude representations
    draw_text(screen, f'Quaternion: {quaternion_str}', (420, 20))
    draw_text(screen, f'Euler Principal Angle & Axis: {rotation_vector_str}', (420, 60))
    draw_text(screen, f'Euler Angles: Roll: {roll:.2f}, Pitch: {pitch:.2f}, Yaw: {yaw:.2f}', (420, 100))
    draw_text(screen, f'Rotation Vector: {rotation_vector_str}', (420, 140))
    draw_text(screen, f'Rotation Matrix: {rotation_matrix_str}', (420, 180))


