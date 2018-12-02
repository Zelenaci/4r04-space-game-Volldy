import pyglet
window = pyglet.window.Window()

def tik(t):
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

class Raketa(object):

    
    def __init__(self, x=None, y=None, direction=None, speed=None, rspeed=None):
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.width // 2
        self.x = 500
        self.y = 50
        self.rotation = 0
        selft.sprite.x = self.x
        self.sprite.y = self.y
        self.rychlost = 0
        self.uhel = 0
    

obrazek = pyglet.image.load('raketa.png')
raketa = pyglet.sprite.Sprite(obrazek)

def vykresli():
    window.clear()
    raketa.draw()

window.push_handlers(
    on_text=Raketa,
    on_draw=vykresli,
)

pyglet.app.run()
