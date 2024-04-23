import turtle as t
import math
# импорт не подставляется в функцию 
from random import *

i = int(input("Введите номер задания: "))

while i > 5 or i < 1:
    print(" :( ")
    i = int(input("Введите номер задания: "))

##########################
    
def tsk_1():
    
    t.shape('circle')

    while True:
        t.forward(randint(0,100))
        t.right(randint(0,360))

##########################

def tsk_2():
    


    t.shape('turtle')

    d=math.sqrt(2*50**2)    

#ввод основных функций

    def goto(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()

#цвет

    t.color("blue")
    t.pensize(3)
    
#основные координаты
    x =-175  
    y=50


    three=([x,y,0,50],[x,0,0,50],[x,0,45,d],[x,-y,0,d],[x,y,-45,0])
    
    four=([x,y,-90,50],[x+50,y,0,100],[x,0,90,50])
      
    zero=([x,y,0,50],[x,-y,0,50],[x+50,-y,90,100],[x,-y,0,100],[x,y,-90,0])

    nine=([x,y,0,50],[x,0,0,50],[x,y,-90,50],[x+50,y,0,50],[x+50,0,-45,d],[x,y,135,0])


    n=((three),(four),(four),(zero),(nine),(zero))

#вложенный цикл,пробегающий по всем элементам листов,находящихся в кортеже  

    x =-175  
    y=50
    for i in n:
        for j in range(len(i)):
            goto(i[j][0]+x,i[j][1])
            t.left(i[j][2])
            t.forward(i[j][3])
        x += 75
    

##########################

def tsk_3():

    
    #файл

    with open('numbers.txt','r') as file:
        cont = file.read()
        numb = [str(num) for num in cont.split()] # для наглядности. str можно не писать 


    t.shape('turtle')

    d=math.sqrt(2*50**2)    

    #ввод основных функций

    def goto(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()

    #цвет

    t.color("blue")
    t.pensize(3)
        
    #основные координаты
    x =-175  
    y=50

    numb_dict={
    '0' : ([x,y,0,50],[x,-y,0,50],[x+50,-y,90,100],[x,-y,0,100],[x,y,-90,0]) ,
    '1' : ([x,0,45,d],[x+50,y,-135,100],[x+50,y,90,0]) ,
    '2' : ([x,y,0,50],[x,-50,0,50],[x+50,0,90,50],[x,-50,-45,d],[x,y,-45,0]) ,
    '3' : ([x,y,0,50],[x,0,0,50],[x,0,45,d],[x,-y,0,d],[x,y,-45,0]) ,
    '4' : ([x,y,-90,50],[x+50,y,0,100],[x,0,90,50]) ,
    '5' : ([x,y,-90,50],[x+50,0,0,50],[x,y,90,50],[x,0,0,50],[x,-50,0,50]) ,
    '6' : ([x+50,y,-135,d],[x,0,45,50],[x+50,0,0,50],[x+50,-50,-90,50],[x+50,0,0,50],[x,0,180,0]) ,
    '7' :([x,y,0,50],[x+50,y,-135,d],[x,0,45,50],[x,y,90,0]) ,
    '8' :([x,y,0,50],[x,-y,0,50],[x,y*0,0,50],[x+50,-y,90,100],[x,-y,0,100],[x,y,-90,0]) ,
    '9' :([x,y,0,50],[x,0,0,50],[x,y,-90,50],[x+50,y,0,50],[x+50,0,-45,d],[x,y,135,0]) ,

    }

    #вложенный цикл,пробегающий по всем элементам листов,находящихся в кортеже  

    x = -175  
    y = 50

    for digit in numb:
        n = [numb_dict[digit]]  # Используем цифры (которые на самом деле строки) из файла в качестве ключей для numb_dict
        for i in n:
            for j in range(len(i)):
                goto(i[j][0] + x, i[j][1])
                t.left(i[j][2])
                t.forward(i[j][3])
            x += 75
        
    t.exitonclick()
##########################

def tsk_4():
    #начальные настройки
    t.shape("circle")
    t.shapesize(0.3,0.3)
    t.goto(220,0)
    t.goto(-200,0)
    y=0
    x=-200
    ay=-9.8
    Vy=50
    Vx=20
    dt=0.08

    #основной цикл
    while True:
        #инициализация используемых законов
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt

        #моделирование отскока с потерей произвольной энергии
        if y <= 0:
            y=0
            Vy=-0.7*Vy
            Vx=0.7*Vx
            print("Vy = ", Vy ,"\nVx = ", Vx ,"\nВысота = ", y)

        #непосредственно функция движения
        t.goto(x,y)

        #условие выхода из цикла
        if Vy < 2 and y == 0 and Vx < 1:
            break
##########################

def tsk_5():
    from random import randint
   
    # Инициализация параметров контейнера
    width = 400
    height = 600

    # Функция для создания контейнера
    def create_container():
        t.shapesize(0.01, 0.01)
        t.penup()
        t.goto(-width/2, -height/2)
        t.pendown()
        for i in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

    create_container()

    # Количество частиц и количество шагов времени
    number_of_pool = 50
    steps_of_time_number = 100

    # Создание частиц
    pool = [t.Turtle(shape='circle') for _ in range(number_of_pool)]
    for particle in pool:
        particle.shapesize(0.6)
        particle.penup()
        particle.speed(0)  # Максимальная скорость
        particle.goto(randint(-200, 200), randint(-300, 300))
        particle.setheading(randint(0, 360))  # Установка случайного направления

    # Моделирование движения частиц
    for _ in range(steps_of_time_number):
        for i in range(len(pool)):
            particle = pool[i]
            particle.forward(2)
            
            # Проверка на выход за пределы контейнера и отражение от границ
            x, y = particle.position()
            if abs(x) >= width / 2:
                particle.setheading(180 - particle.heading())
            if abs(y) >= height / 2:
                particle.setheading(-particle.heading())
            
            # Проверка на столкновения между частицами
            for j in range(i+1, len(pool)): 
                other_particle = pool[j]
                if particle.distance(other_particle) < 15:  # Если частицы слишком близки
                    # Отражение частиц от столкновения
                    particle.setheading(particle.towards(other_particle) + 180)  # Установка направления на противоположное
                    other_particle.setheading(randint(0, 360))  # Установка случайного направления для другой частицы
                    """
                    other_particle.setheading(other_particle.towards(particle) + 180) для идеального газа
                    """
                    particle.forward(2)  # Дополнительное движение, чтобы избежать снова попадания в коллизию
                    other_particle.forward(2)

    t.done()

##########################

if i == 1:
    tsk_1()
elif i == 2:
    tsk_2()
elif i == 3:
    tsk_3()   
elif i == 4:
    tsk_4() 
else:
    i == 5
    tsk_5()

t.exitonclick()
