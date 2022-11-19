
import random

class Carta:
	
	def __init__(self, etiqueta, palo):
		self.etiqueta = etiqueta
		self.palo = palo

	@staticmethod
	def cargar_cartas():
		palos = ['rojo', 'azul', 'amarillo', 'verde']
		valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		baraja = []
		for p in palos:
			for v in valores:
				baraja.append(Carta(v + " " + p, p))
		return baraja

	@staticmethod
	def mezcla(baraja):
		random.shuffle(baraja)
		return baraja

	def imprimir_carta(self, numeracion = None):
		print((str(numeracion) + '. ' if numeracion != None else '') + self.etiqueta)
