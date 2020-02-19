import pygame
import os

# Define window height and width
WIN_WIDTH = 800
WIN_HEIGHT = 600

# Load assets
PLANE_IMGS = [pygame.image.load(os.path.join('assets', 'user-airplane-1.png'))]
OBSTACLE_IMG = [pygame.image.load(os.path.join('assets', 'obstacle-1.png'))]
BG_IMGS = [pygame.image.load(os.path.join('assets', 'background-1.png'))]

