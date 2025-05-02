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
