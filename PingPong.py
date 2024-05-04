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

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height)) #вместе 55, 55 - параметры
        self

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(FPS)
