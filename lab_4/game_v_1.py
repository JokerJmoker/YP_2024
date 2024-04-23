import pygame
from pygame.draw import *
from random import choice, randint
                                    # блок настроек игры
# параметры экрана
WIDTH, HEIGHT = 1200, 900
FPS = 2
BLACK = (0, 0, 0)
# цвета шаров
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
                                    # блок используемых компонент в ф-и игры
# ф-я , отвечающая за создание нового шара в рамках заданного пространства 
def new_ball(screen):
    r = randint(50, 80)
    x = randint(100, WIDTH - r)
    y = randint(100, HEIGHT - r)
    color = choice(COLORS)
    circle(screen, color, (x, y), r)
    return x, y, r
#ф-я по проверке попадания в шарик
def is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
    distance = ((click_x - ball_x) ** 2 + (click_y - ball_y) ** 2) ** 0.5
    return distance <= ball_r
# ф-я, непосредственно реализующая логику игры
def game(screen, clock, finished):  
    
    score = 0 # инициализация счетчика из задания 
    while not finished:
                            # подблок обработки событий в ф-и
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                print("total score:",score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')    
                # получение координат курсора мыши в момент клика
                click_x, click_y = pygame.mouse.get_pos()
                if is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
                    print("got")
                    score += 1      # реализация счетчика очков 
                            #подблок интерактивных объектов в ф-и игры 
        # создание нового шара 
        ball_x, ball_y, ball_r = new_ball(screen)
        # обновление экрана
        pygame.display.update()
        screen.fill(BLACK)
        # Управление частотой кадров
        clock.tick(FPS)
                            # блок конечного результата в виде самой игры 
def main():
    # инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colorful Balls")
    # создание объекта сlock для управления fps
    clock = pygame.time.Clock()
    finished = False
   
    game(screen, clock, finished)  

    # завершение работы pygame
    pygame.quit()

main()

