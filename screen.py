import pygame
import ast
from dotenv import load_dotenv
import os

load_dotenv()

pygame.init()

SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH'))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT'))
WINDOW_TITLE = os.getenv('WINDOW_TITLE')
CLOUD_PATH = os.getenv('CLOUD_PATH')
GROUND_PATH = os.getenv('GROUND_PATH')
PLAYER_STAND_PATH = os.getenv('PLAYER_STAND_PATH')
PLAYER_STAND_POSITION = tuple(int(i) for i in os.getenv('PLAYER_STAND_POSITION').strip('()').split(','))
GAME_NAME = os.getenv('GAME_NAME')
GAME_NAME_COLOR = ast.literal_eval(os.getenv('GAME_NAME_COLOR'))
GAME_NAME_POSITION = tuple(int(i) for i in os.getenv('GAME_NAME_POSITION').strip('()').split(','))
GAME_START_MESSAGE = os.getenv('GAME_START_MESSAGE')
print(os.getenv('GAME_START_MESSAGE_COLOR'))
GAME_START_MESSAGE_COLOR = ast.literal_eval(os.getenv('GAME_START_MESSAGE_COLOR'))
GAME_START_MESSAGE_POSITION = tuple(int(i) for i in os.getenv('GAME_START_MESSAGE_POSITION').strip('()').split(','))
INTRO_SCREEN_COLOR = ast.literal_eval(os.getenv('INTRO_SCREEN_COLOR'))
script_dir = os.path.dirname(os.path.realpath(__file__))
FONT_PATH = os.getenv('FONT_PATH')
FONT_SIZE = int(os.getenv('FONT_SIZE'))
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.sky = pygame.image.load(CLOUD_PATH).convert()
        self.sky_reverse = pygame.transform.flip(self.sky, True, False)
        self.sky_x = 0
        self.sky_x2 = SCREEN_WIDTH
        self.ground = pygame.image.load(GROUND_PATH).convert()
        self.ground_reverse = pygame.transform.flip(self.ground, True, False)
        self.ground_x = 0
        self.ground_x2 = SCREEN_WIDTH

        self.player_stand = pygame.image.load(PLAYER_STAND_PATH).convert_alpha()
        self.player_stand_rect = self.player_stand.get_rect(center = (PLAYER_STAND_POSITION))

        self.game_name = FONT.render(GAME_NAME, False, GAME_NAME_COLOR)
        self.game_name_rect = self.game_name.get_rect(center = GAME_NAME_POSITION)

        self.game_message = FONT.render(GAME_START_MESSAGE, False, GAME_START_MESSAGE_COLOR)
        self.game_message_rect = self.game_message.get_rect(center = GAME_START_MESSAGE_POSITION)
    
    def draw_background(self):
        self.sky_x -= 0.5
        self.sky_x2 -= 0.5
        if self.sky_x <= -SCREEN_WIDTH:
            self.sky_x = self.sky_x2 + SCREEN_WIDTH
        if self.sky_x2 <= -SCREEN_WIDTH:
            self.sky_x2 = self.sky_x + SCREEN_WIDTH
        self.screen.blit(self.sky, (self.sky_x, 0)) 
        self.screen.blit(self.sky_reverse, (self.sky_x2, 0))

        self.ground_x -= 2.5
        self.ground_x2 -= 2.5
        if self.ground_x <= -SCREEN_WIDTH:
            self.ground_x = self.ground_x2 + SCREEN_WIDTH
        if self.ground_x2 <= -SCREEN_WIDTH:
            self.ground_x2 = self.ground_x + SCREEN_WIDTH
        self.screen.blit(self.ground, (self.ground_x, 300))
        self.screen.blit(self.ground_reverse, (self.ground_x2, 300))

    def modify_background(self, path):
        self.ground = pygame.image.load(path).convert()
        self.ground_reverse = pygame.transform.flip(self.ground, True, False)

    def draw_text(self, text, color, position):
        text_surface = FONT.render(text, False, color)
        text_rect = text_surface.get_rect(center = position)
        self.screen.blit(text_surface, text_rect)

    def draw_intro(self):
        self.screen.fill(INTRO_SCREEN_COLOR)
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.screen.blit(self.game_name, self.game_name_rect)
        self.screen.blit(self.game_message, self.game_message_rect)
        
    def draw_change_level(self, level):
        self.screen.fill(INTRO_SCREEN_COLOR)
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.draw_text(f'Level {level}', GAME_NAME_COLOR, GAME_NAME_POSITION)
        self.draw_text('Get Ready!', GAME_START_MESSAGE_COLOR, GAME_START_MESSAGE_POSITION)
        pygame.display.update()