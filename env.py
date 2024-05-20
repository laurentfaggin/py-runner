import pygame

pygame.init()

FPS = 60

# screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# screen display
INTRO_SCREEN_COLOR = (94, 129, 162)
GAME_NAME = 'Pixel Runner'
GAME_NAME_COLOR = (111, 196, 169)
GAME_NAME_POSITION = (400, 80)
GAME_START_MESSAGE = 'Press space to run'
GAME_START_MESSAGE_COLOR = GAME_NAME_COLOR
GAME_START_MESSAGE_POSITION = (400, 320)
WINDOW_TITLE = 'Runner'

#BACKGROUND
SKY_PATH = 'graphics/Sky.png'
SKY_POSITION = (0, 0)
CLOUD_PATH = 'graphics/cloud.png'
GROUND_PATH = 'graphics/beach.png'
GROUND_POSITION = (0, 300)

# music
GAME_MUSIC_PATH = 'audio/music.wav'
JUMP_SOUND_PATH = 'audio/jump.mp3'
MUSIC_VOLUME = 0.3

# font
FONT_PATH = 'font/Pixeltype.ttf'
FONT_SIZE = 50
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)

# game
GAME_NAME = 'Pixel Runner'
GAME_COLOR = (111, 196, 169)
GAME_START_MESSAGE = 'Press space to run'
GAME_START_MESSAGE_COLOR = GAME_COLOR
GAME_ACTIVE = False

#player
PLAYER_STAND_PATH = 'graphics/Player/player_stand.png'
PLAYER_STAND_POSITION = (200, 300)
PLAYER_GAME_POSITION = (80, 300)
PLAYER_WALK1_PATH = 'graphics/Player/player_walk_1.png'
PLAYER_WALK2_PATH = 'graphics/Player/player_walk_2.png'
PLAYER_JUMP_PATH = 'graphics/Player/jump.png'
GRAVITY = 0

#score
SCORE_POSITION = (400, 50)
SCORE_COLOR = (64, 64, 64)


