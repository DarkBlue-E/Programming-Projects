#This is not my program, it is a project I copied, the orginal can be found by clicking this link - https://vm.tiktok.com/ZMkE5PrBa/


import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('#262626')
t.pencolor('magenta')
t.speed(100)

col = ('cyan', 'yellow', 'red', 'light green')

for n in range(10):
    for x in range(8):
        t.speed(x + 10)
        for i in range(2):
            t.pensize(2)
            t.circle(80 + 20 * n, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n % 4])

turtle.done()