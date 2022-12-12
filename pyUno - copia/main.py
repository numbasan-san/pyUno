
from uno import *

print('Uno en Py.')
uno = Uno()

while not uno.game_over():
	uno.ronda()