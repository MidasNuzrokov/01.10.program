from graph import *
import random
import tkinter
### Функции
def rectangle_row(x0, y0, x1, y1, N, dx, clr1, clr2, clr3):
    brushColor(clr1, clr2, clr3)
    Length = x1 - x0
    for i in range(0, N):
        rectangle(x0, y0, x0 + Length, y1)
        x0 += Length + dx
penSize(0)
#Zvetok
def blumen(a, b):
    brushColor("yellow")
    circle(a, b, 4)
    brushColor('red')
    circle(a+5, b+5, 2)
    circle(a - 5, b - 5, 2)
    brushColor('orange')
    circle(a, b + 5, 2)
    circle(a + 5, b, 2)
    brushColor('violet')
    circle(a - 5, b, 2)
    circle(a, b - 5, 2)
#Fon
def backboard():
    x1 = 0
    y1 = 250
    x2 = 500
    y2 = 800

    x3 = 0
    y3 = 0
    x4 = 500
    y4 = 500
    brushColor(0, 255, 125)
    rectangle(x1, y1, x2, y2)
    brushColor(135, 206, 250)
    rectangle(x3, y3, x4, y4)
#Oblaka
def clouds(q, w, e, r, t, y, u, o):
    for i in range(1, 6, 1):
        W = random.randint(q, w) #x1
        Q = random.randint(e, r) #y1
        E = random.randint(t, y) #x2
        R = random.randint(u, o) #y2
        c.create_oval(W, Q, E, R, outline=("black"), fill=('white'), width=0)
#Dvizenie
def update_1():
    global d
    moveObjectBy(obj, d, 0)
    if xCoord(obj) >= 500 or xCoord(obj) <= -200 :
        d=-d

###OSNOVNOY KOD
backboard()
#zvetochki na pole
for I in range(1, 50, 1):
    A = random.randint(0, 500)
    B = random.randint(500,800)
    blumen(A, B)
#Solnze
brushColor("yellow")
obj = circle(40, 40, 100)
d = 5
onTimer(update_1, 50)
#oblaka
canvasSize(500, 800)
c=canvas()
clouds(1, 2, 10, 20, 100, 300, 50, 100)
clouds(3, 5, 9, 23, 120, 298, 40, 107)
clouds(200, 220, 75, 120, 450, 500, 90, 200)
clouds(180, 230, 85, 110, 430, 506, 110, 206)
clouds(10, 15, 160, 200, 90, 130, 250, 256)
clouds(6, 17, 170, 190, 70, 135, 260, 261)
clouds(170, 200, 210, 220, 475, 480, 270, 300)
clouds(164, 213, 221, 222, 470, 485, 300, 320)
run()