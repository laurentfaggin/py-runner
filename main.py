import pygame
from sys import exit
from random import randint, choice
from Player import Player
from Obstacle import Obstacle
from env import *
from screen import Screen
from game import Game

pygame.init()
game = Game()
game.game_loop()