import os
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

# Fontlar
score_font = "Fonts/EvilEmpire-4BBVK.ttf"
final_score_font = "Fonts/ghostclanital.ttf"
title_font = "Fonts/dpcomic.ttf"

# Başlangıç ekranı mesajları
dodgy = Message(WIDTH//2, HEIGHT//3, 80, "Dodgy", title_font, WHITE, win)
walls = Message(WIDTH//2, HEIGHT//2, 60, "Walls", title_font, WHITE, win)
tap_to_play = Message(WIDTH//2, HEIGHT - 100, 20, "Tap To Play", None, WHITE, win)
new_high = Message(WIDTH//2, 240, 20, "NEW HIGH", None, WHITE, win)

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

# Oyun değişkenleri
bar_frequency = 1400
bar_heights = [h for h in range(60, 100, 10)]
bar_speed = 3
pos = -1
clicked = False
score = 0
highscore = 0
player_alive = True
sound_on = True

# Sayfa kontrolleri
home_page = True
game_page = False
score_page = False

# Ana döngü
running = True
start_time = pygame.time.get_ticks()

while running:
    clicked = False
    win.blit(bg, (0, 0))

    # Olay kontrolleri
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_page:
                home_page = False
                game_page = True
                score_page = False
                score = 0
                bar_speed = 3
                player_alive = True
                p = Player(win)
                start_time = pygame.time.get_ticks()
            elif game_page:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    # Ana menü
    if home_page:
        dodgy.update()
        walls.update()
        tap_to_play.update()

    # Skor ekranı
    if score_page:
        final_score.update()
        if score and score >= highscore:
            new_high.update()

        if home_btn.draw(win):
            home_page = True
            score_page = False
            game_page = False

        if replay_btn.draw(win):
            home_page = False
            game_page = True
            score_page = False
            score = 0
            bar_speed = 3
            player_alive = True
            p = Player(win)
            start_time = pygame.time.get_ticks()

        if sound_btn.draw(win):
            sound_on = not sound_on
            if sound_on:
                sound_btn.update_image(sound_on_img)
                pygame.mixer.music.play(loops=-1)
            else:
                sound_btn.update_image(sound_off_img)
                pygame.mixer.music.stop()

    # Oyun ekranı
    if game_page:
        win.blit(frame, (frameX, frameY))
        if player_alive:
            current_time = pygame.time.get_ticks()
            if current_time - start_time >= bar_frequency:
                bar_height = random.choice(bar_heights)
                pos *= -1

                if pos == -1:
                    bar_y = frameY
                    dot_y = frameY + bar_height + 20
                else:
                    bar_y = frameY + frame_height - bar_height
                    dot_y = frameY + frame_height - bar_height - 20

                bar = Bar(WIDTH, bar_y, bar_height, BLACK, win)
                dot = Dot(WIDTH + 10, dot_y, win)
                bar_group.add(bar)
                dot_group.add(dot)
                start_time = current_time

            for dot in dot_group:
                if dot.rect.colliderect(p):
                    dot.kill()
                    score += 1
                    if score >= highscore:
                        highscore = score
                    score_fx.play()
                    score_msg.animate = True

            if pygame.sprite.spritecollide(p, bar_group, False):
                x, y = p.rect.center
                for _ in range(10):
                    particle = Particle(x, y, WHITE, win)
                    particle_group.add(particle)
                player_alive = False
                dead_fx.play()
                bar_speed = 0

        bar_group.update(bar_speed)
        dot_group.update(bar_speed)
        p.update(player_alive, clicked)
        score_msg.update(score)
        particle_group.update()

        # Oyuncu öldüyse skor ekranına geç
        if not player_alive and len(particle_group) == 0:
            score_page = True
            game_page = False
            bar_group.empty()
            dot_group.empty()
            final_score = Message(WIDTH//2, 150, 100, f"{score}", score_font, WHITE, win)
            score_page_fx.play()

    # Kenar çerçevesi
    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 5, border_radius=10)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
