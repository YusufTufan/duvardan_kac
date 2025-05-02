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
