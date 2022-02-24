import pygame
import os

def end(winner,WIN,WIDHT,HEIGHT,FPS):
    BLUE_WIN = pygame.transform.scale(pygame.image.load(os.path.join("Assets_End","winner_blue.png")), ())
    if winner == "blue":
        