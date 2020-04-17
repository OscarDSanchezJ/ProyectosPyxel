import pyxel
import math
#objetos
class Jugador(object):
    def __init__(self, x, y, h, w):
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self.collide = True
        self.velocidad = 1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self,value):
        self._y = value

    @property
    def h(self):
        return self._h

    @x.setter
    def h(self,value):
        self._h = value

    @property
    def w(self):
        return self._w

    @x.setter
    def w(self,value):
        self._w = value

class Pared(object):
    def __init__(self, x, y, h, w):
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self.collide = True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self,value):
        self._y = value

    @property
    def h(self):
        return self._h

    @x.setter
    def h(self,value):
        self._h = value

    @property
    def w(self):
        return self._w

    @x.setter
    def w(self,value):
        self._w = value

class Caja(object):
    def __init__(self, x, y, h, w):
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self.collide = True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self,value):
        self._y = value

    @property
    def h(self):
        return self._h

    @x.setter
    def h(self,value):
        self._h = value

    @property
    def w(self):
        return self._w

    @x.setter
    def w(self,value):
        self._w = value

class Pyxoban(object):
    def __init__(self):
        pyxel.init(120,240,caption = "Pyxoban")
        self.jugador = Jugador(0,0,16,16)
        self.caja = Caja(32,32,16,16)
        self.pared = Pared(64,64,16,16)
        self.jf_x = self.jugador.x
        self.jf_y = self.jugador.y

        #MUSIC
        pyxel.sound(0).set("e3e3c3f1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr","p","6","vffn fnff vffs vfnn",25,)
        pyxel.sound(1).set("r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ","s","6","nnff vfff vvvv vfff svff vfff vvvv svnn",25,)
        pyxel.sound(2).set("c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
        pyxel.sound(3).set("f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
        pyxel.sound(4).set("f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25)
        self.play_music()
        pyxel.run(self.update, self.draw)

    def play_music(self):
        pyxel.play(0, [0, 1], loop=True)
        pyxel.play(1, [2, 3], loop=True)
        pyxel.play(2, 4, loop=True)
#Dibujado de los objetos
#--------------------------------------------------------------------
    def draw_jugador(self, Jugador):
        pyxel.rect(self.jugador.x,self.jugador.y, 16, 16, 10)

    def draw_pared(self, Pared):
        pyxel.rect(self.pared.x, self.pared.y, 16, 16, 15)

#--------------------------------------------------------------------
#Actualizacion del juego Principal
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.jf_x = (self.jugador.x + self.jugador.velocidad)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.jf_x = (self.jugador.x - self.jugador.velocidad)
        elif pyxel.btn(pyxel.KEY_UP):
            self.jf_x = (self.jugador.y - self.jugador.velocidad)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.jf_x = (self.jugador.y + self.jugador.velocidad)

        #ACTUALIZACIÓN DE 'FANTASMAS'
        topEdge1 = self.jf_y + self.jugador.h
        rightEdge1 = self.jf_x + self.jugador.w
        leftEdge1 = self.jf_x
        bottomEdge1 = self.jf_y


        topEdge2 = self.pared.x + self.pared.h
        rightEdge2 = self.pared.x + self.pared.w
        leftEdge2 = self.pared.x
        bottomEdge2 = self.pared.y


        #PROCESO DE COLISIÓN

        collides = (leftEdge1 < rightEdge2 and rightEdge1 > leftEdge2 and bottomEdge1 < topEdge2 and topEdge1 > bottomEdge2)

            #respuesta de todas las colisiones
        if not collides: #Si no se colisiona, entonces actualizar la 'versión real' del móvil
            self.jugador.x = self.jf_x
            self.jugador.y = self.jf_y

#Dibujado del juego Principal
    def draw(self):
        pyxel.cls(0)
        self.draw_jugador(self.jugador)
        self.draw_pared(self.pared)


Pyxoban()
