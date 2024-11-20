# cd C:\Users\s2017073\Desktop\"WORD SEARCH PROJECT"\
from wordsearch import ws, DIM
from wordsearch import output as sol

X, WORDS = ws()

sol()

import pygame
import sys

pygame.init()

SCALE = 45
plusfive = SCALE*(DIM+5)
screen = pygame.display.set_mode((plusfive, plusfive))
pygame.display.set_caption("Simple Pygame Example")

# VARIABLES



BLACK = (255, 255, 255)
RED = (255, 0, 0)
WHITE = (0, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 223, 0)
DARK_GRAY = (50, 50, 50)

FONT = pygame.font.SysFont(None, (4*(SCALE//5)))
BIGFONT = pygame.font.SysFont(None, (6*(SCALE//5)))
running = True

trophyIMAGE = pygame.image.load('trophy.png')
trophyRECT = trophyIMAGE.get_rect()

plusfour = SCALE*(DIM+4)
plusone = SCALE*(DIM+1)

plusoneandahalf = SCALE*(DIM+1.5)
plustwoandahalf = SCALE*(DIM+2.5)
plusthreeandahalf = SCALE*(DIM+3.5)

plusthreeandaquarter = SCALE*(DIM+3.25)


plustwo = SCALE*(DIM+2)
plusthree = SCALE*(DIM+3)



TEXT = ""
SELECTED = []
FOUND = []

xi, yi = -1, -1 #x initial, y initial
DIR = -1


def draw_grid(highlighted=SELECTED):
    for row in range(DIM):
        for col in range(DIM):
            x = col * SCALE
            y = row * SCALE

            rect = pygame.Rect(x, y, SCALE, SCALE)

            letter = X[row][col] 
            if (col, row) in highlighted:
                pygame.draw.rect(screen, RED, rect, 2)
                text = FONT.render(letter, True, RED)

            else:
                text = FONT.render(letter, True, BLACK)
                pygame.draw.rect(screen, BLACK, rect, 1)
            
            
            screen.blit(text, (x + SCALE//3, y + SCALE//3))

def get_ch(x,y):
    return X[y//SCALE][x//SCALE]

def check_adjacent(x1, y1, x2, y2, dir=-1, count=0):
    

    gx1, gy1, gx2, gy2 = x1//(SCALE), y1//(SCALE), x2//(SCALE), y2//(SCALE)


    dy = (gx2 - gx1)
    dx = (gy2 - gy1)

    if dir == -1:

        if (dx==0 and dy == 1): #right
            dir = 0

        elif (dx==1 and dy == 1): #bottom right
            dir = 1

        elif (dx==1 and dy == 0): #bottom
            dir = 2

        elif (dx==1 and dy == -1): #bottom left
            dir = 3

        elif (dx==0 and dy == -1): #left
            dir = 4

        elif (dx==-1 and dy == -1): #top left
            dir = 5

        elif (dx==-1 and dy == 0): #top
            dir = 6

        elif (dx==-1 and dy == 1): #top right
            dir = 7
        else:

            if count==0:
                return (True, dir)
            else:
                return (False, dir)
    else:
        if (dx==0 and dy == 1) and dir==0: #right
            dir = 0

        elif (dx==1 and dy == 1) and dir==1: #bottom right
            dir = 1

        elif (dx==1 and dy == 0) and dir==2: #bottom
            dir = 2

        elif (dx==1 and dy == -1) and dir==3: #bottom left
            dir = 3

        elif (dx==0 and dy == -1) and dir==4: #left
            dir = 4

        elif (dx==-1 and dy == -1) and dir==5: #top left
            dir = 5

        elif (dx==-1 and dy == 0) and dir==6: #top
            dir = 6

        elif (dx==-1 and dy == 1) and dir==7: #top right
            dir = 7
        else:
            return (False, dir)

    return (True, dir)

def reset():
    global TEXT, SELECTED, DIR, xi, yi

    SELECTED = []
    DIR = -1
    TEXT = ""
    xi, yi = -1, -1

# Main game loop


while running:
    # SETUP
    screen.fill(WHITE)
    mousex, mousey = pygame.mouse.get_pos()

    # TEXT
    # mx = FONT.render(str(mousex), True, (0, 0, 0))
    # screen.blit(mx, (plusone, plusfour))

    # my = FONT.render(str(mousey), True, (0, 0, 0))
    # screen.blit(my, (plustwoandahalf, plusfour))
    
    

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if mousex < SCALE*DIM and mousey < SCALE*DIM:

                if xi < 0 and yi < 0:
                    xi = mousex
                    yi = mousey
                
                check = check_adjacent(xi, yi, mousex, mousey, DIR, len(SELECTED))
                
                if check[0]:
                    xi, yi = mousex, mousey
                    TEXT += f"{str(get_ch(mousex, mousey))}"
                    SELECTED.append((mousex//SCALE, mousey//SCALE))
                    DIR = check[1]
                else:
                    reset()
            
            if mousex >= SCALE and mousex <= SCALE*4 and mousey >= plusthree and mousey <= plusthree+(SCALE):
                
                
                if TEXT in WORDS:
                    print("WORD FOUND", TEXT)
                    FOUND.append(TEXT)

                else:
                    print("WORD NOT FOUND", TEXT)
                
                reset()

            if mousex >= SCALE*7 and mousex <= SCALE*10 and mousey >= plusthree and mousey <= plusthree+(SCALE):
                
                X, WORDS = ws()
                sol()
                reset()
                FOUND = []
            # BUTTONS

    # WORD
    letter = FONT.render(TEXT, True, BLACK)
    screen.blit(letter, (SCALE, plusone))
    
    # CHECK BUTTON
    checkButton = pygame.Rect(SCALE, plusthree, SCALE*3, SCALE)
    pygame.draw.rect(screen, BLACK, checkButton, 1)

    checkText = FONT.render("CHECK", True, RED)
    screen.blit(checkText, (SCALE*(1.5), plusthreeandaquarter))


    # REGEN BUTTON

    regenButton = pygame.Rect(SCALE*7, plusthree, SCALE*3, SCALE)
    pygame.draw.rect(screen, BLACK, regenButton, 1)

    regenText = FONT.render("REGEN", True, RED)
    screen.blit(regenText, (((SCALE*6)+(SCALE*(1.5))), plusthreeandaquarter))


    for i in range(len(WORDS)):
        word = WORDS[i]
        if word in FOUND:

            w = FONT.render(word, True, RED)
        else:
            w = FONT.render(word, True, BLACK)
        screen.blit(w, (plusone, SCALE*(i+1)))

    draw_grid(SELECTED)

    if len(WORDS) == len(FOUND):
        winBOX = pygame.Rect(0, 0, screen.get_width(), screen.get_height())
        pygame.draw.rect(screen, RED, winBOX)
        pygame.draw.rect(screen, WHITE, winBOX, 4)

        #winTEXT = FONT.render("YOU WIN", True, RED)

        winTEXT = BIGFONT.render("YOU WIN", True, WHITE)
        textRECT = winTEXT.get_rect(center=(screen.get_width()//2, screen.get_height()//2))

        screen.blit(winTEXT, textRECT)

        ctTEXT = FONT.render("Press SPACE to Exit", True, WHITE)
        ctRECT = ctTEXT.get_rect(center=(screen.get_width() // 2, textRECT.bottom + SCALE))
        screen.blit(ctTEXT, ctRECT)

        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False 
    # Updates
    pygame.display.flip()

pygame.quit()
sys.exit()
