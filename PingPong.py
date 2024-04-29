from pygame import *

#необходимые классы

#игровая сцена
bg = (139, 163, 108)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bg)

#флаги, отвечающие за состояние игры
game = True
finish = False

#таймер
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(FPS)

