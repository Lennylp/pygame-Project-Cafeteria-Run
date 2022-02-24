import pygame
import os
import random
from pygame.constants import K_d, K_j, K_k, K_s, K_u, K_w

def true_or_false(WIN,WIDHT,HEIGHT,FPS):

    pygame.init()

    LIGHT_GRAY = (229,229,229)
    DARK_GRAY = (185,185,185)
    DARKER_GRAY = (150,150,150)
    BLUE = (111,117,204)
    RED = (204,111,111)

    BLUE_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_blue.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
    RED_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_red.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
    CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
    CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
    CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
    CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
    CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
    CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
    CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
    CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
    CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
        
    def blit_text_to_screen(x,y,text,size,color):
        font = pygame.font.Font(None,int(size))
        text = font.render(text,True,color)
        WIN.blit(text,(x,y))


    def blit_text_to_screen_center(center_x,center_y,text,size,color): #from titlescreen
        font = pygame.font.Font(None,int(size))
        text = font.render(text,True,color)
        text_rect = text.get_rect(center = (center_x, center_y))
        WIN.blit(text,text_rect)

    def blit_text_to_screen_center_for_show(center_x,center_y,text,color):
        if len(text) > 7:
            lenght = (1 / (len(text) * 0.55)) * WIDHT
            font = pygame.font.Font(None,int(lenght))
            text = font.render(text,True,color)
            text_rect = text.get_rect(center = (center_x, center_y))
            WIN.blit(text,text_rect)
        else:
            blit_text_to_screen_center(center_x,center_y,text,WIDHT * 0.1,DARK_GRAY)

    def show_main(points_blue,points_red,number_of_rounds):
        WIN.fill(LIGHT_GRAY)
        blit_text_to_screen_center(WIDHT*2.5/10,HEIGHT/2,"TRUE", int(WIDHT*0.15),DARKER_GRAY)
        blit_text_to_screen_center(WIDHT/2,HEIGHT/2,"or", int(WIDHT*0.1),DARK_GRAY)
        blit_text_to_screen_center(WIDHT*7.5/10,HEIGHT/2,"FALSE", int(WIDHT*0.15),DARKER_GRAY)

        y = 5
        x = 5
        for i in range(0,points_blue):
            WIN.blit(BLUE_POINTS_IMAGE,(x,y))
            x += WIDHT*0.0657 + 5
        
        x = WIDHT - 5 - WIDHT*0.0657
        for i in range(0,points_red):
            WIN.blit(RED_POINTS_IMAGE,(x,y))
            x -= WIDHT*0.0657 + 5

        blit_text_to_screen(5, HEIGHT - HEIGHT * 0.05 - 5, f"Amount of rounds: {number_of_rounds}" ,HEIGHT * 0.05, DARK_GRAY)

        pygame.display.update()
        clock = pygame.time.Clock()
        dt = 0
        max_time = 3
        timer = max_time
        while timer > 0:
            timer -= dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        

    def game(show,true_or_false,blue_points,red_points,number_of_rounds):
        show_main(blue_points,red_points,number_of_rounds)
        red_selected = ""
        blue_selected = ""
        
        clock = pygame.time.Clock()
        dt = 0
        max_time = 3
        timer = max_time
        while timer > 0:
            timer -= dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[K_w]:
                        blue_selected = "True"
                        timer = 0
                    if keys[K_s]:
                        blue_selected = "False"
                        timer = 0

                    if keys[K_u]:
                        red_selected = "True"
                        timer = 0
                    if keys[K_j]:
                        red_selected = "False"
                        timer = 0
            
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
    

            WIN.fill(LIGHT_GRAY)
            blit_text_to_screen_center_for_show(WIDHT/2,HEIGHT/2,show,DARK_GRAY)
            WIN.blit(timer_text ,(WIDHT - 95, HEIGHT - 95))

            pygame.display.update()
                                        

        WIN.fill(LIGHT_GRAY)
        blit_text_to_screen_center_for_show(WIDHT/2,HEIGHT/2,show,DARK_GRAY)

        if blue_selected == "" and red_selected == "":
            blit_text_to_screen_center(WIDHT/2,(HEIGHT*3)/4,"Nothing chosen: No points",WIDHT * 0.09,DARK_GRAY)
            pygame.display.update()
        elif blue_selected == "" and red_selected != "":
            if red_selected == true_or_false:
                blit_text_to_screen_center(WIDHT*3/4,(HEIGHT*3)/4,"True", WIDHT * 0.09,RED)
                red_points += 1
            else:
                blit_text_to_screen_center(WIDHT*3/4,(HEIGHT*3)/4,"False", WIDHT * 0.09,RED)
                blue_points += 1
        else:
            if blue_selected == true_or_false:
                blit_text_to_screen_center(WIDHT/4,(HEIGHT*3)/4,"True", WIDHT * 0.09,BLUE)
                blue_points += 1
            else:
                blit_text_to_screen_center(WIDHT/4,(HEIGHT*3)/4,"False", WIDHT * 0.09,BLUE)
                red_points += 1
        
        pygame.display.update()
        
        dt = 0
        max_time = 1.5
        timer = max_time
        while timer > 0:
            timer -= dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        return (blue_points,red_points)

                    


    true = ['LRS-Foerderung Kl. 7-8','LRS-Foerderung Kl. 9','LRS Foerderung Kl.10 gerade Woche','LRS Foerderung Kl.11 ungerade Woche','Vorbereitung Mathematikolympiaden Kl. 7/8','Vorbereitung Mathematikolympiaden Kl. 9/10','Vorbereitung Mathematikolympiaden Kl. 11-12','Foerderunterricht Mathematik Kl. 7 u. 8','Foerderunterricht Mathematik Kl. 9','Foerderunterricht Mathematik Kl.10','Robotik Kl.7/8','Robotik Kl.9/10','Formel 1 in der Schule','AG Schach Anfänger und Fortgeschrittene','AG – Bienen','Foerderunterricht Englisch Kl. 7 u. 8','Foerderunterricht Englisch Kl. 9','Foerderunterricht Englisch Kl.10','Jugend debattiert Kl.7/8 und Kl.9/10','Schülerfirma „school fashion“ Kl.7/8 und Kl.9/10','Schülercafé „Schüleroase“ Kl.7/8 und Kl.9/10','Streitschlichter Kl.7/8 und Kl.9/10','Schulsanitäter Kl.7/8 und Kl.9/10','AG – Kreatives Nähen','AG Kanu','AG Tischtennis','Foerderunterricht Deutsch Kl. 7/8','Foerderunterricht Deutsch Kl 9/10','Gitarrenunterricht','Foerderunterricht Latein Klasse 7/8','Foerderunterricht Latein 9','Stark im Schulalltag','Volleyball Klasse 7/8','Volleyball Klasse 9/10','Volleyball Klasse 11/12'] # echte AGs
    false = ['exp1',"exp2"]

    blue_points , red_points = 0,0

    #print(true[random.randrange(0,(true.__len__()))])

    for i in range(1,11):
        if random.randint(1,2) == 1:
            blue_points,red_points = game(true[random.randint(0,(true.__len__()))], "True",blue_points,red_points,i)
        else:
            blue_points,red_points = game(false[random.randint(0,(false.__len__()))],"False",blue_points,red_points,i)


    if blue_points == red_points:
        return "None"
    elif blue_points > red_points:
        return "blue"
    else:
        return "red"

WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
true_or_false(WIN,WIDHT,HEIGHT,60)