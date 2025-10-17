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

def checkWin(grid):
    winLines = [
        [(0,0), (0,1), (0,2)], 
        [(1,0), (1,1), (1,2)],  
        [(2,0), (2,1), (2,2)], 
        [(0,0), (1,0), (2,0)],  
        [(0,1), (1,1), (2,1)],  
        [(0,2), (1,2), (2,2)],  
        [(0,0), (1,1), (2,2)],  
        [(0,2), (1,1), (2,0)]   
    ]

    for line in winLines:
        (r1, c1), (r2, c2), (r3, c3) = line
        v1 = grid[r1][c1]
        v2 = grid[r2][c2]
        v3 = grid[r3][c3]
        if v1 == v2 == v3 and v1 in ('x', 'o'):
            print("We have a winner!")
            return True
        return False

def playAgain():
    return input('Do you want play again? (yes or no)').lower().startswith('y')
        

def reset_game():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ], [1,2,3,4,5,6,7,8,9], False
     
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
    else:
        variable = 'o'
        computerVariable = 'x'

    while True:

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

        print()

        print('Your move: ')
        updateGrid(grid, position, variable)
        createGrid(grid)

        isGameDone = checkWin(grid)  

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

        print('Computer move: ')
        coMove = computerMove(possibleNumbers)
        possibleNumbers.remove(coMove)
        updateGrid(grid, coMove, computerVariable)
        createGrid(grid)

        isGameDone = checkWin(grid)  

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



if __name__ == '__main__':
    main()