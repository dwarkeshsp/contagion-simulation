import random
import pygame


CENTER = 500


class Person(pygame.sprite.Sprite):
    def __init__(self, status):

        def random_location():
            return random.randint(0, 300) - 150 + CENTER

        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (random_location(), random_location())
        self.status = status
        self.days_sick = 0
        self.dx = 0
        self.dy = 0

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(x):
            gravity = (CENTER - x) ** 2 / 100000
            if x > CENTER:
                gravity *= -1
            return gravity

        self.dx += random_speed() + gravity(self.rect.x)
        self.dy += random_speed() + gravity(self.rect.y)

        DECELERATION = 0.99
        self.dx *= DECELERATION
        self.dy *= DECELERATION

    def color(self):
        if self.status == 'healthy':
            return (255, 255, 255)
        if self.status == 'sick':
            return (255, 69, 0)
        if self.status == 'immune':
            return (0, 100, 255)
