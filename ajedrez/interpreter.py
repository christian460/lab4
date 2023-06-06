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
  pieza()
  while True:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

def pieza():
  imagen=pygame.image.load('imagenes/rock.png')
  DISPLAY.blit(imagen,(0,0))




