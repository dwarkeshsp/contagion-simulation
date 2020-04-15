import pygame
import sys
import random
from person import Person

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

        if person.status == 'healthy':
            for other_person in people:
                if other_person is not person and other_person.status == 'sick':
                    if person.rect.colliderect(other_person.rect):
                        CONTRACT_PROB = random.randint(0, 100) / 100
                        if 0.05 > CONTRACT_PROB:
                            person.status = 'sick'

        if person.status == 'sick':
            person.days_sick += 0.05
            recovered = (person.days_sick + random.randint(0, 10)) / 100.0
            if 0.2 < recovered:
                person.status = 'immune'

        pygame.draw.rect(screen, person.color(), person.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)
