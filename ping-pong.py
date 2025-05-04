from pygame import *

win_widht, win_height = 736, 640
window = display.set_mode((win_widht, win_height))
display.set_caption('ping-pong')
background = transform.scale(image.load('background.png'), (win_widht, win_height))

game = True
finish = False 
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(background, (0, 0))

    display.update()
    clock.tick(fps)