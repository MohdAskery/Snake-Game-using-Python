import pygame
import random
import time
# colors
# ========================================================

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

# ========================================================

# Game start here
screen_width=900
screen_height=600

pygame.init()

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 20
fps=60
velocity_x=0
velocity_y=0
food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_height/2)
score=0
inital_velocity=5

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    # print(snk_list)
    # [[350, 110], [355, 110], [360, 110], [365, 110], [370, 110], [375, 110]]
    for x,y in snk_list:
        # print(snk_list)
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
        
snk_list=[]
snk_length=1

while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x= inital_velocity
                velocity_y=0
            if event.key == pygame.K_LEFT:
               velocity_x= - inital_velocity
               velocity_y=0
            if event.key == pygame.K_UP:
                velocity_y= - inital_velocity
                velocity_x=0
            if event.key == pygame.K_DOWN:
                velocity_y = inital_velocity
                velocity_x=0
    if(abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12):
        score+=1
        # print("Score: ",score)
        food_x=random.randint(20,screen_width/2)
        food_y=random.randint(20,screen_height/2)
        snk_length +=5
    gameWindow.fill(white)
    text_screen("Score: " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    clock.tick(fps)
    snake_x+=velocity_x
    snake_y+=velocity_y
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]
    print(snk_length)
    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    # print(snk_list)
    # print(snk_length)
    # print("snake_x ",snake_x)
    # print("snake_y ",snake_y)
    # print("food x ",food_x)
    # print("food y ",food_y)
   

# print(snk_list)
pygame.quit()
quit()
    