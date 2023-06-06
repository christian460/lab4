import pygame, sys
from pygame.locals import *
from colors import *
from chessPictures import *

DIMENCIONES=(640,480)
DISPLAY=pygame.display.set_mode(DIMENCIONES)
def parseLine(DISPLAY, y, s):
  x = 0
  for c in s:
    pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
    x += 1
def dibujarTab(screen,dimension):
  color=0
  for i in range(8):
    for j in range(8):
      x, y=i * dimension, j * dimension
      if color%2 == 0:
        pygame.draw.rect(screen,GRAY,[x,y,dimension,dimension],0)
      else:
        pygame.draw.rect(screen,LIGHTGRAY,[x,y,dimension,dimension],0)
      color+=1
    color+=1

def draw():
  pygame.init()
  
  dibujarTab(DISPLAY,60)
  piezas()
  while True:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

def piezas():
  #Insertar las torres
  imagen=pygame.image.load('imagenes/rock.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(0,0))
  DISPLAY.blit(imagen,(420,0))
  imagen=pygame.image.load('imagenes/rock_inv.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(0,420))
  DISPLAY.blit(imagen,(420,420))
  #Insertar los caballos
  imagen=pygame.image.load('imagenes/knight.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(60,0))
  DISPLAY.blit(imagen,(360,0))
  DISPLAY.blit(imagen,(60,420))
  DISPLAY.blit(imagen,(360,420))
  #Insertar los alfiles
  imagen=pygame.image.load('imagenes/pawn.png')
  imagen=pygame.transform.scale(imagen,(70,68))
  DISPLAY.blit(imagen,(114,0))
  DISPLAY.blit(imagen,(293,0))
  DISPLAY.blit(imagen,(114,420))
  DISPLAY.blit(imagen,(293,420))
  #nsertar las reinas
  imagen=pygame.image.load('imagenes/Queen.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(180,0))
  DISPLAY.blit(imagen,(180,420))
  #nsertar los reyes
  imagen=pygame.image.load('imagenes/king.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(240,0))
  DISPLAY.blit(imagen,(240,420))
  #insertar los peones
  imagen=pygame.image.load('imagenes/peon.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(0,60))
  DISPLAY.blit(imagen,(60,60))
  DISPLAY.blit(imagen,(120,60))
  DISPLAY.blit(imagen,(180,60))
  DISPLAY.blit(imagen,(240,60))
  DISPLAY.blit(imagen,(300,60))
  DISPLAY.blit(imagen,(360,60))
  DISPLAY.blit(imagen,(420,60))
  imagen=pygame.image.load('imagenes/peon_inv.png')
  imagen=pygame.transform.scale(imagen,(60,60))
  DISPLAY.blit(imagen,(0,360))
  DISPLAY.blit(imagen,(60,360))
  DISPLAY.blit(imagen,(120,360))
  DISPLAY.blit(imagen,(180,360))
  DISPLAY.blit(imagen,(240,360))
  DISPLAY.blit(imagen,(300,360))
  DISPLAY.blit(imagen,(360,360))
  DISPLAY.blit(imagen,(420,360))







