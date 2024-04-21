from pygame import *

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (148, 0, 211))
lose = font.render('YOU LOSE', True,(230, 16, 16))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 550:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.speed = 5
        if self.rect.x <= 650:
            self.direction = "right"
        if self.rect.x >= 550:
            self.direction = "left" 

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_widht, wall_height):
        super(). __init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.widht =  wall_widht
        self.height = wall_height
        self.image = Surface((self.widht, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))
hero = Player ('hero.png', 20, 400, 10)
cyborg = Enemy ('cyborg.png', 90, 90 ,15)
treasure = GameSprite ('treasure.png', 600, 40, 600)



wall1 = Wall(22, 145, 28, 100, 20, 10, 300)
wall2 = Wall(22, 145, 28, 150, 450, 350, 10)
wall3 = Wall(22, 145, 28, 100, 20, 400, 10)

clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play( )

x1 = 100
y1 = 100

finish = False
game = True 
while  game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
         

        window.blit(background,(0, 0))
        hero.update()
        hero.reset()
        cyborg.update()
        cyborg.reset()
        treasure.update()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        
        if sprite.collide_rect(hero, treasure):
            window.blit(win, (200, 200))
            finish = True
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3):
            finish = True
            window.blit(lose, (200, 200))


    display.update()
    clock.tick(FPS)