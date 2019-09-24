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
    brushColor(0, 0, 0)
    rectangle(x1, y1, x2, y2)
    brushColor(100, 100, 100)
    rectangle(x3, y3, x4, y4)
def house():
    x1 = 30
    y1 = 300
    x2 = 300
    y2 = 650
    brushColor(230, 230, 230)
    rectangle(x1, y1, x2, y2)
    rectangle_row(x1 + 20, y2 - 175, x1 + 80, y2 - 50, 3, 25, 139, 69, 19)  # окна снизу
    rectangle_row(x1+20, y1+110, x1+60, y1+40, 5, 10, 43, 44, 124)  # окна сверху
    rectangle_row(x1, y1 + 70, x1 + 10, y1 + 115, 9, 20, 0, 0, 0)  # перила
    rectangle(x1 - 10, y1 + 115, x2 - 10, y1 + 120)  # подоконник
    rectangle(x1 - 10, y1 + 60, x2 - 3, y1 + 80)  # штука на перилах
    penSize(4)
    line(x2 - 10, y1 + 120, 300, y1 + 110)  # бок пола подокнника
def clouds(q, w, e, r, t, y, u, o):
    for i in range(1, 6, 1):
        W = random.randint(q, w) #x1
        Q = random.randint(e, r) #y1
        E = random.randint(t, y) #x2
        R = random.randint(u, o) #y2
        c.create_oval(W, Q, E, R, outline=("black"), fill=("gray"), width=0)
def update():
  moveObjectBy(obj, 5, 0)
  if xCoord(obj) >= 500:
    close()
### Код
canvasSize(500, 800)
penColor('black')
c=canvas()
backboard()
### Облака
clouds(1, 2, 10, 20, 100, 300, 50, 100)
clouds(200, 220, 75, 120, 450, 500, 90, 200)
clouds(10, 15, 160, 200, 90, 130, 250, 256)
clouds(170, 200, 210, 220, 475, 480, 270, 300)
clouds(1, 5, 210, 230, 100, 300, 350, 400)
house()
brushColor(0, 0, 0)
obj = polygon([(10, 300), (30, 280),  (300, 280), (320, 300)])
onTimer(update, 50)
run()
