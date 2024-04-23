import pygame
from pygame.draw import *
from random import choice, randint
                        # блок настроек игры
# параметры экрана
WIDTH, HEIGHT = 1200, 900
FPS = 30
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
#ф-я по созданию шаров, готовых к изменениям в соответсвтии с задачей игры 
def new_ball(screen):
    r = randint(30, 50)
    x = randint(100, WIDTH - r)
    y = randint(100, HEIGHT - r)
    color = choice(COLORS)  # случайный цвет из списка COLORS
    vx = randint(-25, 25)  # случайная скорость по  X
    vy = randint(-25, 25)  # случайная скорость по  Y
    return {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy, 'color': color}  # в качетсве результата выполнения ф-и передаем словарь
#ф-я по проверке попадания в шарик
def is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
    distance = ((click_x - ball_x) ** 2 + (click_y - ball_y) ** 2) ** 0.5
    return distance <= ball_r
# ф-я игры 
def game(screen, clock, finished, balls):  # передача ключевых параметров 
    score = 0
    while not finished:
                                # подблок технических составляющих игры 
        # Отрисовка шариков
        screen.fill(BLACK)
        """
        for ball in balls:
            circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        """
        # Обновление экрана
        pygame.display.update()

        # Управление частотой кадров
        clock.tick(FPS)

                                # подблок обработки событий в ф-и
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                print("total score:",score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('click')    
                # получаем координаты курсора в момент клика 
                click_x, click_y = pygame.mouse.get_pos()
                # проверка, попал ли курсор в область каждого шара
                for ball in balls:
                    if is_inside_ball(ball['x'], ball['y'], ball['r'], click_x, click_y):
                        print("got")
                        # удаление шарика из списка
                        balls.remove(ball)  
                        # Добавление нового шарика в другом месте
                        balls.append(new_ball(screen))
                        score += 1
                            # подблок реализации условий задачи 
        # обновление координат шариков при их столкновение с границами экрана
        for ball in balls:
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']
            # реализация отскока в случайную сторону с разной скоростью( углубленная реализация фактора непредсказуемости)
            if ball['x'] < ball['r']: # слева
                ball['x'] = ball['r']
                ball['vx'] = randint(1, 25) if ball['vx'] < 0 else randint(-25, -1)  
                ball['vy'] = randint(1, 25) if ball['vy'] < 0 else randint(-25, -1)
            elif ball['x'] > WIDTH - ball['r']: # справа
                ball['x'] = WIDTH - ball['r']
                ball['vx'] = randint(-25, -1) if ball['vx'] > 0 else randint(1, 25)
                ball['vy'] = randint(-25, -1) if ball['vy'] > 0 else randint(1, 25) 
            if ball['y'] < ball['r']: # снизу
                ball['y'] = ball['r']
                ball['vx'] = randint(1, 25) if ball['vx'] < 0 else randint(-25, -1)
                ball['vy'] = randint(1, 25) if ball['vy'] < 0 else randint(-25, -1) 
            elif ball['y'] > HEIGHT - ball['r']: # сверху
                ball['y'] = HEIGHT - ball['r']
                ball['vx'] = randint(-25, -1) if ball['vx'] > 0 else randint(1, 25)
                ball['vy'] = randint(-25, -1) if ball['vy'] > 0 else randint(1, 25)  
                            # блок ф-и игры 
def main():
    # инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("colorful balls")
    # создание объекта clock для управления fps
    clock = pygame.time.Clock()
    finished = False
    # создание списка шаров при помощи генератора из теории
    balls = [new_ball(screen) for item in range(3)]  
    # запуск игры
    game(screen, clock, finished, balls)
    # завершение работы Pygame
    pygame.quit()

main()
