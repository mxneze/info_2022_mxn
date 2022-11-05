import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
height = 600
width = 800
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
pts = 0
count = -2

def new_ball(x, y, r):
    '''рисует новый шарик '''
    circle(screen, color, (x, y), r)

def new_rect(xc, yc, xd, yd):
    rect(screen, COLORS[randint(0,5)], (xc, yc, xd, yd), 500)

'''def otr_ball(x, y, r, vx, vy):                           Эта процедура не хочет работать в "main"
            if width - x <= r:
                x = width - r
                vx = -vx
            if height-y <= r:
                y = height - r
                vy = -vy
            if  x <= r:
                x = r
                vx = -vx
            if  y <= r:
                y = r
                vy = -vy                                      '''
       
def click_circle(x, y, r, posx, posy):
    '''решает попал ли игрок или нет'''
    if (posx-x)**2+(posy-y)**2<=r**2:
        return False
    else:
        return True

def click_rect(x, y, x1, y1, posx, posy):
    if posx >= x and posx <= x + x1 and posy >= y and posy <= y + y1:
        return False
    else:
        return True
    

def show_points(location, i, r, pts):
    '''считает количество очков за 1 клик по принципу "быстрее и точнее"'''
    if location == True:
        pts = int((1/i)*100) + int((1/r)*100)
        return pts

pygame.display.update()
clock = pygame.time.Clock()
finished = False
tapped = False

while not finished:
    clock.tick(FPS)
    x = randint(100, 800)                       # без ооп и наследования я не знаю как спрятать эти переменные
    y = randint(100, 500)                       # в процедуру (процедуры) и отдельно "обьявлять" новый шар
    r = randint(50, 100)                        # и другой процедурой двигать его и тд
    color = COLORS[randint(0, 5)]               # дело не в global, а в том, что я окончательно запутался как это все связать
    velocity_x = randint (-15, 15)              # там подводные камни, я пытался
    velocity_y = randint (-15, 15)              # В общем: я тут осознанно нарушил принцип хорошего кода
    if count % 3 == 2:
            xc, yc = randint(50, 700), randint(50, 550)
            xd, yd = randint(30, 150), randint(30, 150)
            vel_rect = 4
    for i in range (FPS):
        clock.tick(FPS)
        if count % 3 == 0:
            new_rect(xc, yc, xd, yd)
            xc -= vel_rect
            yc -= vel_rect
            xd += 2*vel_rect
            yd += 2*vel_rect
        new_ball(x, y, r)
        if width - x <= r:                      # вместо этих 4 if должна быть процедура отражения шара, но она что-то не срабатывает 
            x = width - r                       # :sad
            velocity_x = -velocity_x
        if height-y <= r:
            y = height - r
            velocity_y = -velocity_y
        if  x <= r:
            x = r
            velocity_x = -velocity_x
        if  y <= r:
            y = r
            velocity_y = -velocity_y
        x+=velocity_x
        y+=velocity_y
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if count % 3 == 0:
                    finished = click_circle(x, y, r, event.pos[0], event.pos[1]) or click_rect(xc, yc, xd, yd, event.pos[0], event.pos[1])
                else:
                    finished = click_circle(x, y, r, event.pos[0], event.pos[1])
                current = show_points(not(finished), i, r, pts)
                if type(current) == int:
                    pts += current
                    print("Your points: ", pts)
                count += 1
                i = 30
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()
        screen.fill(BLACK)
    screen.fill(color)

pygame.quit()
print("Your result: ", pts)

