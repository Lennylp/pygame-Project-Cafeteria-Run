import pygame
import random 
import os
from pygame.constants import K_a, K_d, K_h, K_i, K_j, K_k, K_l, K_o, K_p , K_r, K_s, K_t , K_u, K_w


if True:
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


WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
tictactoe(WIN,WIDHT,HEIGHT,60)
