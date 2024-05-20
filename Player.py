import pygame
from random import randint
from env import *
from music import Music

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load(PLAYER_WALK1_PATH).convert_alpha()
        player_walk2 = pygame.image.load(PLAYER_WALK2_PATH).convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load(PLAYER_JUMP_PATH).convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = PLAYER_GAME_POSITION)
        self.gravity = GRAVITY

        self.jump_sound = Music(JUMP_SOUND_PATH, MUSIC_VOLUME)
       
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play(0)
        if keys[pygame.K_RIGHT] and self.rect.right <= SCREEN_WIDTH:
            self.rect.x += 5
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()