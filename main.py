import pygame
import sys


def welcome_screen():
    """
    Display welcome screen to the user
    :return:
    """
    # Position of intro title
    original_title_width = GAME_TITLES['default-main'].get_width()
    original_title_height = GAME_TITLES['default-main'].get_height()
    scaled_title_width = 700
    scaled_title_height = int((scaled_title_width / original_title_width) * original_title_height)
    title_x_position = 50
    title_y_position = int(SCREEN_HEIGHT / 4)

    # Position of subtitle
    original_subtitle_width = GAME_TITLES['default-secondary'].get_width()
    orginal_subtitle_height = GAME_TITLES['default-secondary'].get_height()
    scaled_subtitle_width = 500
    scaled_subtitle_height = int((scaled_subtitle_width / original_subtitle_width) * orginal_subtitle_height)
    subtitle_x_position = 150  # Center of window
    substitle_y_position = 500

    # Position of model airplane
    airplane_x_position = int(SCREEN_WIDTH / 2) - 50  # Center of window
    airplane_y_position = 300

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close game if user exits window
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Start game if user clicks space bar
                return
            else:
                # Display welcome screen
                SCREEN.fill((0, 0, 0))
                SCREEN.blit(
                    pygame.transform.scale(GAME_TITLES['default-main'], (scaled_title_width, scaled_title_height)),
                    (title_x_position, title_y_position)
                )
                SCREEN.blit(
                    pygame.transform.scale(GAME_TITLES['default-secondary'], (scaled_subtitle_width, scaled_subtitle_height)),
                    (subtitle_x_position, substitle_y_position)
                )
                SCREEN.blit(
                    pygame.transform.rotate(pygame.image.load(AIRPLANES['default']).convert_alpha(), 20),
                    (airplane_x_position, airplane_y_position)
                )

                pygame.display.update()


def main_game():
    print('Game has started!')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def get_building_obstacle(building_type='default'):
    """
    Returns a building obstacle of random height
    :return:
    """
    pass


def main():
    global SCREEN
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global FRAMES_PER_SECOND
    global AIRPLANES
    global BACKGROUNDS
    global BUILDINGS
    global BIRDS
    global GAME_TITLES

    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FRAMES_PER_SECOND = 30

    AIRPLANES = {
        'default': 'assets/user-airplane-1.png'
    }

    BACKGROUNDS = {
        'default': ''
    }

    BUILDINGS = {
        'default': 'assets/building-1.png'
    }

    GAME_TITLES = {
        'default-main': pygame.image.load('assets/game-title-1.png').convert_alpha(),
        'default-secondary': pygame.image.load('assets/game-subtitle-1.png').convert_alpha()
    }

    pygame.display.set_caption("Model Airplane Toss")
    pygame.display.set_icon(pygame.image.load('assets/airplane-icon-1.png').convert_alpha())

    # Start Game
    welcome_screen()
    main_game()


if __name__ == '__main__':
    main()
