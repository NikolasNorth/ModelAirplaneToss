import pygame
import os
from game import Game
from airplane import Airplane
from obstacle import Obstacle


# TODO: After this function is called decrement bg_x and bg_x2 by 2
def draw_window(window, airplane, obstacles, bg_img, bg_x, bg_x2):
    """
    Draw window for the game.

    :param window: Game window
    :param airplane: User airplane
    :param obstacles: Obstacle
    :param bg_img: Background image already loaded using pygame.load() function
    :param bg_x: x-coordinate position for background image
    :param bg_x2: x-coordinate position for second background image
    :param font: Loaded pygame font
    :param score: Game score
    :return:
    """
    # Draw sliding background image on to game window
    window.blit(bg_img, (bg_x, 0))
    window.blit(bg_img, (bg_x2, 0))

    # Draw moving pipe on to game window
    for obstacle in obstacles:
        obstacle.draw(window)

    # Draw airplane (with tilting and rotation) on to game window
    airplane.draw(window)

    # Draw score on to game window
    # msg = font.render("Score: " + str(score), 1, (255, 255, 255))
    # window.blit(msg, (10, 10))

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
    OBSTACLE = [
        os.path.join('assets', 'obstacle-1.png')
    ]

    # Initialize Game
    game = Game(WIN_WIDTH, WIN_HEIGHT, FPS, BG_IMGS[0], AIRPLANES[0], OBSTACLE[0], "comicsans")

    airplane = Airplane(game.get_airplane_img(), 200, 200)
    obstacles = [Obstacle(game.get_obstacle_img(), 700)]
    window = game.get_window()
    clock = game.get_clock()
    # font = game.get_font()

    run = True
    bg_x = 0
    bg_x2 = game.get_window_width()
    score = 0
    is_jump = False
    while run:
        is_jump = False
        # Main game loop
        clock.tick(FPS)  # Limit game loop to 30 iterations per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    airplane.jump()
                    is_jump = True
        if not is_jump:
            airplane.move()
        add_obstacle = False
        for obstacle in obstacles:
            if obstacle.collide(airplane):
                print("collision")
            if not obstacle.get_passed() and obstacle.get_x() < airplane.get_x():
                # Obstacle has been successfully passed, set flag to generate new obstacle
                obstacle.set_passed(True)
                add_obstacle = True
            obstacle.move()
        if add_obstacle:
            # Generate a new obstacle and increment score by 1
            score += 1
            obstacles.append(Obstacle(game.get_obstacle_img(), 700))
        draw_window(window, airplane, obstacles, game.get_bg_img(), bg_x, bg_x2)
        # draw_window(window, airplane, obstacles, game.get_bg_img(), bg_x, bg_x2, font, score)
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
