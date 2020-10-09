################################################################
# TickTackToe
################################################################
import random

board = []

def SetBoard():
  return [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def SetPlayerPosition (player, row, col):
  board[row][col] = player
  
def CheckRow (row, player):
  line = board [row]
  return line[0] == player and line[1] == player and line[2] == player

def CheckCol (col, player):
  line = [board[0][col], board[1][col], board[2][col]]
  return line[0] == player and line[1] == player and line[2] == player

def CheckPlayerWin (player):
  
  if CheckRow(0, player) or CheckRow(1, player) or CheckRow(2, player):
    return True 
  elif CheckCol(0, player) or CheckCol(1, player) or CheckCol(2, player):
    return True 
  else: 
    return False 

def CheckIsDraw():

  for line in board:
    for cell in line:
      if cell == 0: 
        return False 

  return True   

def displayBoard():
  print (board[0])
  print (board[1])
  print (board[2])

def GetPlayerRowCol (player):
  row = int(input("Enter Row: "))
  col = int(input("Enter Col: "))
  return row, col

def TakeTurn(player):
  row, col = GetPlayerRowCol(player)
  SetPlayerPosition(player, row, col)
  displayBoard()

def PlayGame(board):
  playerWon = False 
  isDraw = False 
  
  displayBoard()
  
  while playerWon == False and isDraw == False:
    player = 1
    TakeTurn(player)
    playerWon = CheckPlayerWin(player)
    isDraw = CheckIsDraw()

    if not playerWon:
      player = 2  
      TakeTurn(player)
      playerWon = CheckPlayerWin(player)
      isDraw = CheckIsDraw()

  if isDraw:
    print("Its a draw!")

  else:
    print ("Player 1 or Player 2 has won.")


def main():
  global board
  board = SetBoard()
  PlayGame(board)

if __name__ == "__main__":
  main()

