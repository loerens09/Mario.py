import pygame
from settings import *
from player import Player
from platforms import Platform

# lijst met platforms
platforms = [
    Platform(0, 350, 800, 50),    # grond
    Platform(200, 280, 100, 20),  # platform 1
    Platform(400, 220, 150, 20)   # platform 2
]

pygame.init()
screen = pygame.display.set_mode((BREEDTE, HOOGTE))
clock = pygame.time.Clock()

player = Player(100, HOOGTE -64)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys, platforms)  # platforms meegeven aan update

    screen.fill(BLAUW)
    player.draw(screen)
    for platform in platforms:
        platform.draw(screen)
    pygame.display.flip()

pygame.quit()