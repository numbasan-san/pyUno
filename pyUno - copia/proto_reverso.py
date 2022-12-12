
players = ['Bot_0', 'Bot_1', 'Bot_2', 'Bot_3', 'Bot_4', 'Bot_5', 'Bot_6']
game = True

print(players)

def find_index_player(player):
  index_list = []
  index = players.index(player)
  next_index =  (index - len(players)) + (len(players) - 1)
  print(f'El jugador en turno, {player}, está en el puesto {index + 1} de la lista, su "opuesto" es {next_index}')
  
  # print(f'¿Índice prietativo? { next_index }. ({players[ next_index ]})')

  if index == (len(players) - 1):
    # print('final alcanzado')
    
    for i in range(0, (next_index + 1) ):
      index_list.append( (i) )
    index_list = index_list[::-1]
    index_list.append(index)
    # 
      
  elif index > 0 and index < len(players):

    count = 0

    for i in range((next_index), (len(players))):
      index_list.append( (next_index) + count)
      count -= 1

    index_list = index_list[::-1]
    index_list.append(index)
    index_list.append(index + 1)

    for i in range(0, ((index)) ):

      index_list.append( (next_index) + count)
      count -= 1
      # index_list.append( (i - len(players)) )
    
    index_list = index_list[::-1]

    index_list.pop(0)

    '''

    # 

    # index_list = index_list[::-1]

    print('No es mucho, pero es trabajo honesto')
    
    # print(f'A ver... {list(set(players[index]).difference(players))}')
    
    for i in range(0, (index)):
      index_list.append(i)

    index_list = index_list[::-1]

    index_list.append(index)

    # index_list = index_list[::-1]

    for i in range((index + 1), (len(players))):
      index_list.append(i)
    
    # index_list = index_list[::-1]
    '''

  elif index == 0:
    # print('inicio alcanzado')
    for i in range(1, len(players)):
      index_list.append(i)
    index_list.append(index)
    index_list = index_list[::-1]

  players_list = []

  for i in index_list:
    players_list.append(players[i])

  return players_list, index_list

'''
'''

def play(player_in_turn):
  players_list, index_list = find_index_player(player_in_turn)
  print(f'Listado: {players_list}\nIndex:{index_list}')
  print()

def pregunta(text, opts):
    result = ''
    while result not in opts:
        result = input(text)
    return result
    
while game:
      
  for player in players:
      play(player)
      # print(player)
  
  print(players)
  opt = pregunta('¿Seguir con la ronda? y/n ', ['y', 'n'])
  game = False if opt == 'n' else True
