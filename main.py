import pygame
import os
import sys
from game import Game
from airplane import Airplane
from obstacle import Obstacle


def welcome_screen(game):
    """
    Display welcome screen on to window.

    :param game: Game object
    :return:
    """
    # Main title
    main_x = 10
    main_y = 10
    msg_main = game.get_font().render("Model Airplane Toss", 1, (255, 255, 255))

    # Subtitle
    sub_x = 10
    sub_y = game.get_window_height() - 30
    msg_sub = game.get_font().render("Press space bar to start!", 1, (255, 255, 255))

    # Game loop
    run = True
    while run:
        game.get_clock().tick(game.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Start the game
                    game.set_game_in_session(True)
                    return
            else:
                # Set background screen to black
                game.get_window().fill((0, 0, 0))

                # Display messages on to screen
                game.get_window().blit(msg_main, (main_x, main_y))
                game.get_window().blit(msg_sub, (sub_x, sub_y))

                # Update game window
                pygame.display.update()


def game_over_screen(game):
    """
    Display game over screen on to window.

    :param game: Game object
    :return:
    """
    # Score message
    score_x = 10
    score_y = 10
    score_msg = game.get_font().render("Final Score: " + str(game.get_score()), 1, (255, 255, 255))

    # Restart game message
    restart_x = 10
    restart_y = game.get_window_height() - 100
    restart_msg = game.get_font().render("To play again, click the space bar!", 1, (255, 255, 255))

    # Game loop
    run = True
    while run:
        game.get_clock().tick(game.get_fps())

        # Ask user if they want to quit or restart game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close game window
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Restart game
                    game.set_game_in_session(True)
                    game.reset_score()
                    return
            else:
                # Set background colour to black
                game.get_window().fill((0, 0, 0))

                # Display score on to screen
                game.get_window().blit(score_msg, (score_x, score_y))

                # Display restart message on to screen
                game.get_window().blit(restart_msg, (restart_x, restart_y))

                # Update game window
                pygame.display.update()


def draw_window(window, airplane, obstacles, bg_img, bg_x, bg_x2, font, score):
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
    msg = font.render("Score: " + str(score), 1, (255, 255, 255))
    window.blit(msg, (10, 10))

    # Update game window
    pygame.display.update()


def main(game):
    """
    Main game logic.

    :param game: Game object
    :return:
    """
    airplane = Airplane(game.get_airplane_img(), 200, 200)
    obstacles = [Obstacle(game.get_obstacle_img(), 700)]
    window = game.get_window()
    clock = game.get_clock()
    font = game.get_font()

    # Define position of sliding background images
    bg_x = 0
    bg_x2 = game.get_window_width()

    # Start game
    run = True
    while run:
        is_jump = False
        clock.tick(FPS)  # Limit game loop to 30 iterations per second

        # Process user input from keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close the game window
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    airplane.jump()
                    is_jump = True
        if not is_jump:
            airplane.move()

        # Check if airplane has fallen off screen
        if airplane.get_y() <= 0 or airplane.get_y() >= game.get_window_height():
            # Game over. Go to game over screen
            run = False
            game.set_game_in_session(False)
            return

        # Generate obstacle
        add_obstacle = False
        for obstacle in obstacles:
            if obstacle.collide(airplane):
                # Airplane hit obstacle. Go to game over screen
                run = False
                game.set_game_in_session(False)
                return
            if not obstacle.get_passed() and obstacle.get_x() < airplane.get_x():
                # Obstacle has been successfully passed, set flag to generate new obstacle
                obstacle.set_passed(True)
                add_obstacle = True
            obstacle.move()
        if add_obstacle:
            # Generate a new obstacle and increment score by 1
            game.increment_score()
            obstacles.append(Obstacle(game.get_obstacle_img(), 700))

        # Update game window with changes
        draw_window(window, airplane, obstacles, game.get_bg_img(), bg_x, bg_x2, font, game.get_score())

        # Sliding background
        bg_x -= 2
        bg_x2 -= 2
        if bg_x < -game.get_window_width():
            bg_x = game.get_window_width()
        if bg_x2 < -game.get_window_width():
            bg_x2 = game.get_window_width()


if __name__ == '__main__':
    # Define window height, window width and frames per second
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    FPS = 30

    # Background images
    BG_IMGS = [
        os.path.join('assets', 'background-1.png')
    ]
    # Airplane images
    airplanes = [
        os.path.join('assets', 'user-airplane-1.png')
    ]
    # Obstacle images
    OBSTACLE = [
        os.path.join('assets', 'obstacle-1.png')
    ]

    # Setup game settings
    game_settings = Game(WIN_WIDTH, WIN_HEIGHT, FPS, BG_IMGS[0], airplanes[0], OBSTACLE[0], "comicsans")

    # Launch game
    welcome_screen(game_settings)
    while True:
        if game_settings.get_game_in_session():
            main(game_settings)
        else:
            game_over_screen(game_settings)
