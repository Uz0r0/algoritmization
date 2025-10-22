import random   

def createGrid(grid):
    print('-------------')
    for row in grid:
        print('|', end=' ')
        for elem in row:
            print(elem, end=' | ')
        print()
        print('-------------')

def updateGrid(grid, position, variable):
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == position:
                grid[i][j] = variable   
                return     

def computerMove(possibleNumbers):
    position = random.choice(possibleNumbers) 
    return position   

def checkWin(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0], True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i], True
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0], True
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2], True

    return None, False

def printWinner(variable, isGameDone, computerVariable):
    if isGameDone:
        print()
        if variable == computerVariable:
            print('You lost')
        else:
            print('Congrats, you won!!!')

def playAgain():
    return input('Do you want play again? (yes or no)').lower().startswith('y')
        
def reset_game():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ], [1,2,3,4,5,6,7,8,9], False,

def move(grid, position, variable, player):
    print()

    print(player)
    updateGrid(grid, position, variable)
    createGrid(grid)
     
def main():
    grid, possibleNumbers, isGameDone = reset_game()

    print('T I C - T A C - T O E')

    print()
 
    createGrid(grid)

    while True:
        print()
        variable = input('Pick x or o: ')
        if variable.lower() != 'x' and variable.lower() != 'o':
            print('Please enter x or o')
            continue
        else:
            break

    if variable.lower() == 'x':
        variable = 'x'
        computerVariable = 'o'
        First = True
    else:
        variable = 'o'
        computerVariable = 'x'
        First = False

    while True:

        if First:
            print()

            while True:
                pos_input = input('Position (1-9): ').strip()
                try:
                    position = int(pos_input)
                except ValueError:
                    print('Please enter a number 1-9.')
                    continue

                if position < 1 or position > 9:
                    print('Please enter digit in range 1 - 9')
                    continue
                if position not in possibleNumbers:
                    print('Position is already taken. Please try another one.')
                    continue

                possibleNumbers.remove(position)
                break

            move(grid, position, variable, 'Your move: ')

            winnerVariable, isGameDone = checkWin(grid)
            printWinner(winnerVariable, isGameDone, computerVariable)

            if isGameDone:
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break 

            if not possibleNumbers:
                print("It's a tie!")
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break

            coMove = computerMove(possibleNumbers)
            possibleNumbers.remove(coMove)
            move(grid, coMove, computerVariable, 'Computer move: ')

            winnerVariable, isGameDone = checkWin(grid)
            printWinner(winnerVariable, isGameDone, computerVariable)

            if isGameDone:
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break

            if not possibleNumbers:
                print("It's a tie!")
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break  
        else:  
            coMove = computerMove(possibleNumbers)
            possibleNumbers.remove(coMove)
            move(grid, coMove, computerVariable, 'Computer move: ')

            winnerVariable, isGameDone = checkWin(grid)
            printWinner(winnerVariable, isGameDone, computerVariable)

            if isGameDone:
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    createGrid(grid)
                    continue
                else:
                    break

            if not possibleNumbers:
                print("It's a tie!")
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    createGrid(grid)
                    continue
                else:
                    break  

            print()
            
            while True:
                pos_input = input('Position (1-9): ').strip()
                try:
                    position = int(pos_input)
                except ValueError:
                    print('Please enter a number 1-9.')
                    continue

                if position < 1 or position > 9:
                    print('Please enter digit in range 1 - 9')
                    continue
                if position not in possibleNumbers:
                    print('Position is already taken. Please try another one.')
                    continue

                possibleNumbers.remove(position)
                break

            move(grid, position, variable, 'Your move: ')

            winnerVariable, isGameDone = checkWin(grid)
            printWinner(winnerVariable, isGameDone, computerVariable)

            if isGameDone:
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break 

            if not possibleNumbers:
                print("It's a tie!")
                if playAgain():
                    grid, possibleNumbers, isGameDone = reset_game()
                    print()
                    createGrid(grid)
                    continue
                else:
                    break

if __name__ == '__main__':
    main()