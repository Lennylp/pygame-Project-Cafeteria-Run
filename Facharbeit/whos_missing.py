import pygame
import os
import random

from pygame.constants import KEYDOWN, K_d, K_s, K_w, K_a, K_u, K_h, K_j, K_k

def whos_missing(Two_Player,WIN,WIDHT,HEIGHT,fps):
    pygame.init()

    FPS = fps

    blue_points = 0
    red_points = 0
    for d in range(1,4):
        students = []
        for a in range(1,25):
            students.append("None")
        for b in range(0,10): # blue selection
            accepted = False
            while accepted == False:
                random_number = random.randint(0,23)
                if students[random_number] == "None":
                    students[random_number] = "blue"
                    accepted = True
        for c in range(0,10): # red selection
            accepted = False
            while accepted == False:
                random_number = random.randint(0,23)
                if students[random_number] == "None":
                    students[random_number] = "red"
                    accepted = True
        
        DESK_NONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','Desk_None_whos_missing.png')), (WIDHT//8,WIDHT//8))
        DESK_BLUE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','Desk_blue_whos_missing.png')), (WIDHT//8,WIDHT//8))
        DESK_RED_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','Desk_red_whos_missing.png')), (WIDHT//8,WIDHT//8))
        CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
        CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
        CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
        CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
        CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
        CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
        CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
        CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
        CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
        SITZPLAN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Whos_Missing", "sitzplan.png")), (WIDHT,HEIGHT))
        WER_FEHLT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Whos_Missing", "wer_fehlt.png")), (WIDHT,HEIGHT))
        RED_SELECTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','red_selecter.png')), (WIDHT//8,WIDHT//8))
        BLUE_SELECTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','blue_selecter.png')), (WIDHT//8,WIDHT//8))
        BLUE_RED_SELECTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Whos_Missing','blue_red_selecter.png')), (WIDHT//8,WIDHT//8))
        BLUE_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Board','Blue_Figur.png')), (54,54))
        RED_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Board','Red_Figur.png')), (54,54))
        
        def position_in_number(x_position,y_position):
            x = 0
            y = 0
            for i in range(1,9):
                if (WIDHT/8) * i == x_position:
                    x = i
            
            for i in range(0,4):
                if (HEIGHT/4) * i == y_position:
                    y = i
            
            if x == 3 or x == 6:
                return "None"
            else:
                return y * 6 + x
        
        def number_in_position_x(number):
            if number % 6 == 0:
                x = 6
            else:
                x = number % 6
    
            return x

        def number_in_position_y(number):
            if number % 6 == 0:
                y = 24 // 6
            else:
                y = (number // 6) + 1
            
            return y


        def drawselecter(WIN,red_selecter,blue_selecter):
            if blue_selecter.x == red_selecter.x and blue_selecter.y == red_selecter.y:
                WIN.blit(BLUE_RED_SELECTER_IMAGE, (blue_selecter.x,blue_selecter.y))
            else:
                WIN.blit(RED_SELECTER_IMAGE, (red_selecter.x,red_selecter.y))
                WIN.blit(BLUE_SELECTER_IMAGE, (blue_selecter.x,blue_selecter.y))


        def draw(WIN,WIDHT,HEIGHT,students):
            WIN.fill((255,255,255))
            for i in range(0,23):
                if students[i] == "blue":
                    image = DESK_BLUE_IMAGE
                elif students[i] == "red":
                    image = DESK_RED_IMAGE
                else:
                    image = DESK_NONE_IMAGE

                WIN.blit(image,((number_in_position_x(i) * WIDHT/8), (number_in_position_y(i) * HEIGHT / 4)))
            pygame.display.update()
                
        def draw_(WIN,WIDHT,HEIGHT,students):
            WIN.fill((255,255,255))
            x_postion = 0
            y_position = 0
            for y in range(0,5):
                for x in range(0,8):
                    number = None
                    number == position_in_number(x,y)
                    if x != 3 and x != 6:  
                        if students[number] == "blue":
                            image = DESK_BLUE_IMAGE
                        elif students[number] == "red":
                            image = DESK_RED_IMAGE
                        else:
                            image = DESK_NONE_IMAGE
                    else:
                        image = None

                    if image != None:
                        WIN.blit(image,(x*WIDHT/8,y*HEIGHT/4))


                x_postion = 0
                y_position += 1

            pygame.display.update()

            

        WIN.blit(SITZPLAN_IMAGE, (0,0))
        pygame.display.update()   
        pygame.time.delay(1000)    
        
        clock = pygame.time.Clock()
        draw(WIN,WIDHT,HEIGHT,students)
        dt = 0
        max_time = 10
        timer = max_time
        while timer > 0:
            timer -= dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
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

        students_missing = students.copy()
    
        accepted = False
        while accepted == False:
            blue_missing = random.randint(0,23)
            if students[blue_missing] == "blue":
                students_missing[blue_missing] = "None"
                accepted = True
                    
        accepted = False
        while accepted == False:
            red_missing = random.randint(0,23)
            if students[red_missing] == "red":
                students_missing[red_missing] = "None"
                accepted = True
        
        run = True

        WIN.blit(WER_FEHLT_IMAGE,(0,0))
        pygame.display.update()
        pygame.time.delay(4000)

        blue_selector = pygame.Rect(0,0,WIDHT//8,WIDHT//8)
        red_selector = pygame.Rect(0,0,WIDHT//8,WIDHT//8)
            

        dt = 0
        max_time = 10
        timer = max_time
        VELx = WIDHT/8
        VELy = HEIGHT/4
        while timer > 0:
            timer -= dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == KEYDOWN:
                    if True: # selector movement
                        if Two_Player == True:
                            if event.key == K_w and blue_selector.y - VELy >= 0:
                                blue_selector.y -= VELy
                            if event.key == K_s and blue_selector.y + VELy < HEIGHT:
                                blue_selector.y += VELy
                            if event.key == K_a and blue_selector.x - VELx >= 0:
                                blue_selector.x -= VELx
                            if event.key == K_d and blue_selector.x + VELx < WIDHT:
                                blue_selector.x += VELx

                            if event.key == K_u and red_selector.y - VELy >= 0:
                                red_selector.y -= VELy
                            if event.key == K_j and red_selector.y + VELy < HEIGHT:
                                red_selector.y += VELy
                            if event.key == K_h and red_selector.x - VELx >= 0:
                                red_selector.x -= VELx
                            if event.key == K_k and red_selector.x + VELx < WIDHT:
                                red_selector.x += VELx
                            
        
            draw(WIN,WIDHT,HEIGHT,students_missing)
            drawselecter(WIN,red_selector,blue_selector)

            timer_text = CLOCK_ZERO_IMAGE # timer render
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

        for i in range(1,4):
            draw(WIN,WIDHT,HEIGHT,students)
            drawselecter(WIN,red_selector,blue_selector)
            for a in range(0,blue_points):
                WIN.blit(BLUE_POINTS_IMAGE,(54 * a + 10,HEIGHT - 80))
            for a in range(0,red_points):
                WIN.blit(RED_POINTS_IMAGE,(WIDHT - (54 * a + 10),HEIGHT - 80))
            pygame.display.update()
            pygame.time.delay(1000)
            draw(WIN,WIDHT,HEIGHT,students_missing)
            drawselecter(WIN,red_selector,blue_selector)
            for a in range(0,blue_points):
                WIN.blit(BLUE_POINTS_IMAGE,(54 * a + 10,HEIGHT - 80))
            for a in range(0,red_points):
                WIN.blit(RED_POINTS_IMAGE,(WIDHT - (54 * a + 10),HEIGHT - 80))
            pygame.display.update()
            pygame.time.delay(1000)
            

        if position_in_number(blue_selector.x,blue_selector.y) == blue_missing:
            blue_points += 1
        if position_in_number(red_selector.x,red_selector.y) == red_missing:
            red_points += 1
    
    if blue_points == red_points:
        return "None"
    elif blue_points > red_points:
        return "blue"
    else:
        return "red"
             
        
                

    


#if __name__ == "__whos_missing__":
WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
whos_missing(False,WIN,WIDHT,HEIGHT,60)