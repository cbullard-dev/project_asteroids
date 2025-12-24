from circleshape import CircleShape
from constants import LINE_WIDTH, SHOOT_RADIUS
import pygame

class Shot(CircleShape):
  def __init__(self, x, y) -> None:
    super().__init__(x, y, SHOOT_RADIUS)
  
  def update(self, delta_time):
    self.position += self.velocity * delta_time
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)