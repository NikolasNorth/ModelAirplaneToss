import pygame
import sys


def welcome_screen():
    """
    Show welcome screen.
    :return: None
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
    original_subtitle_height = GAME_TITLES['default-secondary'].get_height()
    scaled_subtitle_width = 500
    scaled_subtitle_height = int((scaled_subtitle_width / original_subtitle_width) * original_subtitle_height)
    subtitle_x_position = 150  # Center of window
    subtitle_y_position = 500

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
                    pygame.transform.scale(GAME_TITLES['default-secondary'],
                                           (scaled_subtitle_width, scaled_subtitle_height)),
                    (subtitle_x_position, subtitle_y_position)
                )
                SCREEN.blit(
                    pygame.transform.rotate(pygame.image.load(AIRPLANES['default']).convert_alpha(), 20),
                    (airplane_x_position, airplane_y_position)
                )

                pygame.display.update()


def main_game():
    """
    Run game.
    :return: None
    """
    # Set background image
    background_x = 0  # Initial x-coordinate for 1st background image
    background_x2 = SCREEN_WIDTH  # Initial x-coordinate for 2nd background image
    SCREEN.fill((0, 0, 0))
    x_pos = 50
    y_pos = 50
    while True:
        key = False
        # Display both images
        SCREEN.blit(
            pygame.transform.scale(BACKGROUNDS['default'], (SCREEN_WIDTH, SCREEN_HEIGHT)),
            (background_x, 0)
        )
        SCREEN.blit(
            pygame.transform.scale(BACKGROUNDS['default'], (SCREEN_WIDTH, SCREEN_HEIGHT)),
            (background_x2, 0)
        )

        # Display airplane
        SCREEN.blit(
            pygame.image.load(AIRPLANES['default']).convert_alpha(),
            (x_pos, y_pos)
        )
        pygame.display.update()
        background_x -= 2  # TODO: This is what controls the speed of the airplane flying (use this for setting different difficulty modes)
        background_x2 -= 2
        if background_x < -SCREEN_WIDTH:
            background_x = SCREEN_WIDTH
        if background_x2 < -SCREEN_WIDTH:
            background_x2 = SCREEN_WIDTH
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit application if user closes the game window
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Go back to welcome screen if user presses ESCAPE key
                    welcome_screen()
                elif event.key == pygame.K_SPACE:
                    # Make airplane 'jump' to higher elevation
                    y_pos -= 40
                    key = True
        if key:
            y_pos += 0
        else:
            y_pos += 4
        FPS_CLOCK.tick(FPS)


def get_building_obstacle(building_type='default'):
    """
    Returns a building obstacle of random height
    :return:
    """
    pass


def main():
    # Initialize global variables
    global SCREEN
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global FPS
    global FPS_CLOCK
    global AIRPLANES
    global BACKGROUNDS
    global BUILDINGS
    global BIRDS
    global GAME_TITLES

    # Initialize pygame
    pygame.init()

    # Set global variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 30
    FPS_CLOCK = pygame.time.Clock()
    AIRPLANES = {
        'default': 'assets/user-airplane-1.png'
    }
    BACKGROUNDS = {
        'default': pygame.image.load('assets/background-1.png').convert_alpha()
    }
    BUILDINGS = {
        'default': 'assets/building-1.png'
    }
    GAME_TITLES = {
        'default-main': pygame.image.load('assets/game-title-1.png').convert_alpha(),
        'default-secondary': pygame.image.load('assets/game-subtitle-1.png').convert_alpha()
    }

    # Set caption and icon for game window
    pygame.display.set_caption("Model Airplane Toss")
    pygame.display.set_icon(pygame.image.load('assets/airplane-icon-1.png').convert_alpha())

    # Start Game
    welcome_screen()
    main_game()


if __name__ == '__main__':
    main()
