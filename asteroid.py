import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  SPLIT_RANGE_MIN = 20
  SPLIT_RANGE_MAX = 50
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def update(self, delta_time):
    self.position += self.velocity * delta_time

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
  
  def split(self):
    self.kill()
    if self.radius < ASTEROID_MIN_RADIUS:
      return
    log_event("asteroid_split")
    range = random.uniform(self.SPLIT_RANGE_MIN, self.SPLIT_RANGE_MAX)
    asteroid_rotation_one = self.velocity.rotate(range)
    asteroid_rotation_two = self.velocity.rotate(-range)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid_one = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
    asteroid_two = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
    asteroid_one.velocity = asteroid_rotation_one * 1.2
    asteroid_two.velocity = asteroid_rotation_two * 1.2
