import pygame
import sys
import random


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, status):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (x, y)
        self.status = status
        self.dx = 0
        self.dy = 0

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(x):
            gravity = (CENTER - x) ** 2 / 5000.0
            if x > CENTER:
                gravity *= -1
            return gravity

        self.dx += random_speed() + gravity(self.rect.x)
        self.dy += random_speed() + gravity(self.rect.y)

        if self.status != 'sick':
            for person in people:
                if person.status == 'sick' and self.rect.colliderect(person.rect):
                    print('detected')
                    self.status == 'sick'

        pygame.draw.rect(screen, self.color(), self.rect)

    def color(self):
        if self.status == 'healthy':
            return (255, 255, 255)
        if self.status == 'sick':
            return (255, 255, 0)
        else:
            return None


CENTER = 500

people = []
people.append(Person(CENTER, CENTER, status='sick'))

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Memetic Evolution Simulation')
screen = pygame.display.set_mode((1000, 1000), 0, 32)


running = True

while running:
    screen.fill((0, 0, 0))
    if len(people) < 100:
        people.append(Person(CENTER, CENTER, status='healthy'))

    for person in people:
        person.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(100)
