
from jugador import *
from utilities import *

class Especiales:
	

	def __init__(self): #, etiqueta, palo
		# self.etiqueta = ['+4', 'Ginyu', 'Joker']
		# self.palo = 'negro'
		self.skills_especiales = {'+4': self.skill_plus_4, 'Ginyu': self.skill_ginyu, 'Joker': self.skill_joker}

	@staticmethod
	def skill_plus_4(jugador_en_turno, mesa):

		for jugador in jugadores:
			for i in range(4):
				if not jugador == jugador_en_turno:
					mesa.mezclar()
					jugador.tomar_carta(mesa.mazo[0])
				else:
					pass

		print('Los demás jugadores recibieron 4 cartas.')

	@staticmethod
	def skill_plus_2(jugador, mesa):

		index = jugadores.index(jugador)
		if index == len(jugadores) - 1:
			index =  0
		else:
			index = index + 1

		for i in range(2):
			mesa.mezclar()
			jugadores[index].tomar_carta(mesa.mazo[0])
		
		print('El siguiente jugador recibió 2 cartas.')

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

	@staticmethod
	def skill_reverso(jugador_en_turno, jugadores):
		lista_jugadores = []
		players = jugadores[::-1]

		for jugador in players:
			if jugador != jugador_en_turno :
				lista_jugadores.append(jugador)

		lista_jugadores.append(jugador_en_turno)
		jugadores = lista_jugadores

		for i in range(len(jugadores)):
			print(jugadores[i].nombre)
'''
	PROTOTIPO DEL EFECTO DE LA CARTA 'REVERSO'
			
'''
