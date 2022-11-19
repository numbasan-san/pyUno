
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

		print('\nCarta en Mesa:', self.mesa.servir_mesa( (random.randint(0, self.len_mesa))))

		print(self.len_mesa)

		for i in range(5):
			for jugador in jugadores:
				jugador.tomar_carta(self.mesa.mazo[ (random.randint(0, self.len_mesa ))])

	def ronda(self):

		print('\nCarta en Mesa:', self.mesa.cartas_mesa[0].etiqueta)

		for jugador in jugadores:
			self.jugar(jugador)

		print('\nPrimera carta:', self.mesa.mostrar())
		# print(self.mesa.mostrar_todo())

	def jugar(self, jugador):
		print('Mano de', jugador.nombre)
		jugador.imprimir_mano(selection = True)

	def game_over(self):
		opt = Utilities.opciones('¿Terminar? ', ['Y', 'N'])
		end = True if opt == 'Y' else False
		return end
