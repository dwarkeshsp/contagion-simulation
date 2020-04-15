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
        self.days_sick = 0.0
        self.dx = 0
        self.dy = 0

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(x):
            gravity = (CENTER - x) ** 2 / 100000.0
            if x > CENTER:
                gravity *= -1
            return gravity

        DECELERATION = 0.99
        self.dx *= DECELERATION
        self.dy *= DECELERATION

        self.dx += random_speed() + gravity(self.rect.x)
        self.dy += random_speed() + gravity(self.rect.y)

        if self.status != 'sick':
            for person in people:
                if person.status == 'sick' and self.rect.colliderect(person.rect):
                    if 0.05 > random.randint(0, 100) / 100:
                        self.status = 'sick'

        if self.status == 'sick':
            self.days_sick += 0.05
            recovered = (self.days_sick + random.randint(0, 10)) / 100.0
            if 0.2 < recovered:
                self.status = 'immune'

        pygame.draw.rect(screen, self.color(), self.rect)

    def color(self):
        if self.status == 'healthy':
            return (255, 255, 255)
        if self.status == 'sick':
            return (255, 255, 0)
        if self.status == 'immune':
            return (255, 20, 147)


people = []
for _ in range(5):
    people.append(Person(status='sick'))
for _ in range(250):
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
