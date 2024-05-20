import pygame
from env import *

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)
        self.sky = pygame.image.load(CLOUD_PATH).convert()
        self.sky_reverse = pygame.transform.flip(self.sky, True, False)
        self.sky_x = 0
        self.ground = pygame.image.load(GROUND_PATH).convert()
        self.ground_reverse = pygame.transform.flip(self.ground, True, False)
        self.ground_x = 0

        self.player_stand = pygame.image.load(PLAYER_STAND_PATH).convert_alpha()
        self.player_stand_rect = self.player_stand.get_rect(center = (PLAYER_STAND_POSITION))

        self.game_name = FONT.render(GAME_NAME, False, GAME_NAME_COLOR)
        self.game_name_rect = self.game_name.get_rect(center = GAME_NAME_POSITION)

        self.game_message = FONT.render(GAME_START_MESSAGE, False, GAME_START_MESSAGE_COLOR)
        self.game_message_rect = self.game_message.get_rect(center = GAME_START_MESSAGE_POSITION)
    
    def draw_background(self):
        self.sky_x -= 0.5
        if self.sky_x <= -SCREEN_WIDTH:
            self.sky_x = 0
            self.screen.blit(self.sky, (self.sky_x, 0))
        else:
            self.screen.blit(self.sky_reverse, (self.sky_x + SCREEN_WIDTH, 0))
            self.screen.blit(self.sky, (self.sky_x, 0)) 

        self.ground_x -= 3
        if self.ground_x <= -SCREEN_WIDTH:
            self.ground_x = 0
            self.screen.blit(self.ground, (self.ground_x, 300))
        else:
            self.screen.blit(self.ground_reverse, (self.ground_x + SCREEN_WIDTH, 300))
            self.screen.blit(self.ground, (self.ground_x, 300))
       

    def draw_text(self, text, color, position):
        text_surface = FONT.render(text, False, color)
        text_rect = text_surface.get_rect(center = position)
        self.screen.blit(text_surface, text_rect)

    def draw_intro(self):
        self.screen.fill(INTRO_SCREEN_COLOR)
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.screen.blit(self.game_name, self.game_name_rect)
        self.screen.blit(self.game_message, self.game_message_rect)