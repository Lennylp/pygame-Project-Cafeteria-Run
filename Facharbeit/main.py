import pygame
import os
import random
from pygame.constants import K_a, K_d, K_h, K_i, K_j, K_k, K_l, K_o, K_p , K_r, K_s, K_t , K_u, K_w
from dogeball import dogeball
from board import board
from roll_dice import roll_dice
from whos_missing import whos_missing
from titlescreen import titlesrceen

def main(WIN,WIDHT,HEIGHT,FPS):
    WIDHT, HEIGHT, FPS = titlesrceen(WIN, WIDHT, HEIGHT, FPS)
    pos_red = 1
    pos_blue = 1
    Two_player = True
    while pos_red < 30 or pos_blue < 30: # gameloop
        board(pos_red,pos_blue,3,WIN,WIDHT,HEIGHT,FPS)

        random_game = random.randint(1,1) # minigame selection
        if random_game == 1:
            winner = dogeball(Two_player,WIN,WIDHT,HEIGHT)
        if random_game == 2:
            winner = whos_missing(Two_player,WIN,WIDHT,HEIGHT,FPS)

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
                pass #red win
            else:
                pass #blue win
        elif pos_red == 30:
            pass # red win
        elif pos_blue == 30:
            pass #blue win


            

if __name__ == "__main__":
    FPS = 60
    WIDHT, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDHT,HEIGHT))
    main(WIN,WIDHT,HEIGHT,FPS)