#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
from math import sin, cos, radians, pi
from pyglet.window.key import DOWN, UP, LEFT, RIGHT, NUM_2, NUM_1


window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů


class Stone(object):

    def __init__(self, x=None, y=None, direction=None, speed=None, rspeed=None):

        # nečtu obrázek
        num = random.choice(range(0, 10))
        self.image = pyglet.image.load('meteorit.png')

        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        # pokud není atribut zadán vytvořím ho náhodně
        self._x = x if x is not None else random.randint(600, window.width)
        self._y = y if y is not None else random.randint(600, window.height)
        # musím správně nastavit polohu sprite
        self.x = self._x
        self.y = self._y
        self.direction = direction if direction is not None else random.randint(0, 400)
        #rychlost pohybu
        self.speed = speed if speed is not None else random.randint(40, 200)
        #rychlost otáčení
        self.rspeed = rspeed if rspeed is not None else random.randint(-5, 10)
        

   
    def tick(self, dt):
        self.bounce()

        # do promenne dt se uloží doba od posledního tiknutí
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation += 0.01 * self.rspeed
        
        


    def bounce(self):
        #vzdálenost okraje od středu
        rozmer = min(self.image.width, self.image.height)/2

        if self.x + rozmer >= window.width:
            self.direction = random.randint(200, 400)
            return
        if self.x - rozmer <= 0:
            self.direction = random.randint(30, 100)
            return
        if self.y + rozmer >= window.height:
            self.direction = random.randint(50, 150)
            return
        if self.y - rozmer <= 0:
            self.direction = random.randint(-50, 50)
            return
        

class Lodicka(object):

    def __init__(self):
        #načtení obrázku lodě
        self.obrazek = pyglet.image.load("raketa.png")

        #kotvu umístím do prostřed
        self.obrazek.anchor_x = self.obrazek.width // 2
        self.obrazek.anchor_y = self.obrazek.height // 2

        #z obrázku udělám SPRITE
        self.sprite = pyglet.sprite.Sprite(self.obrazek, batch=batch)

        self.sprite.rotation = 80
        self.speed = 400
        self.x = 600
        self.y = 400
        self.sprite.x = self.x
        self.sprite.y = self.y

    def tiktak(self, t):
        global klavesy
        self.okraj()
        #OVLÁDÁNÍ
        for data in klavesy:
            if data == LEFT:
                self.sprite.rotation -= 5
            if data == RIGHT:
                self.sprite.rotation += 5
            if data ==  UP:
                self.x = self.x + self.speed*t*sin(pi*self.sprite.rotation/180)
                self.sprite.x = self.x
                self.y = self.y + self.speed*t*cos(pi*self.sprite.rotation/180)
                self.sprite.y = self.y
            if data == DOWN:
                self.x = self.x + self.speed*t-sin(pi*self.sprite.rotation/180)
                self.sprite.x = self.x
                self.y = self.y + self.speed*t-cos(pi*self.sprite.rotation/180)
                self.sprite.y = self.y
            

    def okraj(self):
        # vzdálenost okraje od střed
        rozmer = min(self.obrazek.width, self.obrazek.height)/2
        if self.x + rozmer >= window.width + 60:
            self.sprite.x =- 20
        if self.x - rozmer < -60:
            self.sprite.x = window.width + 20
        if self.y + rozmer >= window.height + 60:
            self.sprite.y =- 20
        if self.y - rozmer < -60:
            self.sprite.y = window.height + 20

klavesy = []
for o in range(1):
    lod = Lodicka()
    pyglet.clock.schedule_interval(lod.tiktak, 1/120)

for x in range(5):
    kamen = Stone()
    pyglet.clock.schedule_interval(kamen.tick, 1/120)
    
@window.event
def on_key_release(data, mod):
    global klavesy
    klavesy.remove(data)

@window.event
def on_key_press(data, mod):
    global klavesy
    klavesy.append(data)


@window.event
def on_draw():
    window.clear()
    #image.blit(0,0)
    batch.draw()


pyglet.app.run()
