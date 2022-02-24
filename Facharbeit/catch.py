import pygame
import os
import random
from pygame.constants import K_a, K_d, K_h, K_i, K_j, K_k, K_l, K_o, K_p , K_r, K_s, K_t , K_u, K_w

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
            WIN.fill((50,18,52))

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
            print(timer)

        if blue_points > red_points:
            return "blue"
        elif red_points > blue_points:
            return "red"
        else:
            "None"
            

FPS = 60
WIDHT, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDHT,HEIGHT))
catch(WIN,WIDHT,HEIGHT,FPS)