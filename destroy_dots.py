#Imports
from guizero import App, Text, Waffle, PushButton
from random import randint
#funciones

def crear_punto():
	global speed
	x, y= randint(0,CAJA_TAMAÑO-1), randint(0,CAJA_TAMAÑO-1)
	while board[x, y].dotty==True:
		x, y= randint(0,CAJA_TAMAÑO-1), randint(0,CAJA_TAMAÑO-1)
	board[x, y].dotty = True
	board.set_pixel(x, y, "red")

	#velocidad

	

	all_red=True

	cantidad=0
	for x in range(CAJA_TAMAÑO):
		for y in range(CAJA_TAMAÑO):
			if board[x, y].color!= "red":
				all_red=False
			else:
				cantidad+=1

	if cantidad>10:
		speed=300-puntuaje
	elif cantidad>20:
		speed= 700-puntuaje
	elif puntuaje>0:
		speed=200-puntuaje






	if not all_red:
		board.after(speed, crear_punto)
	else:
		texto_puntos.show()
		texto_puntos.value="Has perdido."
		board.disable()
		reset.show()

def destruir_punto(x, y):
	global puntuaje
	if board[x, y].dotty == True:
		board[x, y].dotty=False
		board.set_pixel(x, y, "white")
		puntuaje+=1
		texto.value=f"El puntuaje es {puntuaje}"

def reiniciarJuego():
	global puntuaje
	for x in range(CAJA_TAMAÑO):
		for y in range(CAJA_TAMAÑO):
			board[x, y].dotty=False
			board.set_pixel(x, y, "white")
			board.enable()
			puntuaje=0
			reset.hide()
			texto.value=f"El puntuaje es {puntuaje}"
	board.after(1000, crear_punto())






#Apps
app=App("Destruir puntos", height=250, width=250)

#Widgets
speed=200
puntuaje=0
CAJA_TAMAÑO=5
board= Waffle(app, width=CAJA_TAMAÑO, height=CAJA_TAMAÑO, command=destruir_punto)
board.after(speed, crear_punto)
texto= Text(app, text="El puntuaje es 0")
texto_puntos= Text(app, visible=False)
reset=PushButton(app, text="Reiniciar", visible=False, command=reiniciarJuego)

#display

app.display()