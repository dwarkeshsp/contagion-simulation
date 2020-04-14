import pygame
import sys
import random


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 6, 6)
        self.rect.center = (x, y)
        self.dx = dx
        self.dy = dy


people = []

clock = pygame.time.Clock()
CENTER = 500


pygame.init()
pygame.display.set_caption('Memetic Evolution Simulation')
screen = pygame.display.set_mode((1000, 1000), 0, 32)


def random_speed():
    return random.randint(0, 20) / 10 - 1


def gravity(x):
    gravity = (CENTER - x) ** 2 / 100000.0
    if x > CENTER:
        gravity *= -1
    print(gravity)
    return gravity


running = True

while running:
    screen.fill((0, 0, 0))
    # border = pygame.draw.rect(screen, (125, 125, 125),
    #                           (250, 250, 500, 500), 3)

    people.append(Person(CENTER, CENTER, random_speed(), random_speed()))

    for person in people:
        person.rect.x += person.dx
        person.rect.y += person.dy
        # if person.rect.x >= 750 or person.rect.x <= 250 or person.rect.y >= 750 or person.rect.y <= 250:
        #     person.dx *= - 1
        #     person.dy *= - 1
        # else:
        person.dx += random_speed() + gravity(person.rect.x)
        person.dy += random_speed() + gravity(person.rect.y)
        pygame.draw.rect(screen, (255, 255, 255),
                         person.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
