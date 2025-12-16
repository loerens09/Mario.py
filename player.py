import pygame
from settings import PLAYER_SNELHEID, GRAVITY, SPRING_KRACHT, HOOGTE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snelheid = PLAYER_SNELHEID

        # Beweging
        self.vel_y = 0
        self.is_jumping = False
        self.on_ground = False

        # ANIMATIES (idle + jump)
        self.animations = {
            "idle": [
                pygame.image.load("assets/Mario.png").convert_alpha()
            ],
            "jump": [
                pygame.image.load("assets/jumpM.png").convert_alpha(),
                
            ]
        }

        # Sprite grootte
        self.sprite_size = 75

        # Alle animaties schalen
        for key in self.animations:
            self.animations[key] = [
                pygame.transform.scale(img, (self.sprite_size, self.sprite_size))
                for img in self.animations[key]
            ]

        # Animatie instellingen
        self.current_animation = "idle"
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][0]

        # Hitbox (zelfde als sprite)
        self.width = self.sprite_size - 16
        self.height = self.sprite_size - 12

    def update(self, keys, platforms):
        
        # LINKS / RECHTS
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.snelheid
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.snelheid

        # SPRINGEN
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = SPRING_KRACHT
            self.is_jumping = True
            self.on_ground = False

        # ZWAARTEKRACHT
        self.vel_y += GRAVITY
        self.y += self.vel_y

        
        # GROND COLLISION (EERST!)
        if self.y + self.height >= HOOGTE:
            self.y = HOOGTE - self.height
            self.vel_y = 0
            self.is_jumping = False
            self.on_ground = True
            return  


        # PLATFORM COLLISION
        self.on_ground = False
        for plat in platforms:
            if self.vel_y >= 0 and \
               self.y + self.height <= plat.y + 10 and \
               self.y + self.height + self.vel_y >= plat.y and \
               self.x + self.width > plat.x and \
               self.x < plat.x + plat.breedte:
                self.y = plat.y - self.height
                self.vel_y = 0
                self.is_jumping = False
                self.on_ground = True
                break

        # GROND COLLISION
        if self.y + self.height >= HOOGTE:
            self.y = HOOGTE - self.height
            self.vel_y = 0
            self.is_jumping = False
            self.on_ground = True

        # ANIMATIE KIEZEN
        if self.is_jumping:
            self.current_animation = "jump"
        else:
            self.current_animation = "idle"

        # ANIMATIE UPDATEN
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.current_animation]):
            self.frame_index = 0

        self.image = self.animations[self.current_animation][int(self.frame_index)]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
