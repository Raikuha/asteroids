import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Prepare debris
            angle = random.uniform(20,50)
            frag_size = self.radius - ASTEROID_MIN_RADIUS

            frag_1 = Asteroid(self.position.x, self.position.y, frag_size)
            frag_2 = Asteroid(self.position.x, self.position.y, frag_size)
            frag_1.velocity = self.velocity.rotate(angle) * 1.2
            frag_2.velocity = self.velocity.rotate(-angle) * 1.2