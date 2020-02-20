import pygame
import random


class Obstacle:
    # Define static variables
    GAP = 200  # Space in between set of pipes
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

    def get_x(self):
        return self.x

    def get_passed(self):
        return self.passed

    def set_passed(self, is_passed):
        self.passed = is_passed

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
        airplane_mask = airplane.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # Distance between two top left-hand corners
        top_offset = (self.x - airplane.get_x(), self.top - round(airplane.get_y()))
        # Distance between two bottom left-hand corners
        bottom_offset = (self.x - airplane.get_x(), self.bottom - round(airplane.get_y()))

        # Determine point of overlap between airplane and bottom pipe
        b_point = airplane_mask.overlap(bottom_mask, bottom_offset)
        # Determine the point of overlap between airplane and top pipe
        t_point = airplane_mask.overlap(top_mask, top_offset)

        # Check if collision has occurred
        if b_point or t_point:
            # Collision has occurred
            return True
        else:
            # No collision
            return False
