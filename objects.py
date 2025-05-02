import pygame
import random

# Ekran boyutunu tanımlıyoruz (ana dosyadaki ile aynı)
SCREEN = WIDTH, HEIGHT = 288, 512

# Pygame için gerekli modülleri başlatıyoruz
pygame.font.init()
pygame.mixer.init()

# Ses efektleri
dash_fx = pygame.mixer.Sound('Sounds/dash.mp3')  # Duvara çarpınca çıkan ses
flip_fx = pygame.mixer.Sound('Sounds/flip.mp3')  # Yön değiştirince çıkan ses

# Oyuncuyu temsil eden sınıf
class Player:
	def __init__(self, win):
		self.win = win  # Çizim yapılacak yüzey
		self.image = pygame.image.load('Assets/rect.png')  # Oyuncunun görseli
		self.image = pygame.transform.scale(self.image, (16,16))  # Küçültüyoruz
		self.reset()  # Başlangıç pozisyonu

		self.dy = 4  # Y eksenindeki hareket miktarı
		self.frame_top = HEIGHT//2 - 75  # Üst sınır
		self.frame_bottom = HEIGHT//2 + 75  # Alt sınır
	# Oyuncuyu ekranda güncelleyen fonksiyon
	def update(self, show_player, clicked):
		

	# Oyuncuyu başlangıç konumuna getir
	def reset(self):
	
