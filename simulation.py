import pygame
import sys
import random


class Person:
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y


people = []

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 1000), 0, 32)


def random_speed():
    return random.randint(0, 20) / 10 - 1


running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (125, 125, 125), (500, 500), 250)

    people.append(Person(500, 500, random_speed(), random_speed()))

    for person in people:
        person.x += person.speed_x
        person.y += person.speed_y
        person.speed_x += random_speed()
        person.speed_y += random_speed()

        pygame.draw.circle(screen, (255, 255, 255),
                           (int(person.x), int(person.y)), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
