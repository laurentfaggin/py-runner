import pygame
from env import *

class Music:
    def __init__(self, music_path, volume):
        self.music = pygame.mixer.Sound(music_path)
        self.music.set_volume(volume)
    
    def play(self,loops=-1):
        self.music.play(loops)
    
    def stop(self):
        self.music.stop()
        