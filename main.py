import pygame
import constants as c

def main():
    pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')
        pygame.display.flip()

# This line ensures main() only runs if this file is executed directly
# so it would never run if it were to be imported from other files
if __name__ ==  "__main__":
    main()