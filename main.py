import pygame
import sys
import random
from pygame.locals import *



'''
class Game(object):
	def __init__(self):
		self.score=0
		self.game_over=False
		self.finish=False

	def events_process(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
'''


def main():
	from car import car
	pygame.init()

	SCREENWIDTH=800
	SCREENHEIGHT=600
	#colors
	GREEN=(0,255,56)
	BLACK=(0,0,0)
	GREY=(150,150,150)
	WHITE=(255,255,255)
	RED=(255,0,0)
	YELLOW=(255,255,0)
	speed=1
	finish =False
	game_over= False
	size=(SCREENWIDTH,SCREENHEIGHT)


	screen =pygame.display.set_mode(size)
	pygame.display.set_caption("Car racing")

	font=pygame.font.SysFont('Arial',30)
	font_score=pygame.font.SysFont('Arial',20)

	#music en loop
	pygame.mixer.music.load('audio/soundtrack.mp3')
	pygame.mixer.music.play(-1)

	#Players i cars
	## tratamos todo el grupo de sprites
	all_sprites_list=pygame.sprite.Group()
	playerCar= car('images/car.png',RED,60,80,70)
	playerCar.rect.x=150-playerCar.image.get_width()/2
	playerCar.rect.y=SCREENHEIGHT-100
	car1= car('images/car1.png',YELLOW,60,80,random.randint(50,100))
	car1.rect.x= 150-playerCar.image.get_width()/2
	car1.rect.y= -100
	car2= car('images/car2.png',YELLOW,60,80,random.randint(50,100))
	car2.rect.x= 250-playerCar.image.get_width()/2
	car2.rect.y= -600
	car3= car('images/car3.png',YELLOW,60,80,random.randint(50,100))
	car3.rect.x= 350-playerCar.image.get_width()/2
	car3.rect.y= -300
	car4= car('images/car4.png',YELLOW,60,80,random.randint(50,100))
	car4.rect.x= 450-playerCar.image.get_width()/2
	car4.rect.y= -900


	#agrupamiento de cars
	all_sprites_list.add(playerCar)
	all_sprites_list.add(car1)
	all_sprites_list.add(car2)
	all_sprites_list.add(car3)
	all_sprites_list.add(car4)

	# agrupamiento de coches que llegan

	all_coming_cars=pygame.sprite.Group()
	all_coming_cars.add(car1,car2,car3,car4)
	#definir reloj
	clock=pygame.time.Clock()

	score=0
	
	while not finish:
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					finish=True

			keys=pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				playerCar.moveLeft(5)
			if keys[pygame.K_RIGHT]:
				playerCar.moveRight(5)
			if keys[pygame.K_UP]:
				speed +=0.05
			if keys[pygame.K_DOWN]:
				speed -=0.05

			#Lógica de juego
			#cars en movimiento
			for car in all_coming_cars:
				car.moveForward(speed)
				if car.rect.y>SCREENHEIGHT:
					car.changeSpeed(random.randint(50,100))
					car.rect.y=-200
					# car.repaint(random.choice(lista_colores))
			#lista de colisiones
			car_collision_list=	pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
			for car in car_collision_list:
				#print("Car crash")
				#audio explosion
				game_over=True
				explosion=pygame.mixer.Sound('audio/carcrash.wav')
				explosion.play()
				
			#detectar limites
			if playerCar.rect.x<100:
				print(playerCar.rect.x) 
				playerCar.rect.x=100
			if playerCar.rect.x>(500 - playerCar.image.get_width()):
				playerCar.rect.x=500- playerCar.image.get_width()
				print(playerCar.rect.x)

			#update sprites	
			all_sprites_list.update()
			# dibujar
			screen.fill(GREEN)
			# dibujar carretera
			pygame.draw.rect(screen,GREY,[100,0,400,SCREENHEIGHT])
			pygame.draw.line(screen,WHITE,[200,0],[200,SCREENHEIGHT],5)
			pygame.draw.line(screen,WHITE,[300,0],[300,SCREENHEIGHT],5)
			pygame.draw.line(screen,WHITE,[400,0],[400,SCREENHEIGHT],5)

			#dibujar sprites
			all_sprites_list.draw(screen)
			#textos
			text=font.render("Car racing",True,BLACK)
			screen.blit(text,(SCREENWIDTH-text.get_width()-10,30))
			text_score=font_score.render("Score: "+str(score),True,BLACK)
			screen.blit(text_score,(SCREENWIDTH-text_score.get_width()-10,60))
			score +=1
			pygame.display.flip()

			clock.tick(60)
		#game over		
		text_exit=font.render("Continue Y/N?",True,BLACK)
		screen.blit(text_exit,(SCREENWIDTH/2-text_exit.get_width(),SCREENHEIGHT/2))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finish=True

			keys=pygame.key.get_pressed()
			if keys[pygame.K_y]:
				score=0
				#reset
				main()
				game_over=False
			if keys[pygame.K_n]:
				finish=True


	sys.exit()


if __name__ == "__main__":
	main()
'''

#velocidad inicial del playercar
speed=1

size=(SCREENWIDTH,SCREENHEIGHT)


screen =pygame.display.set_mode(size)
pygame.display.set_caption("Car racing")

font=pygame.font.SysFont('Arial',30)
font_score=pygame.font.SysFont('Arial',20)

#music en loop
pygame.mixer.music.load('audio/soundtrack.mp3')
pygame.mixer.music.play(-1)

#Players i cars
## tratamos todo el grupo de sprites
all_sprites_list=pygame.sprite.Group()
playerCar=car('images/car.png',RED,60,80,70)
playerCar.rect.x=150-playerCar.image.get_width()/2
playerCar.rect.y=SCREENHEIGHT-100
car1=car('images/car1.png',YELLOW,60,80,random.randint(50,100))
car1.rect.x= 150-playerCar.image.get_width()/2
car1.rect.y= -100
car2=car('images/car2.png',YELLOW,60,80,random.randint(50,100))
car2.rect.x= 250-playerCar.image.get_width()/2
car2.rect.y= -600
car3=car('images/car3.png',YELLOW,60,80,random.randint(50,100))
car3.rect.x= 350-playerCar.image.get_width()/2
car3.rect.y= -300
car4=car('images/car4.png',YELLOW,60,80,random.randint(50,100))
car4.rect.x= 450-playerCar.image.get_width()/2
car4.rect.y= -900


#agrupamiento de cars
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

# agrupamiento de coches que llegan

all_coming_cars=pygame.sprite.Group()
all_coming_cars.add(car1,car2,car3,car4)
#definir reloj
clock=pygame.time.Clock()

score=0
finished=False
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished=True

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		playerCar.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		playerCar.moveRight(5)
	if keys[pygame.K_UP]:
		speed +=0.05
	if keys[pygame.K_DOWN]:
		speed -=0.05

	#Lógica de juego
	#cars en movimiento
	for car in all_coming_cars:
		car.moveForward(speed)
		if car.rect.y>SCREENHEIGHT:
			car.changeSpeed(random.randint(50,100))
			car.rect.y=-200
			# car.repaint(random.choice(lista_colores))
	#lista de colisiones
	car_collision_list=	pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
	for car in car_collision_list:
		print("Car crash")
		#audio explosion
		finished=True
	
	all_sprites_list.update()

	screen.fill(GREEN)
	# dibujar carretera
	pygame.draw.rect(screen,GREY,[100,0,400,SCREENHEIGHT])
	pygame.draw.line(screen,WHITE,[200,0],[200,SCREENHEIGHT],5)
	pygame.draw.line(screen,WHITE,[300,0],[300,SCREENHEIGHT],5)
	pygame.draw.line(screen,WHITE,[400,0],[400,SCREENHEIGHT],5)

	#dibujar sprites
	all_sprites_list.draw(screen)

	text=font.render("Car racing",True,BLACK)
	screen.blit(text,(SCREENWIDTH-text.get_width()-10,30))
	text_score=font_score.render("Score: "+str(score),True,BLACK)
	screen.blit(text_score,(SCREENWIDTH-text_score.get_width()-10,60))
	score +=1
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
'''