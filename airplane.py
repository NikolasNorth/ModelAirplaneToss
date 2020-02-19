import pygame


class Airplane:
    # Define static variables
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20

    def __init__(self, img, x, y):
        """
        Airplane constructor.
        :param img: airplane image loaded with pygame.load()
        :param x: x-coordinate on game window
        :param y: y-coordinate on game window
        """
        self.img = img
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0  # counts number of game loop iterations
        self.velocity = 0
        self.height = self.y

    def jump(self):
        """
        Make airplane 'jump' to a higher elevation
        :return:
        """
        self.tick_count = 0  # Restart counter
        self.velocity = -10.5
        self.height = self.y  # Original position prior to jump

    def move(self):
        """
        Moves airplane
        :return:
        """
        self.tick_count += 1
        # Displacement formula allows for arc trajectory during jump
        displacement = (self.velocity * self.tick_count) + (1.5 * self.tick_count ** 2)

        # Terminal velocity
        if displacement >= 16:
            displacement = 16

        # Fine tune displacement
        if displacement < 0:
            displacement -= 2

        # Update y-coordinate position for airplane
        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            # Tilt airplane upwards
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            # Tilt airplane downwards
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY

    def draw(self, window):
        """
        Draw airplane on to game window and rotate it
        :param window: Game window
        :return:
        """
        # Rotate image around its center
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topLeft=(self.x, self.y)).center)
        window.blit(rotated_img, new_rect.topleft)