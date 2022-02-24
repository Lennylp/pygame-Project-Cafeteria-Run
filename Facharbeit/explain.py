import pygame
from pygame.constants import K_a, K_d, K_h, K_i, K_j, K_k, K_l, K_o, K_p , K_r, K_s, K_t , K_u, K_w

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
    


FPS = 60
WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
explain(WIN,WIDHT,HEIGHT,FPS,"tictactoe")
