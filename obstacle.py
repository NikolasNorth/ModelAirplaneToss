import pygame
import random


class Obstacle:
    # Define static variables
    GAP = 150  # Space in between set of pipes
    VELOCITY = 5  # How fast pipe will be moving towards the bird

    def __init__(self, img, x):
        """
        Pipe constructor.
        Creates pipe obstacle of random height

        :param img: pipe img loaded with pygame.image.load() function
        :param x: x-coordinate position in game window
        """
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(img, False, True)  # Flip pipe img
        self.PIPE_BOTTOM = img
        self.passed = False  # Flag for airplane successfully passing through gap
        self.set_height()

    def set_height(self):
        """
        Set the height of the top pipe and bottom pipe when this object is created.
        :return:
        """
        self.height = random.randrange(120, 320)
        # Set top pipe and bottom pipe position in game window
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        """
        Move pipe img towards airplane
        :return:
        """
        self.x -= self.VELOCITY

    def draw(self, window):
        """
        Draw pipe on to game window
        :param window: Game window
        :return:
        """
        window.blit(self.PIPE_TOP, (self.x, self.top))
        window.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, airplane):
        # TODO: Implement this method
        """

        :param airplane: Airplane object
        :return:
        """
        pass
