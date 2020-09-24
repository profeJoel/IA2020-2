import pygame
from pygame.locals import *

pygame.init()
ventana_x = 800 # se debe acomodar al tamaño del laberinto
ventana_y = 800 # se debe acomodar al tamaño del laberinto
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#Clase Personaje
class personaje(object):

    def __init__(self, x, y, fuente, limite, ancho):
        self.x = x
        self.y = y
        self.velocidad = 5
        #Atributos para salto
        self.ha_saltado = False
        self.impulso_salto = 10
        #Atributos para animación de Sprites
        self.va_izquierda = False
        self.va_derecha = False
        self.va_arriba = False
        self.va_abajo = False
        self.contador_pasos = 0

######################################################################################################################
        self.quieto = pygame.transform.scale( pygame.image.load("img2/ratastanding.png"), (ancho,ancho))
        self.en_movimiento = pygame.transform.scale(pygame.image.load("img2/ratita.png"), (ancho, ancho))
######################################################################################################################
        
        self.izquierda = pygame.transform.rotate(self.en_movimiento, -90)
        self.derecha = pygame.transform.rotate(self.en_movimiento, 90)
        self.arriba = pygame.transform.rotate(self.en_movimiento, 180)
        self.abajo = self.en_movimiento

        self.ancho = ancho
        self.alto = ancho
        #Controles de desplazamiento automático
        self.camino = [self.x, limite]
        #Nivel de Salud
        self.salud = 10
        #Hitbox
        self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)

        self.x0 = 0
        self.y0 = 0


######################################################################################################################
    def dibujar(self, cuadro):
        #Son 9 imágenes de la animación, para que cada una dure 3 vueltas de ciclo se multiplica por 3
        """
        if self.contador_pasos + 1 > 27:
            self.contador_pasos = 0
        """
        if self.va_izquierda:
            cuadro.blit(self.izquierda, (self.x,self.y))
        elif self.va_derecha:
            cuadro.blit(self.derecha, (self.x,self.y))
        elif self.va_abajo:
            cuadro.blit(self.abajo, (self.x,self.y))
        elif self.va_arriba:
            cuadro.blit(self.arriba, (self.x,self.y))
        else:
            cuadro.blit(self.quieto, (self.x,self.y))
        
        #Dibujar hitbox
        self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)
        #En caso de querer visualizar el hitbox, descomentar la siguiente linea
        #pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

        """
        #Crear clase barra de vida
        pygame.draw.rect(cuadro, (255,0,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50, 10))
        pygame.draw.rect(cuadro, (0,128,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50 - (5 * (10 - self.salud)), 10))
        """
        

######################################################################################################################
    def se_mueve_segun(self, k, iz, de, ar, ab, salta, lab):
        
        if k[iz] and self.x >= self.velocidad and lab.obtener_tipo(self.x - self.velocidad, self.y) != "muro" and lab.obtener_tipo(self.x - self.velocidad, self.y + self.alto) != "muro":
            self.x -= self.velocidad
            #Controles de animación
            self.va_izquierda = True
            self.va_derecha = False
            self.va_abajo = False
            self.va_arriba = False

        elif k[de] and self.x <= ventana_x - self.ancho - self.velocidad and lab.obtener_tipo(self.x + self.ancho + self.velocidad, self.y) != "muro" and lab.obtener_tipo(self.x + self.ancho + self.velocidad, self.y + self.alto) != "muro":
            self.x += self.velocidad
            #Controles de animación
            self.va_derecha = True
            self.va_izquierda = False
            self.va_abajo = False
            self.va_arriba = False
        else:
            #Controles de animación en caso de dejar de moverse en horizonal
            self.va_izquierda = False
            self.va_derecha = False
            self.va_abajo = False
            self.va_arriba = False
            self.contador_pasos = 0


        #Control de Salto

        #Si se reconoce que se ha saltado
        if self.ha_saltado:
            if self.impulso_salto >= -10:
                if self.impulso_salto < 0:
                    self.y -= (self.impulso_salto**2) * 0.5 * -1
                else:
                    self.y -= (self.impulso_salto**2) * 0.5
                self.impulso_salto -= 1
            else:
                self.ha_saltado = False
                self.impulso_salto = 10
        else:
            #Permite moverse arriba y abajo sin saltar
            if k[ar] and self.y >= self.velocidad and lab.obtener_tipo(self.x, self.y - self.velocidad) != "muro" and lab.obtener_tipo(self.x + self.ancho, self.y - self.velocidad) != "muro":
                self.y -= self.velocidad
                self.va_izquierda = False
                self.va_derecha = False
                self.va_abajo = False
                self.va_arriba = True

            if k[ab] and self.y <= ventana_y - self.alto - self.velocidad and lab.obtener_tipo(self.x, self.y + self.alto + self.velocidad) != "muro" and lab.obtener_tipo(self.x + self.ancho, self.y + self.alto + self.velocidad) != "muro":
                self.y += self.velocidad
                self.va_izquierda = False
                self.va_derecha = False
                self.va_abajo = True
                self.va_arriba = False
            #Reconoce el salto
            if k[salta]:
                self.ha_saltado = True
                #Controles de animación
                self.va_izquierda = False
                self.va_derecha = False
                self.va_abajo = False
                self.va_arriba = False
                self.contador_pasos = 0


######################################################################################################################
        
    def se_mueve_solo(self, nivel):
        if self.velocidad > 0:
            if self.x + self.velocidad < self.camino[1]:
                self.x += self.velocidad * nivel
                self.va_derecha = True
                self.va_izquierda = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0
        else:
            if self.x - self.velocidad > self.camino[0]:
                self.x += self.velocidad * nivel 
                self.va_izquierda = True
                self.va_derecha = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0
        

    #Detección de colisiones
    def se_encuentra_con(self, alguien):
        R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
        R1_ar = self.zona_impacto[1]
        R1_iz = self.zona_impacto[0]
        R1_de = self.zona_impacto[0] + self.zona_impacto[2]
        R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
        R2_ar = alguien.zona_impacto[1]
        R2_iz = alguien.zona_impacto[0]
        R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]

        return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar

    #Personaje recibe golpe de daño de parte de otro personaje
    def es_golpeado(self):
        self.ha_saltado = False
        self.impulso_salto = 10
        self.x = 100
        self.y = 410
        self.contador_pasos = 0
        self.salud -= 5
        pygame.time.delay(2000)


######################################################################################################################
#Clase bloque
class bloque(object):
    def __init__(self, x, y, ancho, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.ancho = ancho
        self.imagen = pygame.transform.scale(pygame.image.load("img2/" + tipo + ".png"), (self.ancho, self.ancho))
        #self.alto
        self.zona_impacto = [self.x, self.y, ancho, ancho]

    def dibujar(self, cuadro):
        cuadro.blit(self.imagen, (self.x, self.y))

#Clase Laberinto
class laberinto(object):
    def __init__(self, mapa):
        self.mapa = mapa
        self.matriz = []
        self.ancho = 64
        self.cantidad = 0

    def cargar(self):
        i=0
        with open(self.mapa) as en_archivo:
            for linea in en_archivo:
                self.matriz.append([])
                posicion = linea.split(' ')
                if i == 0:
                    self.cantidad = len(posicion) - 1
                    self.ancho = ventana_x // self.cantidad
                    print(self.cantidad, self.ancho)
                j=0
                for pos in posicion:
                    if pos == '0':
                        self.matriz[i].append(bloque(j * self.ancho, i * self.ancho, self.ancho, "pasto"))
                    elif pos == '1':
                        self.matriz[i].append(bloque(j * self.ancho, i * self.ancho, self.ancho, "muro"))
                    elif pos == 'F':
                        self.matriz[i].append(bloque(j * self.ancho, i * self.ancho, self.ancho, "queso_pasto"))
                    else:
                        pass
                        """
                        print("No se carga " + str(i) + str(j))
                        self.matriz[i].append(bloque(j * self.ancho, i * self.ancho, self.ancho, "pasto"))
                        """
                    j += 1	
                i += 1
    
    def pintar(self, cuadro):
        for fila in self.matriz:
            for lugar in fila:
                lugar.dibujar(cuadro)
        #pygame.display.update()

    def pinta_espacio(self, anterior, cuadro):
        x = anterior[0] // self.ancho
        y = anterior[1] // self.ancho
        self.matriz[x][y].dibujar(cuadro)
        #pygame.display.update()

    def obtener_tipo(self, x, y):
        j = x // self.ancho # horizontal
        i = y // self.ancho # vertical
        #print(self.matriz[i][j].tipo)
        return self.matriz[i][j].tipo

    def llega_salida(self, alguien):
        return self.obtener_tipo(alguien.x, alguien.y) == "queso_pasto"


######################################################################################################################

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
    #Dibujar fondo del nivel
    laberinto_ejemplo.pintar(ventana)
    #Dibujar Héroe
    heroe.dibujar(ventana)
    #Crear textos del nivel
    puntos = texto_puntos.render('Puntaje: ' + str(puntaje), 1, (0,0,0))
    nivel_actual = texto_nivel.render('Nivel: ' + str(nivel), 1, (0,0,0))
    #Dibujar textos del nivel
    ventana.blit(puntos, (350, 10))
    ventana.blit(nivel_actual, (350, 30))
    #Se refresca la imagen
    pygame.display.update()

#Subir de nivel
def subir_nivel():
    global nivel
    global nivel_maximo
    global villano
    global musica_fondo
    global ventana
    global esta_jugando
    global gana
    
    nivel += 1#Marca subida de nivel
    pygame.display.update()
    pygame.time.delay(2000)
    #Se verifica si paso el ultimo nivel
    #En caso de pasar el ultimo nivel, gana el juego y termina el ciclo del juego (esta_jugando)
    if nivel > nivel_maximo:
        pygame.mixer.music.stop()
        esta_jugando = False
        gana = True
    #En caso de pasar un nivel intermedio, se actualiza el villano y la musica de acuerdo al nuevo nivel
    else:
        villano = villanos[nivel]
        """
        pygame.mixer.music.stop()
        musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
        pygame.mixer.music.play(-1)
        """

# Inicio Funcion principal

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

    # Inicializacion de elementos del juego
    nivel = 0
    nivel_maximo = 3
    imagen_fondo = [pygame.image.load('img/bg0.jpg'), pygame.image.load('img/bg.jpg'), pygame.image.load('img/bg1.jpg'), pygame.image.load('img/bg2.jpg')]
    ruta_musica = ["snd/dubstep.mp3","snd/moose.mp3","snd/evolution.mp3","snd/epic.mp3"]
    musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
    #pygame.mixer.music.play(-1)
    puntaje = 0
    texto_puntos = pygame.font.SysFont('comicsans', 30, True)
    texto_nivel = pygame.font.SysFont('comicsans', 30, True)
    texto_intro = pygame.font.SysFont('console', 30, True)
    texto_resultado = pygame.font.SysFont('console', 80, True)
    esta_en_intro = True
    gana = False
    personaje_intro = personaje(50, 150, "heroe", ventana_y - 50, 64)


######################################################################################################################
    # Carga mapa laberinto
    #laberinto_ejemplo = laberinto("mapa.dat") # tamaño ventana (800,800)
    laberinto_ejemplo = laberinto("laberinto25x25.dat") # tamaño ventana (800,800)
    #laberinto_ejemplo = laberinto("laberinto1.dat") # tamaño ventana (2200,400)
    #laberinto_ejemplo = laberinto("laberinto2.dat") # tamaño ventana (2200, 400)
    laberinto_ejemplo.cargar()


    #Creación Personaje Héroe
    heroe=personaje(0, 0,"heroe", ventana_x, laberinto_ejemplo.ancho - 10)#Agregar límite

######################################################################################################################

    #Variables Balas
    tanda_disparos = 0
    balas = []
    sonido_bala = pygame.mixer.Sound('snd/bullet.wav')
    sonido_golpe = pygame.mixer.Sound('snd/hit.wav')

    # Seccion de intro
    while esta_en_intro:
        # control de velocidad del juego
        reloj.tick(27)
        # evento de boton de cierre de ventana
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

        ventana.fill((0,0,0)) # pinta el fondo de negro
        titulo = texto_intro.render('MI PRIMER JUEGO', 1, (255,0,0))
        personaje_intro.se_mueve_solo(2)
        instrucciones = texto_intro.render('Presione ENTER para continuar...', 1, (255,255,255))
        ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
        ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            esta_en_intro=False
            esta_jugando = True

        personaje_intro.dibujar(ventana)
        pygame.display.update()


######################################################################################################################
    # Seccion de juego
    #esta_jugando=True
    while esta_jugando:
        # control de velocidad del juego
        reloj.tick(27)
        # evento de boton de cierre de ventana
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

        teclas=pygame.key.get_pressed()
        heroe.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE, laberinto_ejemplo)

        # con esto se comprueba si el personaje llega al bloque final meta (queso)
        if laberinto_ejemplo.llega_salida(heroe):
            gana = True
            esta_jugando = False

        repintar_cuadro_juego()

######################################################################################################################















    # Seccion de pantalla final
    final = True
    while final:
        # evento de boton de cierre de ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        ventana.fill((0,0,0)) # pinta el fondo de negro
        titulo = texto_intro.render('JUEGO TERMINADO', 1, (255,0,0))
        if gana:
            resultado = texto_resultado.render('HAS GANADO! UwU', 1, (255,0,0))
            imagen_victoria = pygame.image.load("img2/ratafeliz.png")
            ventana.blit(imagen_victoria, (ventana_x//2 - imagen_victoria.get_width()//2, ventana_y//2 - imagen_victoria.get_height()//2))
        else:
            resultado = texto_resultado.render(
                'HAS PERDIDO! :(', 1, (255, 0, 0))
            imagen_fracaso = pygame.image.load("img2/ratatriste.png")
            ventana.blit(imagen_fracaso, (ventana_x//2 - imagen_fracaso.get_width()//2, ventana_y//2 - imagen_fracaso.get_height()//2))
        pts = texto_intro.render('Puntaje Total: '+str(puntaje), 1, (255,255,255))
        instrucciones = texto_intro.render('Presione ENTER para cerrar...', 1, (255,255,255))
        reintentar = texto_intro.render('Presione R para volver al juego...', 1, (255,255,255))
        ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
        ventana.blit(resultado, ((ventana_x//2)-resultado.get_width()//2, 200))
        #ventana.blit(pts,((ventana_x//2)-titulo.get_width()//2, 100))
        ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))
        ventana.blit(reintentar, ((ventana_x//2)-reintentar.get_width()//2, 350))
        pygame.display.update()

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            repetir=False
            final=False

        if tecla[pygame.K_r]:
            repetir=True
            final=False
            # se asegura de eliminar los objetos de cada personaje
            del(heroe)
            del(villano)

# Termina el juego y finaliza los elementos de pygame
pygame.quit()
