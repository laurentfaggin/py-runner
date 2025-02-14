import pygame
import time
from sys import exit
from random import choice
from Player import Player
from Obstacle import Obstacle
from screen import Screen
from music import Music
from dotenv import load_dotenv

import os

load_dotenv()
pygame.init()

GAME_ACTIVE = os.getenv('GAME_ACTIVE')
FPS = int(os.getenv('FPS'))
FONT_PATH = os.getenv('FONT_PATH')
FONT_SIZE = int(os.getenv('FONT_SIZE'))
SCORE_COLOR = tuple(map(int, os.getenv('SCORE_COLOR').strip("()").split(',')))
SCORE_POSITION = tuple(int(i) for i in os.getenv('SCORE_POSITION').strip('()').split(','))
GAME_MUSIC_PATH = os.getenv('GAME_MUSIC_PATH')
MUSIC_VOLUME = float(os.getenv('MUSIC_VOLUME'))
FONT = os.getenv('FONT')

class Game:
    def __init__(self):
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.game_active = GAME_ACTIVE
        self.start_time = 0
        self.level_start_time = 0
        self.level = 1
        self.score = 0
        self.bg_music = Music(GAME_MUSIC_PATH, MUSIC_VOLUME)
        self.bg_music.play()
        self.player = Player()
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_speed = 6
        self.changeLevel = False
        global FONT
        FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)
        self.obstacle_timer = pygame.USEREVENT + 1
        self.score_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.obstacle_timer, 1500)
        pygame.time.set_timer(self.score_timer, 1000)

    def display_score(self):
        score_surf = FONT.render(f'Score: {self.score}', False, SCORE_COLOR)
        score_rect = score_surf.get_rect(center = SCORE_POSITION)
        self.screen.screen.blit(score_surf, score_rect)
        return self.score
    
    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player, self.obstacle_group, False):
            self.obstacle_group.empty()
            self.score = 0
            self.level = 1
            return False
        else: return True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if self.game_active and not self.changeLevel:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.player.rect.collidepoint(event.pos) and self.player.bottom >= 300:
                    self.player.gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.rect.bottom >= 300:
                    self.player.gravity = -20
            
            if event.type == self.obstacle_timer:
                self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

            if event.type == self.score_timer:
                self.score += 1
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game_active = True
                self.player.reset_position()
    
    def handleChange_level(self):
        self.changeLevel = True
        self.screen.draw_change_level(self.level)
        pygame.display.update()
        pygame.time.delay(2000)
        self.changeLevel = False
        self.player.reset_position()
        self.obstacle_group.empty()
        self.obstacle_speed += 2
    
    def handle_level(self):
        if self.changeLevel:
            return
        else:
            self.score = self.display_score()
            if self.score < 10:
                self.screen.modify_background(os.getenv('GROUND_PATH'))                
                self.level = 1
            elif self.score < 20:
                if self.level != 2:
                    self.level = 2
                    self.handleChange_level()                    
                self.screen.modify_background(os.getenv('GROUND2_PATH'))
            elif self.score < 30:
                if self.level != 3:
                    self.level = 3                    
                    self.handleChange_level()
                self.screen.modify_background(os.getenv('GROUND3_PATH'))
            elif self.score >= 30:
                if self.level != 4:
                    self.level = 4
                    self.handleChange_level()
                self.screen.modify_background(os.getenv('GROUND4_PATH'))

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)                
            
            if self.game_active:
                if not self.changeLevel:
                    self.handle_level()
                    self.screen.draw_background()
                    self.screen.screen.blit(self.player.image, self.player.rect)
                    self.display_score()
                    self.screen.draw_text(f'Score: {self.display_score()}', SCORE_COLOR, SCORE_POSITION)
                    self.player.update()
                    self.obstacle_group.draw(self.screen.screen)
                    self.obstacle_group.update()
                    self.game_active = self.collision_sprite()
            else:
                self.screen.draw_intro()

            pygame.display.update()
            self.clock.tick(FPS)