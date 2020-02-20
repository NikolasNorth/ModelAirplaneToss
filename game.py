import pygame
import os


class Game:
    def __init__(self, win_width, win_height, fps, bg_img, airplane_img, obstacle_img):
        """
        Game constructor.
        Initializes pygame, creates game window, creates Clock instance and loads image assets

        :param win_width: Window width
        :param win_height: Window height
        :param fps: Frames per second
        :param bg_img: Background image file name (with extension)
        :param airplane_img: Airplane image file name (with extension)
        :param obstacle_img: Obstacle image file name (with extension)
        """
        pygame.init()
        self.win_width = win_width
        self.win_height = win_height
        self.window = pygame.display.set_mode((win_width, win_height))
        self.fps = fps
        self.bg_img = pygame.transform.scale(
            pygame.image.load(bg_img).convert_alpha(),
            (win_width, win_height)
        )
        self.airplane_img = pygame.image.load(airplane_img).convert_alpha()
        self.obstacle_img = pygame.image.load(obstacle_img).convert_alpha()
        self.clock = pygame.time.Clock()

    def get_window_width(self):
        return self.win_width

    def get_window_height(self):
        return self.win_height

    def get_window(self):
        return self.window

    def get_fps(self):
        return self.fps

    def get_bg_img(self):
        return self.bg_img

    def get_airplane_img(self):
        return self.airplane_img

    def get_obstacle_img(self):
        return self.obstacle_img

    def get_clock(self):
        return self.clock
