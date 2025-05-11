from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, size_x, size_y):
       super().__init__()
       self.image = transform.scale(image.load(player_img), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < win_height - 80 :
            self.rect.y += 10

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_l] and self.rect.y < win_height - 80 :
            self.rect.y += 10

player_r = Player('racket.png', 600, 200, 100, 150, 200)
player_l = Player('racket.png', -20, 200, 100, 150, 200)

ball = GameSprite('ball.png', 200, 200, 5, 50, 50)

win_widht, win_height = 736, 640
window = display.set_mode((win_widht, win_height))
display.set_caption('ping-pong')
background = transform.scale(image.load('background.png'), (win_widht, win_height))

game = True
finish = False 
clock = time.Clock()
fps = 60

speed_x = ball.speed
speed_y = ball.speed

font.init()
font = font.SysFont('Arial', 35)
win_r = font.render('Игрок левый', True, (186, 45, 45))
win_l = font.render('Игрок правый', True, (186, 45, 45))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(background, (0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player_l.update_l()
        player_r.update_r()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1 
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.x < -50:
           window.blit(win_r, (260, 100))
           finish = True
        if ball.rect.x > 736:
           window.blit(win_l, (260, 100))
           finish = True


        player_l.reset()
        player_r.reset()

    display.update()
    clock.tick(fps)
