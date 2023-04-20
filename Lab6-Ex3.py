import sys
import pygame as pg
r = 0
g = 200
b = 0

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        (m1,m2) = pg.mouse.get_pos()
        if (m1,m2) >= (self.x ,self.y) and (m1,m2) <= (self.x + self.w, self.y + self.h):
            return True
        else:
            False
        pass

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('Black') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('Orange')     # ^^^
FONT = pg.font.Font(None, 32)



font = pg.font.Font('freesansbold.ttf', 18) # font and fontsize
text1 = font.render('Name', True,pg.Color('Black'), None) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (75, 60)
input_box1 = InputBox(50, 70, 140, 32) # สร้าง InputBox1

text2 = font.render('Surname', True,pg.Color('Black'), None) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (90, 120)
input_box2 = InputBox(50, 130, 140, 32)

text3 = font.render('Age', True,pg.Color('Black'), None)
textRect3 = text3.get_rect()
textRect3.center = (65, 180)
input_box3 = InputBox(50, 190, 140, 32) 
input_boxes = [input_box1, input_box2,input_box3] 

textsentence = font.render('', True,pg.Color('Black'),None)
textsentenceRect = textsentence.get_rect()
textsentenceRect.center = (280, 450)
run = True
btn = Button(250,250,50,50)

while run:

    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(textsentence, textsentenceRect)
    btn.draw(screen)
    if btn.isMouseOn():
        btn.w = 100
        btn.h = 100
        r = 100
        g = 100
        b = 100
        if pg.mouse.get_pressed()[0] == 1:
            r = 200
            g = 0
            b = 0
            sentence = "Hello {}{}! You are {} years old.".format(input_box1.text, input_box2.text,input_box3.text)
            textsentence = font.render(sentence, True,pg.Color('Black'),None)
            textsentenceRect = textsentence.get_rect()
            textsentenceRect.center = (280, 450)
    else:
        btn.w = 100
        btn.h = 100
        r = 0
        g = 200
        b = 0

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(10)
    pg.display.update()