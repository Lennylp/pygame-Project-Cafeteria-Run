import pygame
import random
import os

from pygame.constants import K_k, K_w , K_s , K_a , K_d , K_u , K_h , K_j , K_k

def dasher(Two_Player,WIN,WIDHT,HEIGHT,FPS):

    max_time = 60
    timer = max_time
    dt = 0
    clock = pygame.time.Clock()
    
    class ball_:
        def __init__(self,size):
            self.rect = pygame.Rect(0, 0, 4*size,4*size)
            self.x_vel = 0
            self.y_vel = 0
            self.rect.y = HEIGHT - 200
            random_number = random.randint(1,2)
            if random_number == 1:
                self.rect.x = 200
            else:
                self.rect.x = WIDHT - 200
            
        
        def move(self,size):

            if self.rect.x < WIDHT / 2:
                if self.x_vel > 0 and self.rect.x + self.x_vel < WIDHT * 0.45 - size * 4:
                    self.rect.x += self.x_vel
                elif self.x_vel < 0 and self.rect.x + self.x_vel > 0:
                    self.rect.x += self.x_vel
            else:
                if self.x_vel > 0 and self.rect.x + self.x_vel < WIDHT- size * 4:
                    self.rect.x += self.x_vel
                elif self.x_vel < 0 and self.rect.x + self.x_vel > WIDHT * 0.55:
                    self.rect.x += self.x_vel
            
            self.rect.y += self.y_vel
            self.x_vel *= 0.8
            self.y_vel *= 0.8

        def ball_swap(self):
            if self.rect.x < WIDHT / 2:
                if self.rect.y < 5:
                    self.rect.x += WIDHT * 0.55
                    self.y_vel *= -1
            else:
                if self.rect.y < 5:
                    self.rect.x -= WIDHT * 0.55
                    self.y_vel *= -1

        def collider(self,red_player,blue_player):
            if self.rect.colliderect(red_player):
                m1, v1, m2, v2 = 100, red_player.x_vel, 0.02, ball.x_vel
                u1 = (m1 * v1 + m2 *(2*v2-v1))/(m1+m2)
                u2 = (m2 * v2 + m1 *(2*v1-v2))/(m1+m2)
                red_player.x_vel = u1
                ball.x_vel = u2
                m1, v1, m2, v2 = 100, red_player.y_vel, 0.02, ball.y_vel
                u1 = (m1 * v1 + m2 *(2*v2-v1))/(m1+m2)
                u2 = (m2 * v2 + m1 *(2*v1-v2))/(m1+m2)
                red_player.y_vel = u1
                ball.y_vel = u2
            if self.rect.colliderect(blue_player):
                m1, v1, m2, v2 = 100, blue_player.x_vel, 0.02, ball.x_vel
                u1 = (m1 * v1 + m2 *(2*v2-v1))/(m1+m2)
                u2 = (m2 * v2 + m1 *(2*v1-v2))/(m1+m2)
                blue_player.x_vel = u1
                ball.x_vel = u2
                m1, v1, m2, v2 = 100, blue_player.y_vel, 0.02, ball.y_vel
                u1 = (m1 * v1 + m2 *(2*v2-v1))/(m1+m2)
                u2 = (m2 * v2 + m1 *(2*v1-v2))/(m1+m2)
                blue_player.y_vel = u1
                ball.y_vel = u2

                
    class player:
        def __init__(self,team,size,x,y):
            self.rect = pygame.Rect(x,y,size* 4 , size * 8)
            self.team = team
            self.y_vel = 0
            self.x_vel = 0
        
        def move(self,size):

            if self.team == "blue":
                if self.x_vel > 0 and self.rect.x + self.x_vel < WIDHT * 0.45 - size * 8:
                    self.rect.x += self.x_vel
                elif self.x_vel < 0 and self.rect.x + self.x_vel > 0:
                    self.rect.x += self.x_vel
                if self.y_vel > 0 and self.rect.y + self.y_vel < HEIGHT - size * 4:
                    self.rect.y += self.y_vel
                elif self.y_vel < 0 and self.rect.y + self.y_vel > 0:
                    self.rect.y += self.y_vel
            
            if self.team == "red":
                if self.x_vel > 0 and self.rect.x + self.x_vel < WIDHT- size * 8:
                    self.rect.x += self.x_vel
                elif self.x_vel < 0 and self.rect.x + self.x_vel > WIDHT * 0.55:
                    self.rect.x += self.x_vel
                if self.y_vel > 0 and self.rect.y + self.y_vel < HEIGHT - size * 4:
                    self.rect.y += self.y_vel
                elif self.y_vel < 0 and self.rect.y + self.y_vel > 0:
                    self.rect.y += self.y_vel 


            self.x_vel *= 0.6
            self.y_vel *= 0.6
        
        
            

    size = 10
    red_player = player("red", size, (((WIDHT * 0.45 ) // 2) + (WIDHT * 0.55)) - size * 4,HEIGHT - 100)
    blue_player = player("blue", size, ((WIDHT  * 0.45) // 2) - size * 2,HEIGHT - 100)
    ball = ball_(size)

    # image import
    RED_PLAYER_IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dasher', 'Red_Team_Dasher.png')), (4*size,8*size)), 90)
    BLUE_PLAYER_IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets_Dasher', 'Blue_Team_Dasher.png')), (4*size,8*size)), 90)
    BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Dasher" , "dasher_background.png")), (WIDHT,HEIGHT))
    BALL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Dasher", "Ball_Dasher.png")), (4*size, 4 * size))
    CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
    CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
    CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
    CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
    CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
    CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
    CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
    CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
    CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
    
    def draw(red_player,blue_player,ball,WIN,WIDHT,HEIGHT):
        WIN.blit(BACKGROUND_IMAGE,(0,0))
        WIN.blit(RED_PLAYER_IMAGE, (red_player.rect.x, red_player.rect.y))
        WIN.blit(BLUE_PLAYER_IMAGE, (blue_player.rect.x, blue_player.rect.y))
        WIN.blit(BALL_IMAGE, (ball.rect.x, ball.rect.y))

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

    def movement_controller(red_player,blue_player,keys):
        Player_VEL = 5
        if keys[K_w]:
            blue_player.y_vel -= Player_VEL
        if keys[K_s]:
            blue_player.y_vel += Player_VEL
        if keys[K_a]:
            blue_player.x_vel -= Player_VEL
        if keys[K_d]:
            blue_player.x_vel += Player_VEL
        if keys[K_u]:
            red_player.y_vel -= Player_VEL
        if keys[K_j]:
            red_player.y_vel += Player_VEL
        if keys[K_h]:
            red_player.x_vel -= Player_VEL
        if keys[K_k]:
            red_player.x_vel += Player_VEL

    blue_points, red_points = 0,0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        movement_controller(red_player,blue_player,keys)
        
        red_player.move(size)
        blue_player.move(size)
        ball.collider(red_player,blue_player)
        ball.ball_swap()
        ball.move(size)

        timer -= dt
        if timer <= 0:
            if blue_points == red_points:
                return "None"
            elif red_points > blue_points:
                return "red"
            else:
                return "blue"
        dt = clock.tick(FPS) / 1000

        draw(red_player,blue_player,ball,WIN,WIDHT,HEIGHT)


WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
dasher(False,WIN,WIDHT,HEIGHT,60)
pygame.quit()