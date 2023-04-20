import pygame as pg
pg.init()

win_x, win_y = 800, 480 

screen = pg.display.set_mode((win_x, win_y)) 
posX, posY = 20, 20
r = 255
g = 0
b = 0


while(1): 
    
    screen.fill((255, 255, 255))
    pg.draw.rect(screen,(r,g,b),(posX,posY,100,100))

    pg.time.delay(1)
    pg.display.update() 
    
    for event in pg.event.get(): 
        if event.type == pg.KEYDOWN and event.key == pg.K_w: 
            posY -= 10
            # print("Key W down")
        if event.type == pg.KEYDOWN and event.key == pg.K_a: 
            posX -= 10
            # print("Key A down")
        if event.type == pg.KEYDOWN and event.key == pg.K_s: 
            # print("Key S down")
            posY += 10
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            # print("Key D down")
            posX += 10

        if event.type == pg.QUIT: 
            pg.quit()
            exit()
