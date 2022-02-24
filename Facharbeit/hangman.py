import pygame
import random
from pygame import key
from pygame.constants import K_KP_0, K_a,K_b,K_c,K_d,K_e,K_f,K_g,K_h,K_i,K_j,K_k,K_l,K_m,K_n,K_o,K_p,K_q,K_r,K_s,K_t,K_u,K_v,K_w,K_x,K_y,K_z


if True: #help to import in main file

    def hangman(WIN,WIDHT,HEIGHT,possible_words):

        pygame.init()


        LIGHT_GRAY = (229,229,229)
        DARK_GRAY = (185,185,185)
        DARKER_GRAY = (150,150,150)
        BLUE = (111,117,204)
        RED = (204,111,111)
        GREEN = (111,204,111)
        DARK_RED = (225,100,100)
        
        
        def custom_input(keys):
            if keys[K_a]:
                return "a"
            elif keys[K_b]:
                return "b"
            elif keys[K_c]:
                return "c"
            elif keys[K_d]:
                return "d"
            elif keys[K_e]:
                return "e"
            elif keys[K_f]:
                return "f"
            elif keys[K_g]:
                return "g"
            elif keys[K_h]:
                return "h"
            elif keys[K_i]:
                return "i"
            elif keys[K_j]:
                return "j"
            elif keys[K_k]:
                return "k"
            elif keys[K_l]:
                return "l"
            elif keys[K_m]:
                return "m"
            elif keys[K_n]:
                return "n"
            elif keys[K_o]:
                return "o"
            elif keys[K_p]:
                return "p"
            elif keys[K_q]:
                return "q"
            elif keys[K_r]:
                return "r"
            elif keys[K_s]:
                return "s"
            elif keys[K_t]:
                return "t"
            elif keys[K_u]:
                return "u"
            elif keys[K_v]:
                return "v"
            elif keys[K_w]:
                return "w"
            elif keys[K_x]:
                return "x"
            elif keys[K_y]:
                return "y"
            elif keys[K_z]:
                return "z"

        def return_str(word,guesses):
            sum = ""
            for l in word:
                if l.lower() in guesses:
                    sum += f"{l} "
                else:
                    sum += "_ "
            
            return sum


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

        def keybord(WIDHT,HEIGHT,player,guesses):

            class Selector():
                def __init__(self):
                    self.x = 0
                    self.y = 0 

                def move(self,keys,player):
                    print(keys)
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
                    
            def draw_keybord(possible_keys,selector):
                for i in range(0,3):
                    for j in range(0,10):
                        if selector.x == j and selector.y == i:
                            draw_key(50 + 70 * j,HEIGHT * 0.635 + 70 * i, 60,60,possible_keys[i][j],player)
                        else:
                            draw_key(50 + 70 * j,HEIGHT * 0.635 + 70 * i, 60,60,possible_keys[i][j],"None")
                        

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
                draw_keybord(possible_keys,selector)

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


                current_guess = keybord(WIDHT, HEIGHT, current_player, guesses)

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
            possible_words =["Hi","Ho","Ha","Maren"]
        word = possible_words[random.randrange(0,possible_words.__len__())]

        return game(word)
            
        


WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
hangman(WIN,WIDHT,HEIGHT,None)

