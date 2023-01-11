
import random, os
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
        self.skip = False

        print('\nCarta en Mesa:', self.mesa.servir_mesa((self.mesa.mazo[0])))

        print(self.len_mesa)

        for i in range(5):
            for jugador in jugadores:
                self.mesa.mezclar()
                jugador.tomar_carta(self.mesa.mazo[0])

    def ronda(self):

		#print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)
        players = jugadores[::self.sentido]
        # jugadores = players
        
        '''
        print(f'Supuesta lista inversa de los jugadores:')
        for i in range(len(players)):
            print(f'{players[i].nombre}')
        '''

        i = 0
        while i <= len(jugadores) and i >= -(len(jugadores)):
            # print(f'uno.sentido = {self.sentido}')
            # os.system('cls')
            print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)
            if not self.skip:
                self.jugar(players[ i ])
            else:
                self.skip = False
            i += self.sentido
            if i >= len(jugadores):
               i = 0
            if i <= -(len(jugadores)):
               i =  -1
        '''
        for i in range(len(players)):
            print('\nCarta en Mesa:', self.mesa.cartas_mesa.etiqueta)
            # print('Logitud de la mano del jugador:', len(jugador.mano))
            #'null = 0 if self.sentido == 1 else 1''
            index = i * self.sentido 
            print(f'Supuesto inverso: {index}')
            self.jugar(players[ index ]) # self.sentido
		#print('\nPrimera carta:', self.mesa.mostrar())
		# print(self.mesa.mostrar_todo())
        '''

    def jugar(self, jugador):
        print('\nMano de', jugador.nombre)
        jugador.imprimir_mano(selection = True)
        print(len(jugadores))

        valid_cards = self.valid_cards(jugador, jugador.mano)
        print(f'Cartas válidas: {valid_cards}.')

        if len(valid_cards) >= 1:

            action = Utilities.opciones("¿Qué harás? Ver, Tirar, Robar. [V, T, R] ", ['V', 'T', 'R'])

            if action == 'T':
                selection = (Utilities.pregunta('¿Cuál carta tirará? ', 1, len(jugador.mano), -1))
                # print(f'Uno.jugar.selection: {selection}')
                select_valid = Utilities.validar(selection, valid_cards)
                selection = int(select_valid) - 1

                # print(f'Carta lanzada: {jugador.mano[selection].etiqueta}. Indice: {str(selection)}')

                if jugador.mano[selection].valor == 'Joker':
                    carta = self.especiales.skill_joker()
                    jugador.mano.pop(selection)
                    self.mesa.servir_mesa(carta)

                elif jugador.mano[selection].valor == 'Ginyu':
                    self.mesa.servir_mesa(jugador.mano.pop(selection))
                    self.especiales.skill_ginyu(jugador, self.sentido)

                elif jugador.mano[selection].valor == '+4' or jugador.mano[selection].valor == '+2':
                    plus = 4 if jugador.mano[selection].valor == '+4' else 2
                    self.especiales.skill_plus(jugador, self.mesa, plus, self.sentido)
                    self.mesa.servir_mesa(jugador.mano.pop(selection))

                elif jugador.mano[selection].valor == 'Reverso':
                    # BUG.
                    # Al momento de hacer el reverso se salta jugadores de vez en vez.
                    self.sentido *= -1
                    self.mesa.servir_mesa(jugador.mano.pop(selection))
                    print(f'Kira Kuin Dai San no Bakkudan: Baito Za Dasuto!')

                elif jugador.mano[selection].valor == 'Skip':
                    self.skip = True
                    self.mesa.servir_mesa(jugador.mano.pop(selection))
                    print(f'Kimu Kurinson!')

                elif not jugador.mano[selection].valor in ['+2', 'Reverso', 'Skip', 'Joker', '+4', 'Ginyu']:
                    self.mesa.servir_mesa(jugador.mano.pop(selection))

            elif action == 'R':
                self.mesa.mezclar()
                jugador.tomar_carta(self.mesa.mazo[0])

        else:
            print(f'Cartas insuficientes para jugar. Robo atumático.')
            self.mesa.mezclar()
            jugador.tomar_carta(self.mesa.mazo[0])

        input()

    def valid_cards(self, jugador, mano):
        valid_cards = []
        for i in range(len(mano)):
            if self.mesa.cartas_mesa.valor in ['Ginyu', '+4'] or \
            jugador.mano[i].valor in ['Joker', 'Ginyu', '+4'] or \
            ((jugador.mano[i].valor == self.mesa.cartas_mesa.valor) or \
            (jugador.mano[i].palo == self.mesa.cartas_mesa.palo)):
                valid_cards.append(str(i + 1))
        return valid_cards

    def game_over(self):
        opt = Utilities.opciones("¿Terminar? ['Y', 'N'] ", ['Y', 'N'])
        end = True if opt == 'Y' else False
        return end
#
