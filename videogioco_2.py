import pygame

pygame.init()


sfondo=pygame.image.load('G:\\Python\\videogiochi\\immagini\\mario_sfondo.jpg')
principessa=pygame.image.load('G:\\Python\\videogiochi\\immagini\\super-mario-bros.jpg')
base=pygame.image.load('G:\\Python\\videogiochi\\immagini\\base.png')
gameover=pygame.image.load('G:\\Python\\videogiochi\\immagini\\gameover.png')
cattivo=pygame.image.load('G:\\Python\\videogiochi\\immagini\\cattivo.png')

schermo=pygame.display.set_mode((512,288)) #finestra di gioco
FPS=50 #fotogrammi al secondo
VEL_AVANZ=3




def inizializza():
    global principessax,principessay,principessa_vely,basex
    principessax,principessay=12,230 #posizione personaggio sullo schermo
    principessa_vely=0 #velocità iniziale
    basex=0
    
def disegna_oggetti():
    schermo.blit(sfondo,(0,0))
    schermo.blit(principessa,(principessax,principessay))
    schermo.blit(base,(basex,270))

def aggiorna():
    pygame.display.update() #aggiorna schermo
    pygame.time.Clock().tick(FPS) #frame per secondo

inizializza()
while True:
    basex-=VEL_AVANZ
    if basex<-20:
       basex=0
    principessa_vely+=1
    principessax+=1
    disegna_oggetti()
    aggiorna()
    




