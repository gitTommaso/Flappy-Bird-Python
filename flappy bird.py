import pygame
import random

pygame.init()

sfondo = pygame.image.load('immagini\\sfondo.png')
uccello = pygame.image.load('immagini\\uccello.png')
base = pygame.image.load('immagini\\base.png')
gameover = pygame.image.load('immagini\\gameover.png')
tubo_giu = pygame.image.load('immagini\\tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False,
                                True)  # per capovolgere il tubo. Prima istruzione l'immagine, seconda orizzontale, terza verticale

schermo = pygame.display.set_mode((288, 512))  # finestra di gioco
FPS = 50  # fotogrammi al secondo. Piu' il valore è alto meno scatti ci saranno
VEL_AVANZ = 3
font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)  # bold è grassetto


class tubi_classe():
    def __init__(self):
        global x
        x = 0
        self.x = 300
        x = VEL_AVANZ - 2
        self.y = random.randint(-75, 150)

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        schermo.blit(tubo_giu, (self.x, self.y + 210))
        schermo.blit(tubo_su, (self.x, self.y - 210))

    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 5
        uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy + tolleranza
        uccello_lato_giu = uccelloy + uccello.get_height() - tolleranza
        tubi_lato_su = self.y + 110
        tubi_lato_giu = self.y + 210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()

    def fra_i_tubi(self, uccello, uccellox):
        tolleranza = 5
        uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True


def disegna_oggetti():
    schermo.blit(sfondo, (0, 0))
    for t in tubi:
        t.avanza_e_disegna()
    schermo.blit(uccello, (uccellox, uccelloy))
    schermo.blit(base, (basex, 400))
    punti_render = font.render(str(punti), 1, (255, 255, 255))  # i numeri ultimi sono i colori
    schermo.blit(punti_render, (144, 0))


def aggiorna():
    pygame.display.update()  # aggiorna schermo
    pygame.time.Clock().tick(FPS)  # frame per secondo


def inizializza():
    global uccellox, uccelloy, uccello_vely, basex
    global tubi
    global punti
    global fra_i_tubi
    uccellox, uccelloy = 60, 150  # posizione sullo schermo
    uccello_vely = 0  # velocità iniziale
    basex = 0
    punti = 0
    tubi = []
    tubi.append(tubi_classe())
    fra_i_tubi = False


def hai_perso():
    schermo.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():  # legge tutto quello che fa la tastiera
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # space è il pulsante spazio
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:  # chiudere finestra di gioco
                pygame.quit()


inizializza()
while True:
    basex -= VEL_AVANZ
    if basex < -45:
        basex = 0
    uccello_vely += 1
    uccelloy += uccello_vely
    for event in pygame.event.get():  # legge tutto quello che fa la tastiera
        if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_UP):  # K_UP==tasto in su  KEYDOWN==TASTO DELLA TASTIERA QUALUNQUE
            uccello_vely = -8  # inzia a salire
            if event.type == pygame.QUIT:  # chiudere finestra di gioco
                pygame.quit()
            if uccelloy > 380:
                hai_perso()
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)
    if not fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
            if fra_i_tubi:
                fra_i_tubi = False
                for t in tubi:
                    if fra_i_tubi==True:
                        punti += 1

    disegna_oggetti()
    aggiorna()

