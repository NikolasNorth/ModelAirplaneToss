import pygame

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAMES_PER_SECOND = 30  # TODO: use this to create a counting clock with (see line 61 and 187)

AIRPLANES = [
    # Default
    'assets/user-airplane-1.png'
]

BACKGROUNDS = []


def main():
    global SCREEN

    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Model Airplane Toss")
    pygame.display.set_icon(pygame.image.load('assets/airplane-icon-1.png').convert_alpha())

    AIRPLANES = [
        # Default
        'assets/user-airplane-1.png'
    ]

    # Game Loop (Terminate program if game window is closed)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Change window background colour (R,G,B)
        SCREEN.fill((140, 0, 0))

        # Display player onto the screen over
        player(AIRPLANES[0])

        # Update game window
        pygame.display.update()


def player(airplane_img):
    playerX = 200
    playerY = 300
    # Draw image of player onto game window display
    SCREEN.blit(pygame.image.load(airplane_img).convert_alpha(), (playerX, playerY))


if __name__ == '__main__':
    main()
