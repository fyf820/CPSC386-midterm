from vector import Vector
import pygame

class Ship:
 def __init__(self,game,vector = Vector()):
     self.game = geme
     self.screen = geme.screen
     self.velocity = vector
     self.screen_rect = geme.screen.get_rect()
     self.image = pygame.image.load("ship.png")
     self.rect = self.image.get_rect()
     self.rect.midbottom = self.screen_rect.midbottom
     # initialize the laser group.

 def center_ship(self):
     self.rect.midbottom = self.screen_rect.midbottom

 def fire(self):
     pass
     # create laser instance
     # add laser into self

 def remove_lasers(self):
     pass
     # remove laser

 def move(self):
    if self.velocity == Vector():
        return
    self.rect.left += self.velocity.x
    self.rect.top += self.velocity.y
     # limit ship in screen

 def draw(self):
     self.screen.blit(self.image, self.rect)

 def update(self):
     #create fleet instance
     self.move()
     self.draw()
    #for laser in laser group:
         # update laser
    #for laser in lasers copy:
         #if the bottom of laser is out of top
             #remove laser
     pygame.sprite.groupcollide(self.laser, fleet.aliens, True, True)
     if not fleet.aliens:
         self.game.restart()