from pygame import *
from random import *
window = display.set_mode((700,500))
display.set_caption("шхутер")

background = transform.scale(image.load("galaxy.jpg"),(700,500))
clock = time.Clock()
run = True
FPS = 60

font.init()
font1 = font.SysFont("Arial",80)
win = font1.render('YoU Win', True, (255, 198, 29))
lose = font1.render("you lOsE", True, (183, 123, 239))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
      
lost = 0
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15)
        bullets.add(bullet)


while run:
    for e in event.get():

        if e.type == QUIT:
            run = False

    if not finish:

        window.blit(background, (0,0))

        display.update()
    
    
    clock.tick(FPS)
