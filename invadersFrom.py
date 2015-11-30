#! /usr/bin/env python
import pygame 
import random


class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = pygame.image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

def Intersect(obj1_x, obj1_y, obj2_x, obj2_y):
	if (obj1_x > obj2_x - 16) and (obj1_x < obj2_x + 16) and (obj1_y > obj2_y - 16) and (obj1_y < obj2_y + 16):
		return 1
	else:
		return 0

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.key.set_repeat(1,1)
pygame.display.set_caption('data/Invaders From Py')
backdrop = pygame.image.load('data/backdrop.jpg')
run = 1
def main():
	enemies = []
	x = 0
	for count in range(10):
		enemies.append(Sprite(50 * x + 50, 50, 'data/enemy.png'))
		x += 1
	hero = Sprite(20, 400, 'data/hero.png')
	ourmissile = Sprite(0, 0, 'data/pMissile.png')
	enemymissile = Sprite(0, 480, 'data/ePlasma.png')
	score = 0
	quit = 0
	enemyspeed = 3

	while quit == 0:

		screen.blit(backdrop, (1, 1))
		white = (255, 255, 255)
		scoretxt = 'SCORE: %d' %score
		font = pygame.font.Font(None, 20)
		text = font.render(scoretxt, 1, white)
		screen.blit(text, (320,30))
		

		for count in range(len(enemies)):
			enemies[count].x += + enemyspeed
			enemies[count].render()

		if (enemies[len(enemies)-1].x > 590):
			enemyspeed = -3
			for count in range(len(enemies)):
				enemies[count].y += 5

		if enemies[0].x < 10:
			enemyspeed = 3
			for count in range(len(enemies)):
				enemies[count].y += 5

		if ourmissile.y < 479 and ourmissile.y > 0:
			ourmissile.render()
			ourmissile.y -= 5

		if ourmissile.y < 10:
			ourmissile.x =0
			ourmissile.y =0

		if enemymissile.y >= 480 and len(enemies) > 0:
			enemymissile.x = enemies[random.randint(0, len(enemies) - 1)].x
			enemymissile.y = enemies[0].y

		if Intersect(hero.x+16, hero.y+16, enemymissile.x, enemymissile.y):
			heroBang = Sprite(hero.x+16, hero.y+16, 'data/bang.png')
			heroBang.render()
			quit = 1

		for count in range(0, len(enemies)):
			if Intersect(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
				
				bang = Sprite(enemies[count].x,enemies[count].y, 'data/bang.png')
				bang.render()
				del enemies[count]
				score = score + 50
				ourmissile.x = 0
				ourmissile.y = 0
				break

		if len(enemies) == 0:				
			quit = 1
			

		for ourevent in pygame.event.get():
			if ourevent.type == pygame.QUIT:
				quit = 1
			if ourevent.type == pygame.KEYDOWN:
				if ourevent.key == pygame.K_RIGHT and hero.x < 590:
					hero.x += 5
				if ourevent.key == pygame.K_LEFT and hero.x > 10:
					hero.x -= 5
				if ourevent.key == pygame.K_UP and hero.y > 320:
					hero.y -= 5
				if ourevent.key == pygame.K_DOWN and hero.y < 440:
					hero.y += 5
				if ourevent.key == pygame.K_RETURN:
					if (ourmissile.y == 0):
						ourmissile.x = hero.x +20
						ourmissile.y = hero.y
				if ourevent.key == pygame.K_q:
					exit = 1
					return exit
			
		enemymissile.render()
		enemymissile.y += 5
		hero.render()
		pygame.display.update()
		pygame.time.delay(20)


if run==1:
	main()
