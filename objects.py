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
		if show_player:
			self.rect.y += self.dy  # Aşağı/yukarı hareket

			if clicked:
				# Oyuncu sınırlar içinde mi diye kontrol
				if self.frame_top < self.rect.y < self.frame_bottom:
					self.dy *= -1  # Hareket yönünü değiştir
					flip_fx.play()

			# Alt sınıra çarptıysa
			if self.rect.bottom >= self.frame_bottom:
				self.dy *= -1
				self.rect.bottom = self.frame_bottom - 1
				dash_fx.play()

			# Üst sınıra çarptıysa
			if self.rect.top <= self.frame_top:
				self.dy *= -1
				self.rect.top = self.frame_top + 1
				dash_fx.play()

			# Oyuncuyu ekrana çiz
			self.win.blit(self.image, self.rect)

	# Oyuncuyu başlangıç konumuna getir
	def reset(self):
		self.x = 145
		self.y = 270
		self.rect = self.image.get_rect(center=(self.x,self.y))

class Bar(pygame.sprite.Sprite):
	def __init__(self, x, y, height, color, win):
		super(Bar, self).__init__()
		
		self.rect = pygame.Rect(x, y, 20, height, border_radius = 8)
		self.win = win
		self.color = color
		
	def update(self, speed):
		self.rect.x -= speed
		if self.rect.x <= 0:
			self.kill()
		self.win.fill(self.color, self.rect)
