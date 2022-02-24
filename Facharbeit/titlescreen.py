import pygame
import pygame.font
from pygame.constants import K_w , K_u , K_a ,  K_s , K_j , K_d , K_k , K_h

def titlesrceen(WIN,WIDHT,HEIGHT,FPS):
    pygame.init()
    
    LIGHT_GRAY = (229,229,229)
    DARK_GRAY = (185,185,185)
    DARKER_GRAY = (150,150,150)

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
                            selector = 4
                        else:
                            selector -= 1
                    if key[K_d] or key[K_k]:
                        if selector == 4:
                            selector = 1
                        else:
                            selector += 1
                    if key[K_w] or key[K_u]:
                        if selector == 1:
                            selected = "Settings"
                        if selector == 2:
                            selected = "Start"
                        if selector == 3:
                            selected = "About"
                        if selector == 4:
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
                blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*5,"About",int(WIDHT * 0.075),DARKER_GRAY)
            else:
                blit_text_to_screen_center((WIDHT/5) * 4,HEIGHT/8*5,"About",int(WIDHT * 0.075),DARK_GRAY)
            if selector == 4:
                blit_text_to_screen_center((WIDHT/10)*9,HEIGHT/8*7,"Quit",int(WIDHT * 0.07),DARKER_GRAY)
            else:
                blit_text_to_screen_center((WIDHT/10)*9,HEIGHT/8*7,"Quit",int(WIDHT * 0.07),DARK_GRAY)
            blit_text_to_screen(WIDHT/11 * 8,HEIGHT/8*7.5,"Lenny Priewe",int(WIDHT * 0.05),DARK_GRAY)
            pygame.display.update()
                        
        return selector    


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
            blit_text_to_screen(WIDHT/9*6,HEIGHT/8*7,"UP -> Main Menu",int(WIDHT * 0.09),DARK_GRAY)


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
        else: 
            start_game = True
            return WIDHT, HEIGHT, FPS

if __name__ == "__titlescreen__":
    WIDHT, HEIGHT , FPS = 800, 800 , 60
    WIN = pygame.display.set_mode((WIDHT,HEIGHT))
    titlesrceen(WIN,WIDHT,HEIGHT,60)
    pygame.quit()