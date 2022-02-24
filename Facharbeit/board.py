import pygame
import os

def board(pos_red,pos_blue,time_wait,WIN,WIDHT,HEIGHT,FPS):
        
    WHITE = (255,255,255)

    class pos():
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
    IMAGE_SCHOOL = pygame.transform.scale(pygame.image.load(os.path.join("Assets_Board", "school1_board.png")),(WIDHT,HEIGHT))
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

if __name__ == "__board__":
    WIDHT, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDHT,HEIGHT))
    board(6,22,WIN,HEIGHT,WIDHT)
    