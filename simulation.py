import pygame
import sys
import random

CENTER = 500


class Person(pygame.sprite.Sprite):
    def __init__(self, status):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 5, 5)

        def random_location():
            return random.randint(0, 200) - 100 + CENTER

        self.rect.center = (random_location(), random_location())
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
                    if 0.03 > random.randint(0, 100) / 100:
                        self.status = 'sick'

        pygame.draw.rect(screen, self.color(), self.rect)

    def color(self):
        if self.status == 'healthy':
            return (255, 255, 255)
        if self.status == 'sick':
            return (255, 255, 0)
        else:
            return None


people = []
people.append(Person(status='sick'))
for i in range(250):
    people.append(Person(status='healthy'))

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('COVID Simulation')
screen = pygame.display.set_mode((1000, 1000), 0, 32)


running = True

while running:
    screen.fill((0, 0, 0))

    for person in people:
        person.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)
