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

# Puan veren top sınıfı
class Dot(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Dot, self).__init__()
		self.x = x
		self.y = y
		self.color = (255, 255, 255)
		self.win = win
		self.rect = pygame.draw.circle(win, self.color, (x, y), 6)
		

	def update(self, speed):
		self.x -= speed  # Noktayı sola kaydır
		if self.x <= 0:
			self.kill()  # Ekranı terk ettiyse sil

		# Noktayı tekrar çiz
		pygame.draw.circle(self.win, self.color, (self.x, self.y), 6)
		self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), 6)


class ScoreCard:
	def __init__(self, x, y, size, style, color, win):
		self.size = size
		self.color = color
		self.win = win
		self.inc = 1  # Yazı büyüklüğü animasyonu için
		self.animate = False  # Animasyon açık mı?

		self.style = style
		self.font = pygame.font.Font(self.style, self.size)
		self.image = self.font.render("0", True, self.color)
		self.rect = self.image.get_rect(center=(x, y))
		self.shadow_rect = self.image.get_rect(center=(x + 3, y + 3))

	def update(self, score):
		if self.animate:
			self.size += self.inc  # Yazıyı büyüt/küçült
			self.font = pygame.font.Font(self.style, self.size)
			if self.size <= 50 or self.size >= 60:
				self.inc *= -1
			if self.size == 50:
				self.animate = False  # Animasyon bitti

		self.image = self.font.render(f"{score}", False, self.color)
		shadow = self.font.render(f"{score}", True, (54, 69, 79))
		self.win.blit(shadow, self.shadow_rect)
		self.win.blit(self.image, self.rect)

class Message:
	def __init__(self, x, y, size, text, font, color, win):
		self.win = win
		if not font:
			self.font = pygame.font.SysFont("Verdana", size)
			anti_alias = True
		else:
			self.font = pygame.font.Font(font, size)
			anti_alias = False
		self.image = self.font.render(text, anti_alias, color)
		self.rect = self.image.get_rect(center=(x,y))
		self.shadow = self.font.render(text, anti_alias, (54,69,79))
		self.shadow_rect = self.image.get_rect(center=(x+2,y+2))
		
		
	def update(self):
		self.win.blit(self.shadow, self.shadow_rect)
		self.win.blit(self.image, self.rect)

# Patlama efekti 
class Particle(pygame.sprite.Sprite):
	def __init__(self, x, y, color, win):
		super(Particle, self).__init__()
		self.x = x
		self.y = y
		self.color = color
		self.win = win
		self.size = random.randint(4, 7)
		xr = (-3, 3)
		yr = (-3, 3)
		f = 2
		self.life = 40
		self.x_vel = random.randrange(xr[0], xr[1]) * f
		self.y_vel = random.randrange(yr[0], yr[1]) * f
		self.lifetime = 0
		

	def update(self):
		
		

