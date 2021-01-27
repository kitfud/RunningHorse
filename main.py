import pygame
from pygame.locals import *
from sprite_loader import *
from player import *


horse_images = {}

pygame.init()
#background
background = pygame.image.load('worldmap.png')


screen_info = pygame.display.Info()

size = (width,height)= (screen_info.current_w,screen_info.current_h)
#resizing the background
background = pygame.transform.smoothscale(background,(size))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (0,0,0)

def get_images():
  directions = ['n','e','s','w']
  horse_sheet = SpriteSheet('horse.png')
  for i in range(len(directions)):
    for j in range(3):
      horse_images[directions[i]+str(j)]= horse_sheet.get_image(j*64,i*85,64,85)



def main():
  get_images()
  print(horse_images)
  player = Player((width//2,height//2),horse_images)
  
  while True:
    screen.blit(background,(0,0))
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    keys = pygame.key.get_pressed()
    
    if keys[K_UP]:
      player.up()
    if keys[K_DOWN]:
      player.down()
    if keys[K_LEFT]:
      player.left()
    if keys[K_RIGHT]:
      player.right()

    player.update()
    #screen.fill(color)
    player.draw(screen)
    pygame.display.flip()

if __name__ == '__main__':
  main()