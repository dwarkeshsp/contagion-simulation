import pygame
import random
from person import Person
from plotter import plot

POPULATION = 500
INITIAL_SICK = 5

CONTAGIOUSNESS = 0.05
AVG_RECOVERY_TIME = 14

people = []
for _ in range(INITIAL_SICK):
    people.append(Person(status='sick'))
for _ in range(POPULATION - INITIAL_SICK):
    people.append(Person(status='healthy'))

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Contagion Simulation')
screen = pygame.display.set_mode((1000, 1000), 0, 32)
graph_button = pygame.Rect(800, 800, 140, 50)
graph_button_text = pygame.font.SysFont(
    'manjari', 50).render('Graph', True, (255, 255, 255))

data = [[], [], []]
i = 0

running = True
graphed = False

while running:

    screen.fill((0, 0, 0))

    for ray in data:
        ray.append(0)

    for person in people:
        person.move()

        if person.status == 'sick':
            data[0][i] += 1

            for other_person in people:
                if other_person.status == 'healthy' and person.rect.colliderect(other_person.rect):
                    CONTRACT_PROB = random.randint(0, 100) / 100
                    if CONTAGIOUSNESS > CONTRACT_PROB:
                        other_person.status = 'sick'

            person.days_sick += 1
            RECOVERY_PROB = (person.days_sick + random.randint(0, 10) - 5) / 10
            if AVG_RECOVERY_TIME < RECOVERY_PROB:
                person.status = 'immune'

        if person.status == 'immune':
            data[1][i] += 1

        if person.status == 'healthy':
            data[2][i] += 1

        pygame.draw.rect(screen, person.color(), person.rect)

    if data[0][i] == 0 and not graphed:
        plot(data)
        graphed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)

    i += 1
