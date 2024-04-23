import turtle

i = int(input("Введите номер задания: "))

while i > 14 or i < 2:
    print(" :( ")
    i = int(input("Введите номер задания: "))
##########################
def tsk_2():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90) 
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
##########################
def tsk_3():
    turtle.shape('turtle')
    for i in range(0,4,1):
        turtle.forward(50)
        turtle.left(90)
##########################        
def tsk_4():
    turtle.shape('turtle')
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()
    for i in range (0,360,1):
        turtle.forward(1)
        turtle.left(1)
##########################
def tsk_5():
    turtle.shape('turtle')
    step=10
    for i in range (0,10,1):
        for i in range(0,4,1):
            turtle.forward(step)
            turtle.left(90)
        turtle.penup()
        turtle.left(180)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.left(90)
        step += 10    
##########################
def tsk_6():
    turtle.shape('turtle')
    for i in range (0,12,1):
        turtle.right(30)
        turtle.forward(50)
        turtle.goto(0,0)
##########################
def tsk_7():
    turtle.shape('turtle')
    for i in range (0,720,1):
        turtle.forward(i*0.005)
        turtle.left(3)
##########################   
def tsk_8():
    turtle.shape('turtle')
    for i in range (1,26,1):
        turtle.forward(5*i)
        turtle.left(90)
##########################
def tsk_9():
    import math
    turtle.shape('turtle')

    def help_9():
        for n in range (0,i,1): 
            turtle.left(360*(1/i))
            turtle.forward(10*i)

    for i in range (3,13,1):
        turtle.penup()
        turtle.goto(0,0)
        r=(10*i)/(2*math.sin(math.pi/(i)))
        turtle.forward(r)
        turtle.left(180*(i-2)/(2*i))
        turtle.pendown()
        help_9()    
##########################
def tsk_10():
    turtle.shape('turtle')

    def help_10():
        for i in range (0,60,1):
            turtle.forward(6)
            turtle.right(6)
        for i in range (0,60,1):
            turtle.forward(6)
            turtle.left(6)
        
    for n in range (0,3,1):        
        help_10()
        turtle.left(120)
##########################
def tsk_11():
    turtle.shape('turtle')

    def help_11_L(n):
        for i in range (0,60,1):
                turtle.forward(6+n)
                turtle.left(6)
    def help_11_R(n):
        for i in range (0,60,1):
                turtle.forward(6+n)
                turtle.right(6)

    turtle.left(90)

    for n in range (0,10,1):
        help_11_L(n)
        help_11_R(n)
##########################
def tsk_12():
    turtle.shape('turtle')

    turtle.penup()
    turtle.goto(-450,0)
    turtle.pendown()

    def help_12_1():
        for i in range (0,30,1):
            turtle.forward(6)
            turtle.right(6)

    def help_12_2():
        for i in range (0,5,1):
            turtle.forward(6)
            turtle.right(36) 

    turtle.left(90)
    for n in range (0,10,1):
        help_12_1()
        help_12_2()
##########################        
def tsk_13():

    turtle.shape('turtle')

    def help_1():
        turtle.fillcolor("grey")
        turtle.begin_fill()
        for i in range (0,2,1):
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(180)
            turtle.left(90)
        turtle.end_fill()

    def help_2():
        turtle.fillcolor("grey")
        turtle.begin_fill()
        for i in range (0,2,1):
            turtle.forward(170)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
        turtle.end_fill()

    def help_3():
        turtle.fillcolor("grey")
        turtle.begin_fill()
        turtle.left(90)
        for i in range (0,30,1):
            turtle.forward(8)
            turtle.right(6)
        turtle.right(90)
        turtle.forward(150)
        turtle.end_fill()

    def help_4():
        turtle.fillcolor("#5D8AA8")
        turtle.begin_fill()
        for i in range (0,60,1):
            turtle.forward(6)
            turtle.right(6)
        turtle.end_fill()    

    def help_5():
        turtle.fillcolor("#36454F")
        turtle.begin_fill()
        for i in range (0,60,1):
            turtle.forward(1)
            turtle.right(6)
        turtle.end_fill()

    def help_6():
        turtle.right(90)
        turtle.width(5)
        for i in range (0,30,1):
            turtle.forward(3)
            turtle.right(6)
    def goto(x,y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()


    goto(-100,0)
    help_1()
    goto(-110,-20)
    help_2()
    goto(-101,170)
    help_3()

    goto(-23,40)
    help_4()
    goto(-45,100)
    help_5()
    goto(7,100)
    help_5()
    goto(-45,60)
    help_6()

    goto(-15,105)
    turtle.width(3)

    turtle.forward(8)
    goto(0,0)
##########################
def tsk_14(): 
    turtle.shape('turtle')

    def goto(x,y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

    def star(n):
        for i in range (0,n,1):
            turtle.forward(100)
            turtle.left(180+(180/n))

    star(5)
    goto(200,0)
    star(11)
##########################  
if i ==2:
    tsk_2()  
      
elif i ==3:
    tsk_3() 
  
elif i ==4:
    tsk_4() 
   
elif i ==5:
    tsk_5() 
    
elif i ==6:
    tsk_6() 
    
elif i ==7:
    tsk_7() 
    
elif i ==8:
    tsk_8()
    
elif i ==9:
    tsk_9()
     
elif i ==10:
    tsk_10()     
    
elif i ==11:
    tsk_11() 
    
elif i ==12:
    tsk_12() 
    
elif i ==13:
    tsk_13()  
    
else:
    tsk_14()

turtle.exitonclick()