import pygame
import random
import time
# colors
# ========================================================

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# ========================================================

# Game start here
screen_width = 900
screen_height = 600

pygame.init()

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 70
    snake_y = 80
    snake_size = 20
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(70, screen_width-100)
    food_y = random.randint(70, screen_width-100)
    score = 0
    inital_velocity = 5

    snk_list = []
    snk_length = 1
    
    while not exit_game:
   
        if game_over:
            # gameWindow.fill(white)
            text_screen("Game Over! Press Enter To continue", red, 120, 260)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = inital_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - inital_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - inital_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = inital_velocity
                        velocity_x = 0
            if(abs(snake_x-food_x) < 12 and abs(snake_y-food_y) < 12):
                score += 1
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                inital_velocity+=0.5
                
            gameWindow.fill(white)
        
            
            text_screen("Speed: " + str(int(inital_velocity)), red, screen_width-200, 0)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (screen_width,60), (0,60), width=3)
            snake_x += velocity_x
            snake_y += velocity_y
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
    
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<=60 or snake_y >screen_height:
                game_over=True
                
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
