from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
   
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity1 = self.position.rotate(split_angle)
        velocity2 = self.position.rotate(-split_angle)

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity1 * 0.8
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity2 * 0.8

        

