import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.jugador_x = 0
        self.jugador_y = 0
        self.jugador_futuro_x = self.jugador_x
        self.jugador_futuro_y = self.jugador_y
        self.jugador_velocidad = 1
        self.jugador_h = 8
        self.jugador_w = 8
        self.bloque_x = 64
        self.bloque_y = 64
        self.bloque_h = 24
        self.bloque_w = 64

        pyxel.run(self.update, self.draw)

    def update(self):

        #ORDEN:
         #0. Re-inicializar lo que se deba poner 'en cero' otra vez
         #1. Entrada de datos (botones de controles)
         #2. Actualización de 'fantasmas del futuro'
         #3. Cálculo sobre dichos 'fantasmas'
         #4. Actualización de las versiones reales
         #5. Dibujado

        #Si la 'rejilla' es en base a 8 (8x8), la velocidad puede ser 1,2,4,8...
        #Esto depende del diseño de niveles, no queremos 'problemas de tunel'
        
        #SINCRONIZACIÓN DE FANTASMAS
        self.jugador_futuro_x = self.jugador_x
        self.jugador_futuro_y = self.jugador_y
        
        #ENTRADA DE CONTROLES:
         if pyxel.btn(pyxel.KEY_RIGHT):
            self.jugador_futuro_x = (self.jugador_x + self.jugador_velocidad)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.jugador_futuro_x = (self.jugador_x - self.jugador_velocidad)
        elif pyxel.btn(pyxel.KEY_UP):
            self.jugador_futuro_y = (self.jugador_y - self.jugador_velocidad)  
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.jugador_futuro_y = (self.jugador_y + self.jugador_velocidad)
      

        #ACTUALIZACIÓN DE 'FANTASMAS'
        topEdge1 = self.jugador_futuro_y + self.jugador_h
        rightEdge1 = self.jugador_futuro_x + self.jugador_w
        leftEdge1 = self.jugador_futuro_x
        bottomEdge1 = self.jugador_futuro_y


        topEdge2 = self.bloque_y + self.bloque_h
        rightEdge2 = self.bloque_x + self.bloque_w
        leftEdge2 = self.bloque_x
        bottomEdge2 = self.bloque_y


        #PROCESO DE COLISIÓN
        #Lo que se hace es computar todos los objetos con todos los demás objetos (nxm).
        #Lo que se ha de hacer es buscar alguna mejor manera de computar una cantidad indeterminada de objetos
        
            #detección de todas las colisiones
        collides = (leftEdge1 < rightEdge2 and rightEdge1 > leftEdge2 and bottomEdge1 < topEdge2 and topEdge1 > bottomEdge2)
        
            #respuesta de todas las colisiones
        if not collides: #Si no se colisiona, entonces actualizar la 'versión real' del móvil
            self.jugador_x = self.jugador_futuro_x
            self.jugador_y = self.jugador_futuro_y

 


    def draw(self):
        #DIBUJADO
        pyxel.cls(0)
        pyxel.rect(self.jugador_x, self.jugador_y, self.jugador_h, self.jugador_w, 9)
        pyxel.rect(self.bloque_x, self.bloque_y, self.bloque_w, self.bloque_h, 3)

App()
