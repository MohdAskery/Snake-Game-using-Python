import pygame
import random
import time
# colors
# ========================================================

white =(44,62,78,1)
# background-image: linear-gradient( 76.3deg,  rgba(44,62,78,1) 12.6%, rgba(69,103,131,1) 82.8% );
red =(255,61,89,1)
black = (229,251,31,1)
yellow=(155,254,23,1)
green=(173,255,47)
welcome_color=(26, 188, 156)
wel=(52, 73, 94)
spc=(44, 62, 80)



# ========================================================

# Game start here
screen_width = 900
screen_height = 600

pygame.init()

gameWindow = pygame.display.set_mode((screen_width, screen_height),)
pygame.display.set_caption("Snake Game")

pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

font2 = pygame.font.SysFont(None, 70)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
    
def welcome_screen_text(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    gameWindow.fill((189, 195, 199))
    welcome_screen_text("Welcome To snake Game",spc,170,220)
    text_screen("Press Space Bar To Play",wel,200,290)
    exit_welcome=False
    while not exit_welcome:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_welcome=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
    

def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = random.randint(70,140)
    snake_y = random.randint(100,180)
    snake_size = 20
    fps = 120
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(80, screen_width/1.5)
    food_y = random.randint(80,screen_height/1.5)
    
    score = 0
    inital_velocity = 3

    snk_list = []
    snk_length = 1
    
    with open("highScore.txt","r") as f:
        highScore=f.read()
        
    while not exit_game:
        
        if game_over:
            # gameWindow.fill(white)
            with open("highScore.txt","w") as f:
                f.write(str(highScore))
            text_screen("Game Over! Press Enter To continue", green, 120, 260)
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
                score += 10
                food_x = random.randint(200, screen_width-10)
                food_y = random.randint(80,screen_height-100)
                snk_length += 5
            
                if(score>int(highScore)):
                    highScore=score
                    

                
            gameWindow.fill(white)
        
            
            text_screen("High score : " + str(highScore), red, screen_width-300, 0)
            text_screen("Score: " + str(score), red, 5, 5)
            
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, yellow, (screen_width,60), (0,60), width=3)
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
# gameloop()

welcome()