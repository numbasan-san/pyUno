
from jugador import *
from utilities import *

class Especiales:
	

	def __init__(self):
		self.skills_especiales = {'+4': self.skill_plus, '+2': self.skill_plus, 'Ginyu': self.skill_ginyu, 'Joker': self.skill_joker}
		
	@staticmethod
	def skill_plus(jugador, mesa, num):

		index = jugadores.index(jugador)
		if index == len(jugadores) - 1:
			index =  0
		else:
			index = index + 1

		for i in range(num):
			mesa.mezclar()
			jugadores[index].tomar_carta(mesa.mazo[0])
		
		print(f'El siguiente jugador recibió {str(num)} cartas.')

	@staticmethod
	def skill_joker():
		opt = Utilities.opciones('¿Cuál color quieres? Rojo, Verde, Azul, Amarillo [R, V, Z, A]',  ['R', 'V', 'Z', 'A'])

		palos = {'R':'rojo' , 'V':'verde', 'Z':'azul', 'A':'amarillo'}

		for palo in palos:
			if palo == opt:
				return palos[palo]

	@staticmethod
	def skill_ginyu(jugador):

		index = jugadores.index(jugador)
		if index == len(jugadores) - 1:
			index =  0
		else:
			index = index + 1

		mano_1 = jugador.mano
		mano_2 = jugadores[index].mano
		jugador.mano = mano_2
		jugadores[index].mano = mano_1
		print('VEYETTA #########!!!!!')
