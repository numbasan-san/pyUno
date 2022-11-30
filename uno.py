
import random
from jugador import Jugador, jugadores
from mesa import *
from utilities import *

class Uno:
	"""docstring for Uno"""
	def __init__(self):
		total_jugadores = int(input("¿Cuántos jugadores totales serán? "))
		Jugador.iniciar_jugadores(total_jugadores)

		self.mesa = Mesa()
		self.mesa.mezclar()
		self.len_mesa = len(self.mesa.mazo)

		print('\nCarta en Mesa:', self.mesa.servir_mesa((self.mesa.mazo[ (random.randint(0, self.len_mesa ))])))

		print(self.len_mesa)

		for i in range(5):
			for jugador in jugadores:
				jugador.tomar_carta(self.mesa.mazo[ (random.randint(0, self.len_mesa ))])

	def ronda(self):

		#print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)

		for jugador in jugadores:
			print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)
			self.jugar(jugador)

		#print('\nPrimera carta:', self.mesa.mostrar())
		# print(self.mesa.mostrar_todo())

	def jugar(self, jugador):
		print('\nMano de', jugador.nombre)
		jugador.imprimir_mano(selection = True)
		action = Utilities.opciones("¿Qué harás? Ver, Tirar, Robar. [V, T, R] ", ['V', 'T', 'R'])

		if action == 'T':
			selection = (Utilities.pregunta('¿Cuál carta tirará? ', 0, len(jugador.mano), -1)) - 1
			self.mesa.servir_mesa(jugador.mano.pop(selection - 1))

		elif action == 'R':
			jugador.tomar_carta(self.mesa.mazo[ (random.randint(0, self.len_mesa ))])

	def game_over(self):
		opt = Utilities.opciones('¿Terminar? ', ['Y', 'N'])
		end = True if opt == 'Y' else False
		return end
