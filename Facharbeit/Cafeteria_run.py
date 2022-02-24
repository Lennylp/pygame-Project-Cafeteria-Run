import pygame
import os
import random
from pygame.constants import K_a, K_d, K_h, K_j, K_k, K_o, K_p , K_r, K_s, K_t , K_u, K_w

def main(WIN,WIDHT,HEIGHT,FPS):

    def board(pos_red,pos_blue,time_wait,WIN,WIDHT,HEIGHT,FPS):
        
        WHITE = (255,255,255)

        class pos:
            def __init__(self,pos):
                if pos == 1:
                    self.x = 278
                    self.y = 665
                if pos == 2:
                    self.x = 323
                    self.y = 655
                if pos == 3:
                    self.x = 373
                    self.y = 697
                if pos == 4:
                    self.x = 415
                    self.y = 669
                if pos == 5:
                    self.x = 441
                    self.y = 718
                if pos == 6:
                    self.x = 485
                    self.y = 686
                if pos == 7:
                    self.x = 504
                    self.y = 722
                if pos == 8:
                    self.x = 540
                    self.y = 705
                if pos == 9:
                    self.x = 577
                    self.y = 732
                if pos == 10:
                    self.x = 585
                    self.y = 691
                if pos == 11:
                    self.x = 582
                    self.y = 641
                if pos == 12:
                    self.x = 547
                    self.y = 641
                if pos == 13:
                    self.x = 512
                    self.y = 623
                if pos == 14:
                    self.x = 474
                    self.y = 636
                if pos == 15:
                    self.x = 449
                    self.y = 613
                if pos == 16:
                    self.x = 406
                    self.y = 621
                if pos == 17:
                    self.x = 371
                    self.y = 597
                if pos == 18:
                    self.x = 324
                    self.y = 592
                if pos == 19:
                    self.x = 284
                    self.y = 572
                if pos == 20:
                    self.x = 243
                    self.y = 538
                if pos == 21:
                    self.x = 224
                    self.y = 496
                if pos == 22:
                    self.x = 241
                    self.y = 450
                if pos == 23:
                    self.x = 257
                    self.y = 403
                if pos == 24:
                    self.x = 271
                    self.y = 347
                if pos == 25:
                    self.x = 294
                    self.y = 299
                if pos == 26:
                    self.x = 314
                    self.y = 261
                if pos == 27:
                    self.x = 324
                    self.y = 222
                if pos == 28:
                    self.x = 335
                    self.y = 159
                if pos == 29:
                    self.x = 379
                    self.y = 144
                if pos == 30:
                    self.x = 386
                    self.y = 93

        if pos_blue != pos_red:
            blue = pos(pos_blue)
            red = pos(pos_red)
        else:
            blue_red = pos(pos_blue)

    

        IMAGE_BLUE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Board','Blue_Figur.png')),(18,18))
        IMAGE_RED = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Board','Red_Figur.png')),(18,18))
        IMAGE_BLUE_RED = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Board", "blue_red_board.png")),(18,18))
        IMAGE_SCHOOL = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Board", "school2_board.png")),(WIDHT,HEIGHT))
        WIN.blit(IMAGE_SCHOOL,(0,0))
        if pos_blue != pos_red:
            WIN.blit(IMAGE_BLUE,(blue.x,blue.y))
            WIN.blit(IMAGE_RED,(red.x,red.y))
        else:
            WIN.blit(IMAGE_BLUE_RED,(blue_red.x,blue_red.y))

        pygame.display.update()
        clock = pygame.time.Clock()
        timer = time_wait
        dt = 0
        while timer > 0:
            timer -=dt
            dt = clock.tick(FPS) / 1000
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

    def roll_dice(max_number,WIN,WIDHT,HEIGHT):
        random_number = random.randint(1,max_number)
        if random_number == 1:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_1.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 2:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_2.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 3:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_3.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 3:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_3.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 4:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_4.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 5:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_5.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        elif random_number == 6:
            DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_6.png')), (int(WIDHT*0.625),int(WIDHT*0.625)))
        WIN.blit(DICE_IMAGE,(WIDHT/2 - 250,HEIGHT/2 - 250))
        pygame.display.update()
        pygame.time.delay(3000)
        return random_number
    
    def titlesrceen(WIN,WIDHT,HEIGHT,FPS):
        pygame.init()
        
        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)
        DARKER_GRAY = (150,150,150)
        BLUE = (111,117,204)
        RED = (204,111,111)

        def blit_text_to_screen_center(center_x,center_y,text,size,color):
            font = pygame.font.Font(None,size)
            text = font.render(text,True,color)
            text_rect = text.get_rect(center = (center_x, center_y))
            WIN.blit(text,text_rect)

        def blit_text_to_screen(x,y,text,size,color):
            font = pygame.font.Font(None,size)
            text = font.render(text,True,color)
            WIN.blit(text,(x,y))

        def main_screen(WIN,WIDHT,HEIGHT,FPS):
            selected = "None"
            selector = 2
            clock = pygame.time.Clock()
            while selected == "None":
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[K_a] or key[K_h]:
                            if selector == 1:
                                selector = 5
                            else:
                                selector -= 1
                        if key[K_d] or key[K_k]:
                            if selector == 5:
                                selector = 1
                            else:
                                selector += 1
                        if key[K_w] or key[K_u]:
                            if selector == 1:
                                selected = "Settings"
                            if selector == 2:
                                selected = "Start"
                            if selector == 3:
                                selected = "Controls"
                            if selector == 4:
                                selected = "About"
                            if selector == 5:
                                selected = "Quit"
                                pygame.quit()
                
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Cafeteria Run",int(WIDHT * 0.1875),DARK_GRAY)
                if selector == 1:
                    blit_text_to_screen_center(WIDHT/5,HEIGHT/8*5,"Settings",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen_center(WIDHT/5,HEIGHT/8*5,"Settings",int(WIDHT * 0.075),DARK_GRAY)
                if selector == 2:
                    blit_text_to_screen_center(WIDHT/2,HEIGHT/8*5,"Start Game",int(WIDHT * 0.08),DARKER_GRAY)
                else:
                    blit_text_to_screen_center(WIDHT/2,HEIGHT/8*5,"Start Game",int(WIDHT * 0.08),DARK_GRAY)
                if selector == 3:
                    blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*4,"Controls",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*4,"Controls",int(WIDHT * 0.075),DARK_GRAY)
                
                if selector == 4:
                    blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*5,"About",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*5,"About",int(WIDHT * 0.075),DARK_GRAY)
                if selector == 5:
                    blit_text_to_screen_center((WIDHT/10)*9,HEIGHT/8*7,"Quit",int(WIDHT * 0.07),DARKER_GRAY)
                else:
                    blit_text_to_screen_center((WIDHT/10)*9,HEIGHT/8*7,"Quit",int(WIDHT * 0.07),DARK_GRAY)
                blit_text_to_screen(WIDHT/11 * 8,HEIGHT/8*7.5,"Lenny Priewe",int(WIDHT * 0.05),DARK_GRAY)
                
                blit_text_to_screen(30,HEIGHT*14/15,"w(u) -> select, a+d(h+k) to move",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                            
            return selected    


        def settings(WIN,WIDHT,HEIGHT,FPS):
            setting_selektor = 3
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Settings",int(WIDHT * 0.1875),DARK_GRAY)
                blit_text_to_screen(WIDHT/9,HEIGHT/4,"Presets:",int(WIDHT * 0.1),DARK_GRAY)
                if setting_selektor == 1:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*3,"Potato",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*3,"Potato",int(WIDHT * 0.075),DARK_GRAY)
                if setting_selektor == 2:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*4,"Arcade",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*4,"Arcade",int(WIDHT * 0.075),DARK_GRAY)
                if setting_selektor == 3:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*5,"Casual",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*5,"Casual",int(WIDHT * 0.075),DARK_GRAY)
                if setting_selektor == 4:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*6,"Epic Gamer",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*6,"Epic Gamer",int(WIDHT * 0.075),DARK_GRAY)
                if setting_selektor == 5:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*7,"Custom",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9,HEIGHT/8*7,"Custom",int(WIDHT * 0.075),DARK_GRAY)
                if setting_selektor == 6:
                    blit_text_to_screen(WIDHT/9*7,HEIGHT/8*7,"Back",int(WIDHT * 0.075),DARKER_GRAY)
                else:
                    blit_text_to_screen(WIDHT/9*7,HEIGHT/8*7,"Back",int(WIDHT * 0.075),DARK_GRAY)
                blit_text_to_screen(30,HEIGHT*14/15,"a+d(h+k) -> select, w+s(u+j) to move",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()

                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] or keys[K_u]:
                            if setting_selektor == 1:
                                setting_selektor = 6
                            else: 
                                setting_selektor -= 1
                        if keys[K_s] or keys[K_j]:
                            if setting_selektor == 6:
                                setting_selektor = 1
                            else: 
                                setting_selektor += 1
                        if keys[K_d] or keys[K_k] or keys[K_a] or keys[K_h]:
                            if setting_selektor == 1: #potato
                                WIDHT,HEIGHT = 50,50
                                FPS = 10
                                WIN = pygame.display.set_mode((WIDHT,HEIGHT))
                            if setting_selektor == 2: #arcade
                                WIDHT, HEIGHT = 200,200
                                FPS = 25
                                WIN = pygame.display.set_mode((WIDHT,HEIGHT))
                            if setting_selektor == 3: #casual
                                WIDHT, HEIGHT = 800,800
                                FPS = 60
                                WIN = pygame.display.set_mode((WIDHT,HEIGHT))
                            if setting_selektor == 4: #epic gamer
                                WIDHT, HEIGHT = 1200,1200
                                FPS = 250
                                WIN = pygame.display.set_mode((WIDHT,HEIGHT))
                            if setting_selektor == 5: #change the values below to get your custom settings
                                WIDHT, HEIGHT = 200,200 #widht and height of the screen
                                FPS = 25 # frames per second
                                WIN = pygame.display.set_mode((WIDHT,HEIGHT))
                            if setting_selektor == 6: #quit
                                back = True
            
            return WIN, WIDHT, HEIGHT, FPS
            
        def about(WIN,WIDHT,HEIGHT,FPS):
            back = False
            clock = pygame.time.Clock()
            while back == False:

                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"About",int(WIDHT * 0.1875),DARK_GRAY)
                blit_text_to_screen(WIDHT/20,HEIGHT/8*2,"Cafeteria Run is a Game that was",int(WIDHT * 0.08),DARK_GRAY)
                blit_text_to_screen(WIDHT/20,HEIGHT/8*3,"developed for my school project.",int(WIDHT * 0.08),DARK_GRAY)
                blit_text_to_screen(WIDHT/20,HEIGHT/8*4,"All sprites are painted by myself.",int(WIDHT * 0.08),DARK_GRAY)
                blit_text_to_screen(WIDHT/20,HEIGHT/8*5,"The entire game was created in",int(WIDHT * 0.08),DARK_GRAY)
                blit_text_to_screen(WIDHT/20,HEIGHT/8*6,"Python using free programs.",int(WIDHT * 0.08),DARK_GRAY)
                blit_text_to_screen(WIDHT/9*6,HEIGHT/8*7,"UP -> Main Menu",int(WIDHT * 0.05),DARK_GRAY)


                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] or keys[K_u]:
                            back = True

        def controls(WIN,WIDHT,HEIGHT,FPS):
            back = False
            clock = pygame.time.Clock()
            while back == False:

                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls",int(WIDHT * 0.1875),DARK_GRAY)
                
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*2/8,"Blue:",int(WIDHT * 0.1),BLUE)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*3/9,"w",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*4/9,"s",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*5/9,"a",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*6/9,"d",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*7/9,"r",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*2/5,HEIGHT*8/9,"t",int(WIDHT * 0.1),DARK_GRAY)
                
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*2/8,"Red:",int(WIDHT * 0.1),RED)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"u",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"j",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*5/9,"h",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*6/9,"k",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*7/9,"o",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*8/9,"p",int(WIDHT * 0.1),DARK_GRAY)
                
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"UP:",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"DOWN:",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*5/9.4,"LEFT:",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*6/9.4,"RIGHT:",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*7/9.4,"L-BUTTON:",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*8/9.4,"R-Button:",int(WIDHT * 0.09),DARK_GRAY)
                
                blit_text_to_screen(WIDHT/9*6,HEIGHT*14/15,"UP -> Main Menu",int(WIDHT * 0.05),DARK_GRAY)


                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] or keys[K_u]:
                            back = True


        start_game = False  
        
        
        while start_game == False:
            return_ = main_screen(WIN,WIDHT,HEIGHT,FPS)
            if return_ == "About":
                about(WIN,WIDHT,HEIGHT,FPS)
            elif return_ == "Settings":
                WIN , WIDHT , HEIGHT , FPS = settings(WIN, WIDHT, HEIGHT, FPS) 
            elif return_ == "Controls":
                controls(WIN,WIDHT,HEIGHT,FPS)
            else: 
                start_game = True
                return WIDHT, HEIGHT, FPS

    def explain(WIN,WIDHT,HEIGHT,FPS,game):
        pygame.init()
        def blit_text_to_screen_center(center_x,center_y,text,size,color):
            font = pygame.font.Font(None,size)
            text = font.render(text,True,color)
            text_rect = text.get_rect(center = (center_x, center_y))
            WIN.blit(text,text_rect)

        def blit_text_to_screen(x,y,text,size,color):
            font = pygame.font.Font(None,size)
            text = font.render(text,True,color)
            WIN.blit(text,(x,y))

        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)    
        DARKER_GRAY = (150,150,150)

        if game == "dogeball":
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls Dogeball",int(WIDHT * 0.15),DARKER_GRAY)

                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"UP",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"DOWN",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*5/9,"LEFT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*6/9,"RIGHT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*7/9,"L-BUTTON",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*8/9,"R-BUTTON",int(WIDHT * 0.1),DARK_GRAY)

                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"Move up",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"Move down",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*5/9.4,"Move left",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*6/9.4,"move right",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*7/9.4,"change Player",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*8/9.4,"throw ball",int(WIDHT * 0.09),DARK_GRAY)

                blit_text_to_screen(WIDHT/9*4,HEIGHT*14/15,"Both player: UP -> Contiue",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] and keys[K_u]:
                            back = True

        if game == "catch":
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls Catch",int(WIDHT * 0.15),DARKER_GRAY)

                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"UP",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"DOWN",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*5/9,"LEFT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*6/9,"RIGHT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*7/9,"L-BUTTON",int(WIDHT * 0.1),DARK_GRAY)

                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"Move forward",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"Move bachwards",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*5/9.4,"Turn left",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*6/9.4,"Turn right",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*7/9.4,"jump forward",int(WIDHT * 0.09),DARK_GRAY)

                blit_text_to_screen(WIDHT/9*4,HEIGHT*14/15,"Both player: UP -> Contiue",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] and keys[K_u]:
                            back = True

        if game == "trueorfalse":
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls True or False",int(WIDHT * 0.1),DARKER_GRAY)

                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"UP",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"DOWN",int(WIDHT * 0.1),DARK_GRAY)

                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"True",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"False",int(WIDHT * 0.09),DARK_GRAY)

                blit_text_to_screen(WIDHT/9*4,HEIGHT*14/15,"Both player: UP -> Contiue",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] and keys[K_u]:
                            back = True

        if game == "hangman":
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls Hangman",int(WIDHT * 0.14),DARKER_GRAY)

                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"UP",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"DOWN",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*5/9,"LEFT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*6/9,"RIGHT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*7/9,"L-BUTTON",int(WIDHT * 0.1),DARK_GRAY)

                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"Move up",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"Move down",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*5/9.4,"Move left",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*6/9.4,"move right",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*7/9.4,"select letter",int(WIDHT * 0.09),DARK_GRAY)

                blit_text_to_screen(WIDHT/9*4,HEIGHT*14/15,"Both player: UP -> Contiue",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] and keys[K_u]:
                            back = True
        
        if game == "tictactoe":
            back = False
            clock = pygame.time.Clock()
            while back == False:
                WIN.fill(LIGHT_GRAY)
                blit_text_to_screen_center(WIDHT/2,HEIGHT/8,"Controlls Tic Tac Toe",int(WIDHT * 0.13),DARKER_GRAY)
                
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*3/9,"UP",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*4/9,"DOWN",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*5/9,"LEFT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*6/9,"RIGHT",int(WIDHT * 0.1),DARK_GRAY)
                blit_text_to_screen_center(WIDHT*4/5,HEIGHT*7/9,"L-BUTTON",int(WIDHT * 0.1),DARK_GRAY)
                
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*3/9.4,"Move up",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*4/9.4,"Move down",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*5/9.4,"Move left",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*6/9.4,"move right",int(WIDHT * 0.09),DARK_GRAY)
                blit_text_to_screen(WIDHT*0.25/10,HEIGHT*7/9.4,"select letter",int(WIDHT * 0.09),DARK_GRAY)
                
                blit_text_to_screen(WIDHT/9*4,HEIGHT*14/15,"Both player: UP -> Contiue",int(WIDHT * 0.05),DARK_GRAY)
                pygame.display.update()
                dt = clock.tick(FPS) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w] and keys[K_u]:
                            back = True

    def dogeball(WIN,WIDHT,HEIGHT):

        Two_Player = True
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
                """
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
                """        
            
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


        def blit_text_to_screen_center(center_x,center_y,text,size,color):
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
                    blit_text_to_screen_center(WIDHT*3/4,(HEIGHT*3)/4,"True", WIDHT * 0.1,RED)
                    red_points += 1
                else:
                    blit_text_to_screen_center(WIDHT*3/4,(HEIGHT*3)/4,"False", WIDHT * 0.1,RED)
                    blue_points += 1
            else:
                if blue_selected == true_or_false:
                    blit_text_to_screen_center(WIDHT/4,(HEIGHT*3)/4,"True", WIDHT * 0.1,BLUE)
                    blue_points += 1
                else:
                    blit_text_to_screen_center(WIDHT/4,(HEIGHT*3)/4,"False", WIDHT * 0.1,BLUE)
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

                    


        true = ['true'] # place here some real things about your school
        false = 'false'] # place here some wrong things about your school

        blue_points , red_points = 0,0

        #print(true[random.randrange(0,(true.__len__()))])

        for i in range(1,11):
            if random.randint(1,2) == 1:
                blue_points,red_points = game(true[random.randint(0,(true.__len__() - 1))], "True",blue_points,red_points,i)
            else:
                blue_points,red_points = game(false[random.randint(0,(false.__len__() - 1))],"False",blue_points,red_points,i)


        if blue_points == red_points:
            return "None"
        elif blue_points > red_points:
            return "blue"
        else:
            return "red"

    def hangman(WIN,WIDHT,HEIGHT,possible_words):

        pygame.init()


        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)
        DARKER_GRAY = (150,150,150)
        BLUE = (111,117,204)
        RED = (204,111,111)
        GREEN = (111,204,111)
        DARK_RED = (225,100,100)
        
        def return_str(word,guesses):
            sum = ""
            for l in word:
                if l.lower() in guesses:
                    sum += f"{l} "
                else:
                    sum += "_ "
            
            return sum

        def blit_text_to_screen(x,y,text,size,color):
            font = pygame.font.Font(None,int(size))
            text = font.render(text,True,color)
            WIN.blit(text,(x,y))


        def rahmen(color):
            thick = 45
            pygame.draw.line(WIN,color,(0,0),(WIDHT,0), thick)
            pygame.draw.line(WIN,color,(WIDHT,0),(WIDHT, HEIGHT), thick)
            pygame.draw.line(WIN,color,(0,HEIGHT),(WIDHT, HEIGHT), thick)
            pygame.draw.line(WIN,color,(0,HEIGHT),(0,0), thick)
        
        def blit_text_to_screen_center(center_x,center_y,text,size,color): #from titlescreen
            font = pygame.font.Font(None,int(size))
            text = font.render(text,True,color)
            text_rect = text.get_rect(center = (center_x, center_y))
            WIN.blit(text,text_rect)

        def blit_text_to_screen_center_for_show(center_x,center_y,text,color): #from true_or_false
            if len(text) > 7:
                lenght = (1 / (len(text) * 0.55)) * WIDHT
                font = pygame.font.Font(None,int(lenght))
                text = font.render(text,True,color)
                text_rect = text.get_rect(center = (center_x, center_y))
                WIN.blit(text,text_rect)
            else:
                blit_text_to_screen_center(center_x,center_y,text,WIDHT * 0.1,color)

        def keybord(WIDHT,HEIGHT,player,guesses,tries):

            class Selector():
                def __init__(self):
                    self.x = 0
                    self.y = 0 

                def move(self,keys,player):
                    if player == "blue":
                        if keys[K_w]:
                            self.y -= 1
                            if self.y < 0:
                                self.y = 2
                        if keys[K_s]:
                            self.y += 1
                            if self.y > 2:
                                self.y = 0
                        if keys[K_a]:
                            self.x -= 1
                            if self.x < 0:
                                self.x = 9
                        if keys[K_d]:
                            self.x += 1
                            if self.x > 9:
                                self.x = 0
                    else:
                        if keys[K_u]:
                            self.y -= 1
                            if self.y < 0:
                                self.y = 2
                        if keys[K_j]:
                            self.y += 1
                            if self.y > 2:
                                self.y = 0
                        if keys[K_h]:
                            self.x -= 1
                            if self.x < 0:
                                self.x = 9
                        if keys[K_k]:
                            self.x += 1
                            if self.x > 9:
                                self.x = 0

            def draw_key(x,y,widht,height,letter,player):
                if player == "blue":
                    color = BLUE
                elif player == "None":
                    color = DARKER_GRAY
                else:    
                    color = RED
                key = pygame.Rect(x,y,widht,height)
                pygame.draw.rect(WIN,color,key)
                blit_text_to_screen_center(key.centerx,key.centery,letter,int(widht * 0.9),DARK_GRAY)        
                    
            def draw_keybord(possible_keys,selector,tries):
                for i in range(0,3):
                    for j in range(0,10):
                        if selector.x == j and selector.y == i:
                            draw_key(50 + 70 * j,HEIGHT * 0.635 + 70 * i, 60,60,possible_keys[i][j],player)
                        else:
                            draw_key(50 + 70 * j,HEIGHT * 0.635 + 70 * i, 60,60,possible_keys[i][j],"None")
                        
                blit_text_to_screen(5, HEIGHT - HEIGHT * 0.05 - 5, f"Amount of tries: {tries}" ,HEIGHT * 0.05, DARK_GRAY)


            selector = Selector()

            possible_keys = [["q","w","e","r","t","z","u","i","o","p"], #max = 3,10
                              ["a","s","d","f","g","h","j","k","l","ß"],
                              ["y","x","c","v","b","n","m","ä","ö","ü"]]
            
            #for i in range(0,3):
            #    for j in range(0,10):

            run = True
            while run == True:
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        selector.move(keys, player)

                        if player == "blue":
                            if keys[K_r]:
                                return str(possible_keys[selector.y][selector.x])
                                run = False
                        else:
                            if keys[K_o]:
                                return str(possible_keys[selector.y][selector.x])
                                run = False

                    if event.type == pygame.QUIT:
                        pygame.quit()
                
                WIN.fill(LIGHT_GRAY)
                if player == "blue":
                    c = BLUE
                else:
                    c = RED
                rahmen(c)
                blit_text_to_screen_center_for_show(WIDHT/2,HEIGHT*2/5,return_str(word,guesses),DARK_GRAY)
                draw_keybord(possible_keys,selector,tries)

                pygame.display.update()


        def game(word):

            tries = 6
            guesses = []
            current_player = ""

            if random.randint(1,2) == 1:
                current_player = "blue" 
            else: 
                current_player = "red"

            done = False

            while done == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()


                current_guess = keybord(WIDHT, HEIGHT, current_player, guesses,tries)

                if current_guess in word.lower():
                    guesses.append(current_guess)
                    blit_text_to_screen_center(WIDHT/2,HEIGHT/5,"Right guess!",WIDHT* 0.1,GREEN)
                    pygame.display.update()
                    pygame.time.delay(1000)

                    finished = True
                    for letter in word:
                        if letter.lower() not in guesses:
                            finished = False
                    
                    if finished == True:
                        return current_player

                else:
                    tries -= 1
                    if tries <= 0:
                        if current_player == "blue":
                            return "red"
                        else:
                            
                            return "blue"
                    
                    blit_text_to_screen_center(WIDHT/2,HEIGHT/5,f"{current_guess} isn't a part!",WIDHT* 0.1,DARK_RED)
                    pygame.display.update()
                    pygame.time.delay(1000)
                
                print(current_player)
                if current_player == "blue":
                    current_player = "red"
                else:
                    current_player = "blue"



            

        if possible_words == None:
            possible_words =["Hi","Ho","Ha"]
        word = possible_words[random.randrange(0,possible_words.__len__())]

        return game(word)

    def catch(WIN,WIDHT,HEIGHT,FPS):

        class Player():
            def __init__(self,color,x,y,rotation):
                self.color = color
                self.y = y
                self.x = x
                self.z = 1
                self.rotation = rotation
            
            def move(self,command):
                if command == "UP" or command == "DOWN" or command == "LBUTTON":
                    a = 0
                    if command == "UP":
                        a = 1
                    elif command == "DOWN":
                        a = -1
                    else: 
                        a = 2

                    if self.rotation == 0:
                        self.y -= a
                    elif self.rotation == 90:
                        self.x += a
                    elif self.rotation == 180:
                        self.y += a
                    elif self.rotation == 270:
                        self.x -= a
                if command == "LEFT":
                    self.rotation -= 90
                    if self.rotation == -90:
                        self.rotation = 270
                if command == "RIGHT":
                    self.rotation += 90
                    if self.rotation == 360:
                        self.rotation = 0
            
            def draw(self):
                if self.color == "blue":
                    if self.rotation == 0:
                        blit_image_by_xyz(BLUE_UP_IMG,self.x,self.y,1,size)
                    if self.rotation == 90:
                        blit_image_by_xyz(BLUE_LEFT_IMG,self.x,self.y,1,size)
                    if self.rotation == 180:
                        blit_image_by_xyz(BLUE_DOWN_IMG,self.x,self.y,1,size)
                    if self.rotation == 270:
                        blit_image_by_xyz(BLUE_RIGHT_IMG,self.x,self.y,1,size)
                else:
                    if self.rotation == 0:
                        blit_image_by_xyz(RED_UP_IMG,self.x,self.y,1,size)
                    if self.rotation == 90:
                        blit_image_by_xyz(RED_LEFT_IMG,self.x,self.y,1,size)
                    if self.rotation == 180:
                        blit_image_by_xyz(RED_DOWN_IMG,self.x,self.y,1,size)
                    if self.rotation == 270:
                        blit_image_by_xyz(RED_RIGHT_IMG,self.x,self.y,1,size)

        size = int(WIDHT * 0.00625)
        x_offset = 0.44
        y_offset = 0.225

        BLUE_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","blue_UP.png")), (size * 18,size * 18))
        BLUE_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","blue_LEFT.png")), (size * 18,size * 18))
        BLUE_DOWN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","blue_DOWN.png")), (size * 18,size * 18))
        BLUE_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","blue_RIGHT.png")), (size * 18,size * 18))
        RED_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","red_UP.png")), (size * 18,size * 18))
        RED_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","red_LEFT.png")), (size * 18,size * 18))
        RED_DOWN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","red_DOWN.png")), (size * 18,size * 18))
        RED_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Catch","red_RIGHT.png")), (size * 18,size * 18))
        CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
        CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
        CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
        CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
        CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
        CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
        CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
        CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
        CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
        BLUE_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_blue.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
        RED_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_red.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
        

        FLOOR_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Catch','school_floor.png')), (18*size,18*size))


        
        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)
        DARKER_GRAY = (150,150,150)
        BLUE = (111,117,204)
        RED = (204,111,111)
            

        def blit_image_by_xyz(image,x,y,z,size):
            WIN.blit(image,(int(WIDHT/2 - ((size*18)/2) + (x* (size*18) * x_offset )- (y * (size*18) * x_offset )),int(HEIGHT/4 + (x * (size * 18) *y_offset) + (y * (size * 18) * y_offset) - (z/2) * (size * 18))))

        def generate_map(size):
            map_data = []
            x_line = []
            for i in range(0,size):
                x_line.append(0)
            map_data.append(x_line)
            x_line = []
            x_line.append(0)
            for i in range(1,size-1):
                x_line.append(1)
            x_line.append(0)
            map_data.append(x_line)
            x_line = []
            for i in range(0,size-4):
                x_line.append(0)
                x_line.append(1)
                for j in range(2,size-2):
                    if random.randint(1,2) == 1:
                        x_line.append(1)
                    else:
                        x_line.append(0)
                x_line.append(1)
                x_line.append(0)
                map_data.append(x_line)
                x_line = []
            x_line.append(0)
            for i in range(1,size-1):
                x_line.append(1)
            x_line.append(0)
            map_data.append(x_line)
            x_line = []
            for i in range(0,size):
                x_line.append(0)
            map_data.append(x_line)
            x_line = []
            return map_data
                

        def get_number_xy0(map_data,x,y):
            return map_data[y][x]
        
        def rahmen(catcher):
            if catcher == "blue":
                color = BLUE
            else:
                color = RED
            thick = 45
            pygame.draw.line(WIN,color,(0,0),(WIDHT,0), thick)
            pygame.draw.line(WIN,color,(WIDHT,0),(WIDHT, HEIGHT), thick)
            pygame.draw.line(WIN,color,(0,HEIGHT),(WIDHT, HEIGHT), thick)
            pygame.draw.line(WIN,color,(0,HEIGHT),(0,0), thick)

        def game(catcher,timer,points_blue,points_red):
            max_time = 60
            dt = 0

            clock = pygame.time.Clock()

            blue = Player("blue",1,10,0)
            red = Player("red",10,1,180)

            map_data = generate_map(12)
            while True:
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_w]:
                            blue.move("UP")
                        if keys[K_s]:
                            blue.move("DOWN")
                        if keys[K_a]:
                            blue.move("LEFT")
                        if keys[K_r]:
                            blue.move("LBUTTON")
                        if keys[K_d]:
                            blue.move("RIGHT")
                        if keys[K_u]:
                            red.move("UP")
                        if keys[K_j]:
                            red.move("DOWN")
                        if keys[K_h]:
                            red.move("LEFT")
                        if keys[K_k]:
                            red.move("RIGHT")
                        if keys[K_o]:
                            red.move("LBUTTON")


                if get_number_xy0(map_data, blue.x,blue.y) == 0 or blue.y < 0 or blue.x < 0:
                    #blue fallen down
                    return (timer,"blue_fall")     
                if get_number_xy0(map_data, red.x,red.y) == 0 or red.y < 0 or red.x < 0:
                    #red fallen down
                    return (timer,"red_fall")   
                if blue.x == red.x and blue.y == red.y:
                    return (timer,"catch")

                #draw
                WIN.fill(LIGHT_GRAY)

                rahmen(catcher)

                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        if tile == 1:
                            blit_image_by_xyz(FLOOR_IMG,x,y,0,size)   

                if blue.y < red.y:
                    blue.draw()  
                    red.draw()  
                elif red.y< blue.y:
                    red.draw()  
                    blue.draw()  
                else:
                    if blue.x < red.x:
                        blue.draw()  
                        red.draw()  
                    else:
                        red.draw() 
                        blue.draw()  

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

                y = 25
                x = 25
                for i in range(0,points_blue):
                    WIN.blit(BLUE_POINTS_IMAGE,(x,y))
                    x += WIDHT*0.0657 + 5

                x = WIDHT - 25 - WIDHT*0.0657
                for i in range(0,points_red):
                    WIN.blit(RED_POINTS_IMAGE,(x,y))
                    x -= WIDHT*0.0657 + 5

                timer -= dt
                if timer <= 0:
                    run = False
                    return (0,"Time out")
                dt = clock.tick(FPS) / 1000    
                
                pygame.display.update()

        if random.randint(1,2) == 1:
            catcher = "blue"
        else:
            catcher = "red"

        blue_points = 0
        red_points = 0

        timer = 60
        while True:
            while timer > 0:
                timer, return_value = game(catcher,timer,blue_points,red_points)
                if return_value == "catch":
                    if catcher == "blue":
                        blue_points += 1
                    else:
                        red_points += 1
                elif return_value == "blue_fall":
                    red_points += 1
                elif return_value == "red_fall":
                    blue_points += 1

                if catcher == "red":
                    catcher = "blue"
                else:
                    catcher = "red"

            if blue_points > red_points:
                return "blue"
            elif red_points > blue_points:
                return "red"
            else:
                "None"

    def tictactoe(WIN,WIDHT,HEIGHT,FPS):

        EMPTY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_tictactoe','empty.png')), (int(WIDHT/3),int(WIDHT/3)))
        RED_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_tictactoe','red.png')), (int(WIDHT/3),int(WIDHT/3)))
        BLUE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_tictactoe','blue.png')), (int(WIDHT/3),int(WIDHT/3)))
        BLUE_SELECTOR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_tictactoe','blue_selector.png')), (int(WIDHT/3),int(WIDHT/3)))
        RED_SELECTOR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_tictactoe','red_selector.png')), (int(WIDHT/3),int(WIDHT/3)))
        CLOCK_ZERO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_0.png')), (90,90))
        CLOCK_ONE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_1.png')), (90,90))
        CLOCK_TWO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_2.png')), (90,90))
        CLOCK_THREE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_3.png')), (90,90))
        CLOCK_FOUR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_4.png')), (90,90))
        CLOCK_FIVE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_5.png')), (90,90))
        CLOCK_SIX_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_6.png')), (90,90))
        CLOCK_SEVEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_7.png')), (90,90))
        CLOCK_EIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Global', 'clock_8.png')), (90,90))
        BLUE_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_blue.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
        RED_POINTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_True_or_False','points_red.png')), (int(WIDHT*0.0657),int(WIDHT*0.0657)))
    

        
        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)
        DARKER_GRAY = (150,150,150)
        BLUE = (111,117,204)
        RED = (204,111,111)



        class Selector():
            def __init__(self,color):
                self.x = 1
                self.y = 1 
                self.color = color

            def move(self,keys,player):
                if player == "blue":
                    if keys[K_w]:
                        self.y -= 1
                        if self.y < 0:
                            self.y = 2
                    if keys[K_s]:
                        self.y += 1
                        if self.y > 2:
                            self.y = 0
                    if keys[K_a]:
                        self.x -= 1
                        if self.x < 0:
                            self.x = 2
                    if keys[K_d]:
                        self.x += 1
                        if self.x > 2:
                            self.x = 0
                else:
                    if keys[K_u]:
                        self.y -= 1
                        if self.y < 0:
                            self.y = 2
                    if keys[K_j]:
                        self.y += 1
                        if self.y > 2:
                            self.y = 0
                    if keys[K_h]:
                        self.x -= 1
                        if self.x < 0:
                            self.x = 2
                    if keys[K_k]:
                        self.x += 1
                        if self.x > 2:
                            self.x = 0

        def select(color,keys,board,player):
            if color == "blue":
                if keys[K_r] and board[player.y][player.x] == "empty":
                    board[player.y][player.x] = "blue"
                    return "next"
            if color == "red":
                if keys[K_o] and board[player.y][player.x] == "empty":
                    board[player.y][player.x] = "red"
                    return "next"
            
                
            
        def rahmen(color):
                thick = 45
                pygame.draw.line(WIN,color,(0,0),(WIDHT,0), thick)
                pygame.draw.line(WIN,color,(WIDHT,0),(WIDHT, HEIGHT), thick)
                pygame.draw.line(WIN,color,(0,HEIGHT),(WIDHT, HEIGHT), thick)
                pygame.draw.line(WIN,color,(0,HEIGHT),(0,0), thick)

        
        def draw_Selector(player):
            if player.color == "blue":
                image = BLUE_SELECTOR_IMAGE
            else:
                image = RED_SELECTOR_IMAGE
            WIN.blit(image,(player.x * int(WIDHT/3),player.y * int(WIDHT/3)))

        def draw_board(board):
            for y in range(0,3):
                for x in range(0,3):
                    if board[y][x] == "empty":
                        image = EMPTY_IMAGE
                    elif board[y][x] == "blue":
                        image = BLUE_IMAGE
                    else:
                        image = RED_IMAGE
                    WIN.blit(image,(x * int(WIDHT/3),y * int(WIDHT/3)))

        def returnx_or_o(player,field):
            if player.color == "blue":
                if field == "blue":
                    return "x"
                else:
                    return "o"
            else:
                if field == "red":
                    return "x"
                else:
                    return "o"
        
        def wining(board,player):
            b = [["o","o","o"],["o","o","o"],["o","o","o"]]
            for y in range(0,3):
                for x in range(0,3):
                    b[y][x] = returnx_or_o(player, board[y][x])
            
            if b[0][0] == "x" and b[0][1] == "x" and b[0][2] == "x" or b[1][0] == "x" and b[1][1] == "x" and b[1][2] == "x" or b[2][0] == "x" and b[2][1] == "x" and b[2][2] == "x" or b[0][0] == "x" and b[0][1] == "x" and b[0][2] == "x" or b[1][0] == "x" and b[1][1] == "x" and b[1][2] == "x" or b[2][0] == "x" and b[2][1] == "x" and b[2][2] == "x" or b[0][0] == "x" and b[1][1] == "x" and b[2][2] == "x" or b[0][2] == "x" and b[1][1] == "x" and b[2][0] == "x":
                return "win"
            else:
                return "nothing"
            

        def main(points_blue,points_red):
            current_player = "blue" if random.randrange(0,2) == 0 else "red"
            print(current_player)
            

            board = [["empty","empty","empty"],["empty","empty","empty"],["empty","empty","empty"]]

            blue_player = Selector("blue")
            red_player = Selector("red")
            
            clock = pygame.time.Clock()

            dt = 0

            run = True

            timer = 10

            while run == True:

                timer -= dt
                if timer <= 0:
                    run = False
                    if current_player == "red":
                        return "blue"
                    else:
                        return "red"
                dt = clock.tick(FPS) / 1000   
                
                draw_board(board)
                draw_Selector(blue_player if current_player == "blue" else red_player)
                rahmen(BLUE if current_player == "blue" else RED)
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
                y = 25
                x = 25
                for i in range(0,points_blue):
                    WIN.blit(BLUE_POINTS_IMAGE,(x,y))
                    x += WIDHT*0.0657 + 5
                x = WIDHT - 25 - WIDHT*0.0657
                for i in range(0,points_red):
                    WIN.blit(RED_POINTS_IMAGE,(x,y))
                    x -= WIDHT*0.0657 + 5
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if current_player == "blue":
                            blue_player.move(key,current_player)
                        else:
                            red_player.move(key,current_player)
                        if select(current_player, key, board, blue_player if current_player == "blue" else red_player) == "next":
                            print("next")
                            if wining(board, blue_player if current_player == "blue" else red_player) == "win":
                                print("win")
                                run = False
                                return current_player
                            else:
                                if current_player == "red":
                                    current_player = "blue"
                                    timer = 10
                                else:
                                    current_player = "red"
                                    timer = 10

                

        
        blue_points = 0
        red_points = 0
        max_time = 10
        while True:
            for i in range(0,6):
                print("a")
                return_value = main(blue_points,red_points)
                if return_value == "red":
                    red_points += 1
                else:
                    blue_points += 1

            if blue_points > red_points:
                return "blue"
            elif red_points > blue_points:
                return "red"
            else:
                "None"

    def end(winner,WIDHT,HEIGHT,FPS):

        BLUE = (111,117,204)
        RED = (204,111,111)

        def blit_text_to_screen_center(center_x,center_y,text,size,color):
            font = pygame.font.Font(None,size)
            text = font.render(text,True,color)
            text_rect = text.get_rect(center = (center_x, center_y))
            WIN.blit(text,text_rect)

        if winner == "blue":
            blit_text_to_screen_center(WIDHT/2,HEIGHT/4,"BLUE WINS",200,BLUE)
        elif winner == "red":
            blit_text_to_screen_center(WIDHT/2,HEIGHT/4,"RED WINS",200,RED)
        
        pygame.display.update()

        pygame.time.delay(5000)

    while True: #core loop
        WIDHT, HEIGHT, FPS = titlesrceen(WIN, WIDHT, HEIGHT, FPS)
        pos_red = 1
        pos_blue = 1
        while pos_red < 30 and pos_blue < 30: # gameloop
            if pos_red != 30 and pos_blue != 30:
                board(pos_red,pos_blue,3,WIN,WIDHT,HEIGHT,FPS)
                random_game = random.randint(1,5) # minigame selection
                if random_game == 1:
                    explain(WIN, WIDHT, HEIGHT, FPS, "dogeball")
                    winner = dogeball(WIN,WIDHT,HEIGHT)
                if random_game == 2:
                    explain(WIN, WIDHT, HEIGHT, FPS, "trueorfalse")
                    winner = true_or_false(WIN,WIDHT,HEIGHT,FPS)
                if random_game == 3:
                    explain(WIN, WIDHT, HEIGHT, FPS, "hangman")
                    possible_words = ["names"] # place here some names
                    winner = hangman(WIN, WIDHT, HEIGHT, possible_words)
                if random_game == 4:
                    explain(WIN, WIDHT, HEIGHT, FPS, "catch")
                    winner = catch(WIN, WIDHT, HEIGHT, FPS)
                if random_game == 5:
                    explain(WIN, WIDHT, HEIGHT, FPS, "tictactoe")
                    winner = tictactoe(WIN, WIDHT, HEIGHT, FPS)
                board(pos_red,pos_blue,2,WIN,WIDHT,HEIGHT,FPS)
                if winner == "blue": # dice
                    eyes = roll_dice(6,WIN,WIDHT,HEIGHT)
                    if pos_blue + eyes <= 30:
                        for i in range(1,eyes + 1):
                            pos_blue += 1
                            board(pos_red,pos_blue,0.5,WIN,WIDHT,HEIGHT,FPS)
                    board(pos_red,pos_blue,1,WIN,WIDHT,HEIGHT,FPS)
                    eyes = roll_dice(3,WIN,WIDHT,HEIGHT)
                    if pos_red + eyes <= 30:
                        for i in range(1,eyes + 1):
                            pos_red += 1
                            board(pos_red,pos_blue,0.5,WIN,WIDHT,HEIGHT,FPS)
                    board(pos_red,pos_blue,1,WIN,WIDHT,HEIGHT,FPS)
                elif winner == "red":
                    eyes = roll_dice(6,WIN,WIDHT,HEIGHT)
                    if pos_red + eyes <= 30:
                        for i in range(1,eyes + 1):
                            pos_red += 1
                            board(pos_red,pos_blue,0.5,WIN,WIDHT,HEIGHT,FPS)
                    board(pos_red,pos_blue,1,WIN,WIDHT,HEIGHT,FPS)
                    eyes = roll_dice(3,WIN,WIDHT,HEIGHT)
                    if pos_blue + eyes <= 30:
                        for i in range(1,eyes + 1):
                            pos_blue += 1
                            board(pos_red,pos_blue,0.5,WIN,WIDHT,HEIGHT,FPS)
                    board(pos_red,pos_blue,1,WIN,WIDHT,HEIGHT,FPS)

        if pos_red == 30 and pos_blue == 30:
            if winner == "red":
                end("red",WIDHT,HEIGHT,FPS)
            else:
                end("blue",WIDHT,HEIGHT,FPS)
        elif pos_red == 30:
            end("red",WIDHT,HEIGHT,FPS)
        elif pos_blue == 30:
            end("blue",WIDHT,HEIGHT,FPS)


FPS = 60
WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
main(WIN,WIDHT,HEIGHT,FPS)
