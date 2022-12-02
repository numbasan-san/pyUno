
from jugador import *
from mesa import *

class Especiales:
	

	def __init__(self): #, etiqueta, palo
		# self.etiqueta = ['+4', 'Ginyu', 'Joker']
		# self.palo = 'negro'
		self.skills_especiales = {'+4': self.skill_plus_4, 'Ginyu': self.skill_ginyu, 'Joker': self.skill_joker}

	@staticmethod
	def skill_plus_4(player, mesa):

		for jugador in jugadores:
			for i in range(4):
				mesa.mezclar()
				if not jugador == player:
					jugador.tomar_carta(mesa.mazo[0])
				else:
					pass

		print('Los demás jugadores recibieron 4 cartas.')

	@staticmethod
	def skill_joker(player):
		return None

	@staticmethod
	def skill_ginyu(player):
		return None