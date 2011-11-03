import pygame, sys, random
from pygame.locals import *

BRIGHT = 255
MEDIUM = 155
DIM = 55
BLACK = (0,0,0)

FPS = 50

clock = pygame.time.Clock()

class Starfield():
	def __init__(self,screen,num_stars,width,height):
		self.screen = screen
		self.num_stars = num_stars
		self.star = []
		for i in range(num_stars):
			max_bright = random.randint(1,254)
			self.star.append([random.randint(0,width),random.randint(0,height),1,random.randint(1,max_bright),max_bright,0])
			
	
	def update(self):
		#self.screen.fill(BLACK)
		for i in range (self.num_stars):		
			pygame.draw.rect(self.screen,(self.star[i][3],self.star[i][3],self.star[i][3]),((self.star[i][0],self.star[i][1]),(2,2)))
				
			#get brighter/dimmer
			if self.star[i][5] == 0:
				self.star[i][3] -= 1
			if self.star[i][5] == 1:
				self.star[i][3] +=1
				
			#toggle brighter/dimmer
			if self.star[i][3] == 0:
				self.star[i][5] = 1
			if self.star[i][3] == self.star[i][4]:
				self.star[i][5] = 0

		

def exit_game():
	sys.exit()
	
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((320,240),pygame.FULLSCREEN,32)
	stars = Starfield(screen,100,320,240)
	while 1:
		stars.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_game()
		pygame.display.flip()
		clock.tick(FPS)