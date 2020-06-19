import pygame
import time
import random


pygame.init()

dis_width = 800
dis_height = 600

dis=pygame.display.set_mode((dis_width,dis_height))

white=(255,255,255)
blue=(50,50,50)
red=(255,0,0)
black=(0,0,0)
yellow =(255,255,102)
green=(0, 255, 0)

pygame.display.set_caption('Snake')



clock = pygame.time.Clock()



font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value=score_font.render("Score:" +str(score), True,black)
    dis.blit(value,[0,0])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,yellow,[x[0],x[1],snake_block,snake_block])

def message(msg ,color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/6,dis_height/3])
def gameLoop():

    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_list=[]
    snake_length=1

    snake_speed =15
    snake_block =20

    food_x=round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block
    food_y=round(random.randrange(0,dis_height-snake_block)/snake_block)*snake_block

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message('You Lost! Press any key to Play again  Q to quit', red)
            your_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
 
                if event.type==pygame.KEYDOWN:
                    print(event.type)

                    if event.key == pygame.QUIT:
                         pygame.quit()
                         quit()

                    if event.key == pygame.K_q or event.key == pygame.QUIT:
                        game_over=True
                        game_close=False
                        return
                    else:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change =snake_block

        if x1 >= dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)


        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close=True

        our_snake(snake_block, snake_list)
        your_score(snake_length-1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            snake_length += 1
        clock.tick(snake_speed)


    pygame.quit()

    quit()



gameLoop()