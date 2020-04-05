import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120)

        pyxel.load("assets/runamy.pyxres")

        self.jugador_x = 0
        self.jugador_y = 0
        self.jugador_h = 16
        self.jugador_w = 16

        pyxel.run(self.update, self.draw)

    def update(self):
        #MOVIMIENTOS DEL JUGADOR
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.jugador_x = (self.jugador_x + 1) % pyxel.width

        elif pyxel.btn(pyxel.KEY_LEFT):
            self.jugador_x = (self.jugador_x - 1) % pyxel.width

        elif pyxel.btn(pyxel.KEY_UP):
            self.jugador_y = (self.jugador_y - 1) % pyxel.height

        elif pyxel.btn(pyxel.KEY_DOWN):
            self.jugador_y = (self.jugador_y + 1) % pyxel.height
        #COLISION CON LA PARED



    def draw(self):
        #DIBUJADO
        pyxel.cls(0)
        #Uso de recursos
        #btl(x, y, img, u, v, w, h)
        #pyxel.blt(self.jugador_x, self.jugador_y, 0, 0 ,0 ,self.jugador_w, self.jugador_h)
        if pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.blt(self.jugador_x, self.jugador_y, 0, 0 ,0 ,self.jugador_w, self.jugador_h)

        elif pyxel.btn(pyxel.KEY_LEFT):
            pyxel.blt(self.jugador_x, self.jugador_y, 0, 0 ,0 ,-self.jugador_w, self.jugador_h)

        elif pyxel.btn(pyxel.KEY_UP):
            pyxel.blt(self.jugador_x, self.jugador_y, 0, 48 ,0 ,-self.jugador_w, self.jugador_h)

        elif pyxel.btn(pyxel.KEY_DOWN):
            pyxel.blt(self.jugador_x, self.jugador_y, 0, 0 ,0 ,self.jugador_w, self.jugador_h)

App()
