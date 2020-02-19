import pygame
import os
from game import Game
from airplane import Airplane


# TODO: After this function is called decrement bg_x and bg_x2 by 2
def draw_window(window, airplane, bg_img, bg_x, bg_x2):
    """
    Draw window for the game.

    :param window: Game window
    :param airplane: User airplane
    :param bg_img: Background image already loaded using pygame.load() function
    :param bg_x: x-coordinate position for background image
    :param bg_x2: x-coordinate position for second background image
    :return:
    """
    # Draw sliding background image on to game window
    window.blit(bg_img, (bg_x, 0))
    window.blit(bg_img, (bg_x2, 0))

    # Draw airplane (with tilting and rotation) on to game window
    airplane.draw(window)

    # Update game window
    pygame.display.update()


def main():
    # Define window height and width
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    FPS = 30

    # Image file path's
    BG_IMGS = [
        os.path.join('assets', 'background-1.png')
    ]
    AIRPLANES = [
        os.path.join('assets', 'user-airplane-1.png')
    ]
    OBSTACLE = []

    # Initialize Game
    game = Game(WIN_WIDTH, WIN_HEIGHT, FPS, BG_IMGS[0], AIRPLANES[0])

    airplane = Airplane(game.get_airplane_img(), 200, 200)
    window = game.get_window()
    clock = game.get_clock()

    run = True
    bg_x = 0
    bg_x2 = game.get_window_width()
    while run:
        # Main game loop
        clock.tick(FPS)  # Limit game loop to 30 iterations per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        airplane.move()
        draw_window(window, airplane, game.get_bg_img(), bg_x, bg_x2)
        bg_x -= 2
        bg_x2 -= 2
        if bg_x < -game.get_window_width():
            bg_x = game.get_window_width()
        if bg_x2 < -game.get_window_width():
            bg_x2 = game.get_window_width()


if __name__ == '__main__':
    # TODO: Implement welcome_screen method
    # TODO: Add logic to delay the start of the game when user presses space bar (similar to flappybird.io)
    main()
