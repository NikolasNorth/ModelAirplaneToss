import pygame


class Game:
    def __init__(self, win_width, win_height, fps, bg_img, airplane_img, obstacle_img, font_name):
        """
        Game constructor.
        Initializes pygame, initializes pygame font, creates game window, creates Clock instance and loads image assets.
        Provides logic for the welcome screen.

        :param win_width: Window width
        :param win_height: Window height
        :param fps: Frames per second
        :param bg_img: Background image file name (with extension)
        :param airplane_img: Airplane image file name (with extension)
        :param obstacle_img: Obstacle image file name (with extension)
        :param font_name: Name of desired font
        """
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(font_name, 50)
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
        self.score = 0
        self.game_in_session = False

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

    def get_font(self):
        return self.font

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def get_game_in_session(self):
        return self.game_in_session

    def set_game_in_session(self, is_game_in_session):
        self.game_in_session = is_game_in_session
