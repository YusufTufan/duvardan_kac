import pygame
import random

from objects import Bar, Dot, Player, Message, Particle, ScoreCard, Button

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 30

# Arka planlar yükleniyor
bg = pygame.image.load('Assets/bg4.jpg')
bg = pygame.transform.scale(bg, SCREEN)

frame_height = 150
frame = pygame.image.load('Assets/bg3.jpg')
frame = pygame.transform.scale(frame, (WIDTH - 10, frame_height))
frameX, frameY = 5, HEIGHT // 2 - frame_height // 2

# Renkler
BLACK = (0, 0, 32)
WHITE = (255, 255, 255)

# Ses dosyaları
score_fx = pygame.mixer.Sound('Sounds/point.mp3')
dead_fx = pygame.mixer.Sound('Sounds/dead.mp3')
score_page_fx = pygame.mixer.Sound('Sounds/score_page.mp3')
pygame.mixer.music.load('Sounds/Chill Gaming.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

# FONTS 

score_font = "Fonts/EvilEmpire-4BBVK.ttf"
final_score_font = "Fonts/ghostclanital.ttf"
title_font = "Fonts/dpcomic.ttf"

# Messages

dodgy = Message(WIDTH//2, HEIGHT//3, 80, "Dodgy", title_font, WHITE, win)
walls = Message(WIDTH//2, HEIGHT//2, 60, "Walls", title_font, WHITE, win)
tap_to_play = Message(WIDTH//2, HEIGHT-100, 20, "Tap To Play", None, WHITE, win)
new_high =  Message(WIDTH//2, 240, 20, "NEW HIGH", None, WHITE, win)

# Buton resimleri
home_img = pygame.image.load('Assets/homeBtn.png')
replay_img = pygame.image.load('Assets/replay.png')
sound_off_img = pygame.image.load("Assets/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/soundOnBtn.png")

# Buton nesneleri
home_btn = Button(home_img, (36, 36), WIDTH // 4 - 18, 320)
replay_btn = Button(replay_img, (44, 44), WIDTH // 2 - 18, 315)
sound_btn = Button(sound_on_img, (36, 36), WIDTH - WIDTH // 4 - 18, 320)

# Sprite grupları
bar_group = pygame.sprite.Group()
dot_group = pygame.sprite.Group()
particle_group = pygame.sprite.Group()

# Skor kartı
score_msg = ScoreCard(WIDTH//2, 100, 50, score_font, WHITE, win)

# Oyuncu
p = Player(win)

#Oyun Degiskenleri
bar_frequency = 1400
bar_heights = [height for height in range(60,100,10)]
bar_speed = 3
pos = -1
pos_updater = 1
start_time = pygame.time.get_ticks()

clicked = False
score = 0
highscore = 0
player_alive = True
sound_on = True

home_page = True
game_page = False
score_page = False
