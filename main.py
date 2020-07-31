import pygame, pandas as pd
from Ship import *
from Asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h) 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)

df = pd.read.csv('game_info.csv')
#cole = df['AsteroidCount'] -- stores column 
#row = df.iloc['row number or row variable']  

NumLevels = df['LevelNum'].max()
Level = df['LevelNum'].min #stores 0()
LevelData = df.iloc['LevelNum'].min() #gives us the first row 
#LevelNum,AsteroidCount,PlayerX,PlayerY
#0,3,20,200
AsteroidCount = LevelData['AsteroidCount']
Player = Ship((LevelData['Playerx'], LevelData['Playery'])) 
#Obstacle = Asteroid
Asteroids = pygame.sprite.Group()

def init():
  LevelData = df.iloc[Level]
  Player = Ship((LevelData['Playerx'], LevelData['Playery'])) 
    AsteroidCount = LevelData['AsteroidCount']
    Asteroids.empty()
    for i in range[AsteroidCount]:
      Asteroids.add(Asteroid():

def main():
  global Level
  init()
  while Level <= NumLevels: 
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed [0] = 10
        if event.key == pygame.K_LEFT:
          Player.speed [0] = -10
        if event.key == pygame.K_UP:
           Player.speed [1] = -10
        if event.key == pygame.K_DOWN:
          Player.speed [1] = 10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
           Player.speed [0] = 0
        if event.key == pygame.K_LEFT:
           Player.speed [0] = 0
        if event.key == pygame.K_UP:
           Player.speed [1] = 0
        if event.key == pygame.K_DOWN:
           Player.speed [1] = 0  
    Asteroids.update()
    get_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
    Player.update()
    screen.fill(color)
    Asteroids.draw(screen)
    screen.blit(Player.image, Player.rect)
    #screen.blit(obstacle.image, obstacle.rect)
    pygame.display.flip()

    if Player.checkReset(800):
      if Level == NumLevels:
        break
      else:
        level += 1
      init()
    elif get_hit: 
      Player.reset((20, 200))


if __name__ == '__main__':
  main()   






