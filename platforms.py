class Platform:
    def __init__(self, x, y, breedte, hoogte):
        self.x = x
        self.y = y
        self.breedte = breedte
        self.hoogte = hoogte

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.breedte, self.hoogte))
