import pygame


class Airplane:

    def __init__(self, name, img_url, x_pos=0, y_pos=0):
        self.name = name
        self.img = pygame.image.load(img_url).convert_alpha()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.position = (self.x_pos, self.y_pos)

    def get_name(self):
        return self.name

    def get_img(self):
        return self.img

    def get_x_position(self):
        return self.x_pos

    def get_y_position(self):
        return self.y_pos

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name

    def set_img_url(self, img_url):
        self.img = pygame.image.load(img_url).convert_alpha()

    def set_x_position(self, x_pos):
        self.x_pos = x_pos
        self.position = (x_pos, self.y_pos)

    def set_y_position(self, y_pos):
        self.y_pos = y_pos
        self.position = (self.x_pos, y_pos)

    def set_position(self, x_pos, y_pos):
        self.set_x_position(x_pos)
        self.set_y_position(y_pos)
