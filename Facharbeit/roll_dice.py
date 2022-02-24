import pygame
import os
import random

from board import board

def roll_dice(max_number,WIN,WIDHT,HEIGHT):
    random_number = random.randint(1,max_number)
    if random_number == 1:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_1.png')), (500,500))
    elif random_number == 2:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_2.png')), (500,500))
    elif random_number == 3:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_3.png')), (500,500))
    elif random_number == 3:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_3.png')), (500,500))
    elif random_number == 4:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_4.png')), (500,500))
    elif random_number == 5:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_5.png')), (500,500))
    elif random_number == 6:
        DICE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Roll_Dice', 'dice_6.png')), (500,500))
    WIN.blit(DICE_IMAGE,(WIDHT/2 - 250,HEIGHT/2 - 250))
    pygame.display.update()
    pygame.time.delay(3000)
    return random_number

if __name__ == "__roll_dice__":
    WIDHT, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDHT,HEIGHT))
    board(6,6,WIN,WIDHT,HEIGHT)