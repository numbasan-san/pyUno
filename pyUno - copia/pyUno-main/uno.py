
import random
from jugador import Jugador, jugadores
from mesa import *
from utilities import *
from especiales import *

class Uno:
    """docstring for Uno"""
    def __init__(self):
        total_jugadores = int(input("¿Cuántos jugadores totales serán? "))
        Jugador.iniciar_jugadores(total_jugadores)

        self.mesa = Mesa()
        self.especiales = Especiales()

        self.mesa.mezclar()
        self.len_mesa = len(self.mesa.mazo)
        self.sentido = 1

        print('\nCarta en Mesa:', self.mesa.servir_mesa((self.mesa.mazo[0])))

        print(self.len_mesa)

        for i in range(5):
            for jugador in jugadores:
                self.mesa.mezclar()
                jugador.tomar_carta(self.mesa.mazo[0])

				
    '''
    BUG.
    
    Al momento de hacer el reverso se salta jugadores de vez en vez.
    '''
    def ronda(self):

		#print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)

        for i in range(len(jugadores)):
            print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)
            #print('Logitud de la mano del jugador:', len(jugador.mano))
            null = 0 if self.sentido == 1 else 1
            index = i + ( null * ( self.sentido * ( len(jugadores) ) ) ) 
            # print(f'Supuesto inverso: {index}')
            self.jugar(jugadores[ index ]) # self.sentido

		#print('\nPrimera carta:', self.mesa.mostrar())
		# print(self.mesa.mostrar_todo())

    def jugar(self, jugador):
        print('\nMano de', jugador.nombre)
        jugador.imprimir_mano(selection = True)
        print(len(jugadores))
        action = Utilities.opciones("¿Qué harás? Ver, Tirar, Robar. [V, T, R] ", ['V', 'T', 'R'])

        if action == 'T':
            selection = (Utilities.pregunta('¿Cuál carta tirará? ', 1, len(jugador.mano), -1))
            valid_cards = self.valid_cards(jugador, jugador.mano)
            action = Utilities.validar(selection, valid_cards)

            if  jugador.mano[selection - 1] in valid_cards:
                if jugador.mano[selection - 1].valor == 'Joker':
# BUG.
# Cambia el color/palo de las demás cartas Joker del juego al cambiar el palo del joker lanzado.
                    jugador.mano[selection - 1].palo = self.especiales.skill_joker()
                    jugador.mano[selection - 1].etiqueta = jugador.mano[selection].valor + ' ' + jugador.mano[selection].palo
                    self.mesa.servir_mesa(jugador.mano.pop(selection - 1))
    
                elif jugador.mano[selection - 1].valor == 'Ginyu':
                    self.mesa.servir_mesa(jugador.mano.pop(selection - 1))
                    self.especiales.skill_ginyu(jugador)
    
                elif jugador.mano[selection - 1].valor == '+4':
                    plus = 4
                    self.especiales.skill_plus(jugador, self.mesa, plus)
                    self.mesa.servir_mesa(jugador.mano.pop(selection - 1))
			
                elif jugador.mano[selection - 1].valor == '+2':
                    plus = 2 
                    self.especiales.skill_plus(jugador, self.mesa, plus)
                    self.mesa.servir_mesa(jugador.mano.pop(selection - 1))
                else:
                    self.mesa.servir_mesa(jugador.mano.pop(selection - 1))
            else:
                print(f'Carta inválida. Elija otra.')
                

        elif action == 'R':
            self.mesa.mezclar()
            jugador.tomar_carta(self.mesa.mazo[0])

    def valid_cards(self, jugador, mano):
        valid_cards = []
        for i in range(len(mano)):
            if self.mesa.cartas_mesa.valor in ['Joker', 'Ginyu', '+4'] or \
            ((jugador.mano[i].valor == self.mesa.cartas_mesa.valor) or \
            (jugador.mano[i].palo == self.mesa.cartas_mesa.palo)):
                valid_cards.append(str(i + 1))
        return valid_cards

    def game_over(self):
        opt = Utilities.opciones("¿Terminar? ['Y', 'N'] ", ['Y', 'N'])
        end = True if opt == 'Y' else False
        return end
