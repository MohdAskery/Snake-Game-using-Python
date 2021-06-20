import pygame

pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False


# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(pygame.KEYDOWN)

pygame.quit()
quit()

