import pygame
import json 
import random
import os
from pygame.constants import K_a, K_d, K_h, K_i, K_j, K_k, K_l, K_o, K_p , K_r, K_s, K_t , K_u, K_w
    

def dogeball(Two_Player, WIN , WIDHT , HEIGHT):
    pygame.init()

    def is_blue_in_front(red,blue,blue_direction,red_direction,ball,size):
        if ball.y > blue.y * 8*size and ball.y + 4*size < blue.y and blue_direction == "None" or blue_direction == "Left" or blue_direction == "Right":
            return True
        time1 = ball.x - blue.x / BALL_VEL
        

    #colors:
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    RED = (255, 0 , 0)
    BROWN = (236,180,68)
    GREEN = (122,180,153)
    GREY = (130,130,130)

    size = 15
    FPS = 60
    VEL = 5
    BALL_VEL = 10
    max_time = 60
    timer = max_time
    dt = 0

    BLUE_HIT = pygame.USEREVENT +1
    RED_HIT = pygame.USEREVENT +2

    # blue rect
    blue1 = pygame.Rect(100,250-(8*size)/2,4*size, 8*size)
    blue1_direction = "Up"
    blue1_alive = True
    blue2 = pygame.Rect(100,400-(8*size)/2,4*size, 8*size)
    blue2_direction = "Right"
    blue2_alive = True
    blue3 = pygame.Rect(100,550-(8*size)/2,4*size, 8*size)
    blue3_direction = "Down"
    blue3_alive = True
    blue_selected = 2
    # red rect
    red1 = pygame.Rect(700,250-(8*size)/2,4*size, 8*size)
    red1_direction = "Up"
    red1_alive = True
    red2 = pygame.Rect(700,400-(8*size)/2,4*size, 8*size)
    red2_direction = "Left"
    red2_alive = True
    red3 = pygame.Rect(700,550-(8*size)/2,4*size, 8*size)
    red3_direction = "Down"
    red3_alive = True
    red_selected = 2

    if Two_Player == False:
        red2_direction = "Up"

    #ball rect
    ball = pygame.Rect(WIDHT/2 - 2*size,HEIGHT/2 - size*2,4*size,4*size)
    if random.randrange(1,3) == 1:
        ball_direction = "Left"
    else:
        ball_direction = "Right"
    ball_throw = "None"
    ball_carrier = "None"

    #pointer rect
    pointer_blue = pygame.Rect(0,0, 3*size,3*size)
    pointer_red = pygame.Rect(0,0, 3*size,3*size)    

    # image import
    BALL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball','Ball_Dogeball.png')), (4*size,4*size))
    BLUE_PLAYER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'Blue_Team_Dogeball.png')), (4*size,8 *size))
    RED_PLAYER_IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'Red_Team_Dogeball.png')), (4*size,8*size)), 180)
    BORDER_RED = pygame.Rect(WIDHT/2 -10 , 0 , 20, HEIGHT)
    BORDER_UP = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'Border_up_dogeball.png')), (WIDHT, HEIGHT//5))
    BORDER_DOWN = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'Border_down_dogeball.png')), (WIDHT, HEIGHT//5))
    POINTER_GREEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'pointer_green_dogeball.png')), (3*size,3*size))
    POINTER_RED_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'pointer_red_dogeball.png')), (3*size,3*size))
    POINTER_BLUE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dogeball', 'pointer_blue_dogeball.png')), (3*size,3*size))
    CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
    CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
    CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
    CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
    CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
    CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
    CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
    CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
    CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
    
    def draw_Display(WIN,BORDER_RED,BORDER_UP,BORDER_DOWN,pointer__blue,pointer_red,blue1,blue2,blue3,red1,red2,red3,blue1_alive,blue2_alive,blue3_alive,red1_alive,red2_alive,red3_alive,timer):
        WIN.fill(GREEN)
        pygame.draw.rect(WIN, BLACK, BORDER_RED)
        if blue1_alive == True:
            WIN.blit(BLUE_PLAYER_IMAGE, (blue1.x, blue1.y))
        if blue2_alive == True:
            WIN.blit(BLUE_PLAYER_IMAGE, (blue2.x, blue2.y))
        if blue3_alive == True:
            WIN.blit(BLUE_PLAYER_IMAGE, (blue3.x, blue3.y))
        if red1_alive == True:
            WIN.blit(RED_PLAYER_IMAGE,(red1.x,red1.y))
        if red2_alive == True:
            WIN.blit(RED_PLAYER_IMAGE,(red2.x,red2.y))
        if red3_alive == True:
            WIN.blit(RED_PLAYER_IMAGE,(red3.x,red3.y))
        WIN.blit(BORDER_UP,(0,0))
        WIN.blit(BORDER_DOWN,(0,(HEIGHT/5) * 4))
        WIN.blit(POINTER_BLUE_IMAGE,(pointer_blue.x,pointer_blue.y))
        WIN.blit(POINTER_RED_IMAGE,(pointer_red.x,pointer_red.y))
        WIN.blit(BALL_IMAGE, (ball.x,ball.y))

        timer_text = CLOCK_ZERO_IMAGE
        if timer / max_time <= (1/9)*8:
            timer_text = CLOCK_ONE_IMAGE
        if timer / max_time <= (1/9)*7:
            timer_text = CLOCK_TWO_IMAGE
        if timer / max_time <= (1/9)*6:
            timer_text = CLOCK_THREE_IMAGE
        if timer / max_time <= (1/9)*5:
            timer_text = CLOCK_FOUR_IMAGE
        if timer / max_time <= (1/9)*4:
            timer_text = CLOCK_FIVE_IMAGE
        if timer / max_time <= (1/9)*3:
            timer_text = CLOCK_SIX_IMAGE
        if timer / max_time <= (1/9)*2:
            timer_text = CLOCK_SEVEN_IMAGE
        if timer / max_time <= (1/9):
            timer_text = CLOCK_EIGHT_IMAGE
        
        WIN.blit(timer_text ,(WIDHT - 95, HEIGHT - 95))
        

        pygame.display.update()


    #ball rect
    
             
    #gameloop
    run = True
    clock = pygame.time.Clock()
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    blue_selected += 1
            
                        
                if event.key == K_o and Two_Player == True:
                    red_selected += 1
        
        
            if blue_selected == 4:
                blue_selected = 1
            if blue1_alive == False and blue_selected == 1:
                blue_selected += 1
            if blue2_alive == False and blue_selected == 2:
                blue_selected += 1
            if blue3_alive == False and blue_selected == 3:
                blue_selected += 1

            if red_selected == 4:
                red_selected = 1
            if red1_alive == False and red_selected == 1:
                red_selected += 1
            if red2_alive == False and red_selected == 2:
                red_selected += 1
            if red3_alive == False and red_selected == 3:
                red_selected += 1
                    
        
        keys_pressed = pygame.key.get_pressed()

        if True: #Movement Controller
            if Two_Player == True:
                # blue Movement Controller
                if keys_pressed[K_t]:
                    if ball_carrier == "blue1":
                        ball_direction = blue1_direction
                        ball_carrier = "None"
                        ball_throw = "blue"
                    if ball_carrier == "blue2":
                        ball_direction = blue2_direction
                        ball_carrier = "None"
                        ball_throw = "blue"
                    if ball_carrier == "blue3":
                        ball_direction = blue3_direction
                        ball_carrier = "None"
                        ball_throw = "blue"

                if blue_selected == 1:
                    if keys_pressed[K_w]:
                        blue1_direction = "Up"
                    if keys_pressed[K_s]:
                        blue1_direction = "Down"
                    if keys_pressed[K_a]:
                        blue1_direction = "Left"
                    if keys_pressed[K_d]:
                        blue1_direction = "Right"
                if blue_selected == 2:
                    if keys_pressed[K_w]:
                        blue2_direction = "Up"
                    if keys_pressed[K_s]:
                       blue2_direction = "Down"
                    if keys_pressed[K_a]:
                        blue2_direction = "Left"
                    if keys_pressed[K_d]:
                        blue2_direction = "Right"
                if blue_selected == 3:
                    if keys_pressed[K_w]:
                        blue3_direction = "Up"
                    if keys_pressed[K_s]:
                        blue3_direction = "Down"
                    if keys_pressed[K_a]:
                        blue3_direction = "Left"
                    if keys_pressed[K_d]:
                        blue3_direction = "Right"
                # red Movement Controller
                
                if keys_pressed[K_p]:
                    if ball_carrier == "red1":
                        ball_direction = red1_direction
                        ball_carrier = "None"
                        ball_throw = "red"
                    if ball_carrier == "red2":
                        ball_direction = red2_direction
                        ball_carrier = "None"
                        ball_throw = "red"
                    if ball_carrier == "red3":
                        ball_direction = red3_direction
                        ball_carrier = "None"
                        ball_throw = "red"
                if red_selected == 1:
                    if keys_pressed[K_u]:
                        red1_direction = "Up"
                    if keys_pressed[K_j]:
                        red1_direction = "Down"
                    if keys_pressed[K_h]:
                        red1_direction = "Left"
                    if keys_pressed[K_k]:
                        red1_direction = "Right"
                if red_selected == 2:
                    if keys_pressed[K_u]:
                        red2_direction = "Up"
                    if keys_pressed[K_j]:
                        red2_direction = "Down"
                    if keys_pressed[K_h]:
                        red2_direction = "Left"
                    if keys_pressed[K_k]:
                        red2_direction = "Right"
                if red_selected == 3:
                    if keys_pressed[K_u]:
                        red3_direction = "Up"
                    if keys_pressed[K_j]:
                        red3_direction = "Down"
                    if keys_pressed[K_h]:
                        red3_direction = "Left"
                    if keys_pressed[K_k]:
                        red3_direction = "Right"

            else:
                # blue Movement Controller
                
                if keys_pressed[K_t]:
                    if ball_carrier == "blue1":
                        ball_direction = blue1_direction
                        ball_carrier = "None"
                        ball_throw = "blue"
                    if ball_carrier == "blue2":
                        ball_direction = blue2_direction
                        ball_carrier = "None"
                        ball_throw = "blue"
                    if ball_carrier == "blue3":
                        ball_direction = blue3_direction
                        ball_carrier = "None"
                        ball_throw = "blue"
                if blue_selected == 1:
                    if keys_pressed[K_w]:
                        blue1_direction = "Up"
                    if keys_pressed[K_s]:
                        blue1_direction = "Down"
                    if keys_pressed[K_a]:
                        blue1_direction = "Left"
                    if keys_pressed[K_d]:
                        blue1_direction = "Right"
                if blue_selected == 2:
                    if keys_pressed[K_w]:
                        blue2_direction = "Up"
                    if keys_pressed[K_s]:
                       blue2_direction = "Down"
                    if keys_pressed[K_a]:
                        blue2_direction = "Left"
                    if keys_pressed[K_d]:
                        blue2_direction = "Right"
                if blue_selected == 3:
                    if keys_pressed[K_w]:
                        blue3_direction = "Up"
                    if keys_pressed[K_s]:
                        blue3_direction = "Down"
                    if keys_pressed[K_a]:
                        blue3_direction = "Left"
                    if keys_pressed[K_d]:
                        blue3_direction = "Right"
                #red bot controller
                if red1_alive == True:
                    red_selected = 1
                if red_selected == 1:
                    if ball.y < HEIGHT/5 + 8*size and ball_throw == "blue":
                        red1_direction = "Down"

                    else: 
                        if red1.centerx < HEIGHT / 2:
                            red1_direction = "Down"
                        else:
                            red1_direction = "Up"
                        if red1.centerx + 5 < HEIGHT / 2 and red1.centerx - 5 > HEIGHT / 2:
                            red1_direction = "Right"

                    if ball_carrier == "red1":

                        ball_direction = "Left"
                        ball_carrier = "None"
                        ball_throw = "blue"
                    
        
        if True: #move
            #blue 1
            if blue1_direction == "Up" and blue1.y + VEL > HEIGHT/5 + 10:
                blue1.y -= VEL
            if blue1_direction == "Down" and blue1.y + VEL < (HEIGHT/5)*4-8*size:
                blue1.y += VEL
            if blue1_direction == "Right" and blue1.x + VEL < WIDHT/2 -5 - 4*size:
                blue1.x += VEL
            if blue1_direction == "Left" and blue1.x - VEL > 0:
                blue1.x -= VEL
            #blue 2
            if blue2_direction == "Up" and blue2.y + VEL > HEIGHT/5 + 10:
                blue2.y -= VEL
            if blue2_direction == "Down" and blue2.y + VEL < (HEIGHT/5)*4-8*size:
                blue2.y += VEL
            if blue2_direction == "Right" and blue2.x + VEL < WIDHT/2 -5 - 4*size:
                blue2.x += VEL
            if blue2_direction == "Left" and blue2.x - VEL > 0:
                blue2.x -= VEL
            #blue 3
            if blue3_direction == "Up" and blue3.y + VEL > HEIGHT/5 + 10:
                blue3.y -= VEL
            if blue3_direction == "Down" and blue3.y + VEL < (HEIGHT/5)*4-8*size:
                blue3.y += VEL
            if blue3_direction == "Right" and blue3.x + VEL < WIDHT/2 -5 - 4*size:
                blue3.x += VEL
            if blue3_direction == "Left" and blue3.x - VEL > 0:
                blue3.x -= VEL
            #red 1
            if red1_direction == "Up" and red1.y + VEL > HEIGHT/5 + 10:
                red1.y -= VEL
            if red1_direction == "Down" and red1.y + VEL < (HEIGHT/5)*4-8*size:
                red1.y += VEL
            if red1_direction == "Right" and red1.x + VEL < WIDHT-4*size:
                red1.x += VEL
            if red1_direction == "Left" and red1.x - VEL > WIDHT/2 +5:
                red1.x -= VEL
            #red 2
            if red2_direction == "Up" and red2.y + VEL > HEIGHT/5 + 10:
                red2.y -= VEL
            if red2_direction == "Down" and red2.y + VEL < (HEIGHT/5)*4-8*size:
                red2.y += VEL
            if red2_direction == "Right" and red2.x + VEL < WIDHT-4*size:
                red2.x += VEL
            if red2_direction == "Left" and red2.x - VEL > WIDHT/2 +5:
                red2.x -= VEL
            #red 3
            if red3_direction == "Up" and red3.y + VEL > HEIGHT/5 + 10:
                red3.y -= VEL
            if red3_direction == "Down" and red3.y + VEL < (HEIGHT/5)*4-8*size:
                red3.y += VEL
            if red3_direction == "Right" and red3.x + VEL < WIDHT-4*size:
                red3.x += VEL
            if red3_direction == "Left" and red3.x - VEL > WIDHT/2 +5:
                red3.x -= VEL
            
        if True: #Ball movement + death + collider
            #Ball movement
            ball_player_distance = 60
            if ball_direction == "None":
                if ball_carrier == "blue1":
                    ball.x = blue1.x + ball_player_distance
                    ball.y = blue1.y + 30
                if ball_carrier == "blue2":
                    ball.x = blue2.x + ball_player_distance
                    ball.y = blue2.y + 30
                if ball_carrier == "blue3":
                    ball.x = blue3.x + ball_player_distance 
                    ball.y = blue3.y + 30
                if ball_carrier == "red1":
                    ball.x = red1.x - ball_player_distance
                    ball.y = red1.y + 30
                if ball_carrier == "red2":
                    ball.x = red2.x - ball_player_distance
                    ball.y = red2.y + 30
                if ball_carrier == "red3":
                    ball.x = red3.x - ball_player_distance
                    ball.y = red3.y + 30
            
            if ball_direction == "Up":
                if ball.y + BALL_VEL > HEIGHT/5 + 10:
                    ball.y -= BALL_VEL
                else:
                    ball_direction = "None"
                    ball_throw = "None"
            if ball_direction == "Down":
                if ball.y + BALL_VEL < (HEIGHT/5)*4-2*size:
                    ball.y += BALL_VEL
                else:
                    ball_direction = "None"
                    ball_throw = "None"
            if ball_direction == "Left":
                if ball.x - BALL_VEL > -5:
                    ball.x -= BALL_VEL
                else:
                    ball_direction = "None"
                    ball_throw = "None"
            if ball_direction == "Right":
                if ball.x + BALL_VEL < WIDHT - 3.5*size:
                    ball.x += BALL_VEL
                else:
                    ball_direction = "None"
                    ball_throw = "None"
            
            #collider + death
            
            if ball.colliderect(blue1) and blue1_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "blue1"
                if ball_direction != "None" and ball_throw =="red":
                    blue1_alive = False
                    blue1.x = 100
                    blue1.y = 0
                    if blue1_alive == False and blue2_alive == False and blue3_alive == False:
                        return "red"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "red":
                    ball_direction = "None"
            if ball.colliderect(blue2) and blue2_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "blue2"
                if ball_direction != "None" and ball_throw =="red":
                    blue2_alive = False
                    blue2.x = 100
                    blue2.y = 0
                    if blue1_alive == False and blue2_alive == False and blue3_alive == False:
                        return "red"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "red":
                    ball_direction = "None"
            if ball.colliderect(blue3) and blue3_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "blue3"
                if ball_direction != "None" and ball_throw =="red":
                    blue3_alive = False
                    blue3.x = 100
                    blue3.y = 0
                    if blue1_alive == False and blue2_alive == False and blue3_alive == False:
                        return "red"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "red":
                    ball_direction = "None"
            

            if ball.colliderect(red1) and red1_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "red1"
                if ball_direction != "None" and ball_throw =="blue":
                    red1_alive = False
                    red1.x = 100
                    red1.y = 0
                    if red1_alive == False and red2_alive == False and red3_alive == False:
                        return "blue"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "blue":
                    ball_direction = "None"
            if ball.colliderect(red2) and red2_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "red2"
                if ball_direction != "None" and ball_throw =="blue":
                    red2_alive = False
                    red2.x = 100
                    red2.y = 0
                    if red1_alive == False and red2_alive == False and red3_alive == False:
                        return "blue"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "blue":
                    ball_direction = "None"
            if ball.colliderect(red3) and red3_alive == True:
                if ball_direction == "None" and ball_carrier == "None":
                    ball_carrier = "red3"
                if ball_direction != "None" and ball_throw =="blue":
                    red3_alive = False
                    red3.x = 100
                    red3.y = 0
                    if red1_alive == False and red2_alive == False and red3_alive == False:
                        return "blue"
                    ball_direction = "None"
                    ball_throw = "None"
                if ball_direction != "None" and ball_throw != "blue":
                    ball_direction = "None"

        if True: #pointer
            if blue_selected == 1:
                pointer_blue.x = blue1.x + 5
                pointer_blue.y = blue1.y + 10
            if blue_selected == 2:
                pointer_blue.x = blue2.x + 5
                pointer_blue.y = blue2.y + 10
            if blue_selected == 3:
                pointer_blue.x = blue3.x + 5
                pointer_blue.y = blue3.y + 10
            if red_selected == 1:
                pointer_red.x = red1.x + 5
                pointer_red.y = red1.y + 10
            if red_selected == 2:
                pointer_red.x = red2.x + 5
                pointer_red.y = red2.y + 10
            if red_selected == 3:
                pointer_red.x = red3.x + 5
                pointer_red.y = red3.y + 10
            
        timer -= dt
        if timer <= 0:
            run = False
            return "None"
        dt = clock.tick(FPS) / 1000
        draw_Display(WIN,BORDER_RED,BORDER_UP,BORDER_DOWN,pointer_blue,pointer_red,blue1,blue2,blue3,red1,red2,red3,blue1_alive,blue2_alive,blue3_alive,red1_alive,red2_alive,red3_alive, timer)

#if __name__ == "__dogeball__":
WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
dogeball(True,WIN,WIDHT,HEIGHT)
pygame.quit()


