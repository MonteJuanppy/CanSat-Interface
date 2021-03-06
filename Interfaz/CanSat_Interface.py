#librerias que se importan
import pygame 
import time


#inicializa todos los modulos de pygame
#retorna si la inicializacion fue exitosa o no 
pygame.init()

#va a ser nuestra superficie 
display = pygame.display.set_mode((1298,768)) #Resolucion de la ventana

pygame.display.set_caption('CanSat') #titulo de la ventana 

#imagen
image = pygame.image.load(r'logo.jpeg')
image = pygame.transform.scale(image, (420, 320))

#icono
pygame.display.set_icon(image)

myColor = (10,26,56) #fondo
orange = (255,127,80) #botones
white = (255,255,255) #color de letra 

#variable necesaria para los textos
smallfont = pygame.font.SysFont(None,25)
mediumfont = pygame.font.SysFont(None,30)
bigfont = pygame.font.SysFont(None,75)

#Estilo de los textos
def textObjects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text,True,color)
	if size == "medium":
		textSurface = mediumfont.render(text,True,color)
	if size == "big":
		textSurface = bigfont.render(text,True,color)
	return textSurface, textSurface.get_rect()

#texto de los botones
def textToButton(msg,color,buttonx,buttony,buttonwidth,buttonheight):
	textSurf, textRect = textObjects(msg,color,"small")
	textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
	display.blit(textSurf,textRect)
	
#funcion que lee si se le hizo click al boton 
def button(msg,x,y,width,height):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + width > cur[0] > x and y + height > cur[1] > y and click[0] == 1:
		buttonActions(msg)
		
def label(msg,color,size,x,y):
	textSurf, textRect = textObjects(msg,color,size)
	textRect.center = (x,y)
	display.blit(textSurf,textRect)
	
		
#Acciones de los diferentes botones, cada uno lleva a la funcion definida
def buttonActions(msg):
	if msg == "Exit":
		pygame.quit()
		quit()
	if msg == "Tempeture":
		print(msg)
	if msg == "Pressure":
		print(msg)
	if msg == "Voltage":
		print(msg)
	if msg == "Air speed":
		print(msg)
	if msg == "Altitude":
		print(msg)
	if msg == "General":
		general()
	if msg == "Trajectory":
		print(msg)
	if msg == "Return":
		init()
	if msg == "Start":
		print(msg)
	if msg == "Reset":
		print(msg)
		


#metodo de inicializacion 
def init():

	display.fill(myColor)
	
	#imagen
	display.blit(image,(439,125))
	
	
	#Uso de draw  eje x, eje y, largo, altura
	
	#izquierda
	pygame.draw.rect(display,orange, (100,125,200,75))
	pygame.draw.rect(display,orange, (100,320,200,75))
	pygame.draw.rect(display,orange, (100,515,200,75))

	#derecha
	pygame.draw.rect(display,orange, (1000,125,200,75))
	pygame.draw.rect(display,orange, (1000,320,200,75))
	pygame.draw.rect(display,orange, (1000,515,200,75))
	
	#Centro
	pygame.draw.rect(display,orange, (550,515,200,75))
	
	#Exit
	pygame.draw.rect(display,myColor, (1100,625,200,75))
	
	#codigo para poner el texto en los rectangulos
	textToButton("Voltage",white,100,125,200,75)
	textToButton("Air speed",white,100,320,200,75)
	textToButton("Altitude",white,100,515,200,75)
	textToButton("Trajectory",white,1000,125,200,75)
	textToButton("Tempeture",white,1000,320,200,75)
	textToButton("Pressure",white,1000,515,200,75)
	textToButton("General",white,550,515,200,75)
	textToButton("Exit",white,1100,625,200,75)

	#Aplica los cambios realizados en el fondo
	pygame.display.update()
	
	time.sleep(0.25)
	
	mainloop = True
	while mainloop:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
	
		#espera de los evento de presionar los botones 
		button("Voltage",100,125,200,75)
		button("Air speed",100,320,200,75)
		button("Altitude",100,515,200,75)
		button("Trajectory",1000,125,200,75)
		button("Tempeture",1000,320,200,75)
		button("Pressure",1000,515,200,75)
		button("General",550,515,200,75)
		button("Exit",1100,625,200,75)
	
		
#Inicializa el fondo y aplica los valores para mostrar la ventana general	
def general():
	display.fill(myColor)
	
	#Return
	pygame.draw.rect(display,myColor, (1100,625,200,75))
	textToButton("Return",white,1100,625,200,75)
	
	#Start / Reset
	pygame.draw.rect(display,orange, (540,515,90,50))
	pygame.draw.rect(display,orange, (660,515,90,50))
	
	textToButton("Start",white,540,515,90,50)
	textToButton("Reset",white,660,515,90,50)
	
	#Etiquetas izq
	label("Voltage:",white,"medium",900,125)
	label("Air speed:",white,"medium",900,175)
	label("Altitude:",white,"medium",900,225)
	label("Trajectory:",white,"medium",900,275)
	label("Tempeture:",white,"medium",900,325)
	label("Pressure:",white,"medium",900,375)
	label("Particle count:",white,"medium",900,425)
	label("Software state:",white,"medium",900,475)
	
	#Etiquetas der
	label("Team ID:",white,"medium",300,125)
	label("Mission time:",white,"medium",300,175)
	label("Packet count:",white,"medium",300,225)
	label("GPS time:",white,"medium",300,300)
	label("GPS altitude:",white,"medium",300,350)
	label("GPS latitud:",white,"medium",300,400)
	label("GPS longitud:",white,"medium",300,450)
	
	#titulo
	label("General",white,"big",650,60)
	
	#imagen
	image = pygame.image.load(r'logo.jpeg')
	image = pygame.transform.scale(image, (110, 90))
	display.blit(image,(20,20))
	
	
	#Aplicar los cambios en el fondo
	pygame.display.update()
	
	time.sleep(0.25)
	
	
	mainloop = True
	#este while es el mainloop
	while mainloop:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
		
		#leyendo las acciones de los botones
		button("Return",1100,625,200,75)
		button("Start",540,515,90,50)
		button("Reset",660,515,90,50)
	
#llama a la funcion que inicializa todo el programa 	
init()
