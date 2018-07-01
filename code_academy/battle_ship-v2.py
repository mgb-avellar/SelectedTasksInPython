#! /usr/bin/python

from random import randint 

print

board = []

for i in range(0,5):
  board.append(["O"]*5)

def print_board(board_in):
  for row in board_in:
    # print row  # aparece 'O' 'O' 'O' 'O' 'O'
    print " ".join(row)  # aparece O O O O O
    
print_board(board)
#print len(board)  # nesse caso, o resultado sera 5

# criando numeros aleatorios entre 0 e 5 para a posicao do navio

def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# pedindo ao usuario para adivinhar a linha e a coluna
# o raw_input retorna sempre uma string e por isso, se quisermos
#  fazer operacoes matematicas com o numero de entrada, precisamos
#  converte-lo apropriadamente

#print ship_row
#print ship_col

print

for turn in range(4):
  print "Turn", turn + 1

  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):  # numeros escolhidos fora do tabuleiro
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":  # numeros escolhidos ja tinha sido escolhidos
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      print_board(board)
    if turn == 3:
      print "Game Over."
      print "The ship was at row", [ship_row], "and col", [ship_col] 

  print

print
