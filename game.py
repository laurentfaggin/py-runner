import pygame
from sys import exit
from random import choice
from Player import Player
from Obstacle import Obstacle
from env import *
from screen import Screen
from music import Music

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.game_active = GAME_ACTIVE
        self.start_time = 0
        self.score = 0
        self.bg_music = Music(GAME_MUSIC_PATH, MUSIC_VOLUME)
        self.bg_music.play()
        self.player = Player()
        self.obstacle_group = pygame.sprite.Group()

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        score_surf = FONT.render(f'Score: {current_time}', False, SCORE_COLOR)
        score_rect = score_surf.get_rect(center = SCORE_POSITION)
        self.screen.screen.blit(score_surf, score_rect)
        return current_time
    
    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player, self.obstacle_group, False):
            self.obstacle_group.empty()
            return False
        else: return True

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.game_active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.player.rect.collidepoint(event.pos) and self.player.bottom >= 300:
                            self.player.gravity = -20
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and self.player.rect.bottom >= 300:
                            self.player.gravity = -20
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.game_active = True
                            self.start_time = int(pygame.time.get_ticks() / 1000)
                
                if self.game_active:
                    if event.type == self.obstacle_timer:
                        self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            
            if self.game_active:
                self.screen.draw_background()
                self.screen.screen.blit(self.player.image, self.player.rect)
                self.screen.draw_text(f'Score: {self.display_score()}', SCORE_COLOR, SCORE_POSITION)
                self.player.update()
                self.obstacle_group.draw(self.screen.screen)
                self.obstacle_group.update()
                self.game_active = self.collision_sprite()
            else:
                self.screen.draw_intro()

            pygame.display.update()
            self.clock.tick(FPS)