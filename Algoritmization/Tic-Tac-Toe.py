import random   

def createGrid(grid):
    for row in grid:
        for elem in row:
            print(elem, end=' | ')
        print()
        print('__|___|___')

def updateGrid(grid, position, variable):
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == position:
                grid[i][j] = variable

def computerMove(possibleNumbers):
    position = random.choice(possibleNumbers) 
    return position   
     
def main():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

        position = int(input('Position: '))
        if position in possibleNumbers:
            possibleNumbers.remove(position)
        elif position > 9:
            print('Please enter digit in range 1 - 9')
            continue
        else:   
            print('Posititon is already taken. Please try another one.')
            continue

        print()

        print('Your move: ')
        updateGrid(grid, position, variable)
        createGrid(grid)

        print()

        print('Computer move: ')
        coMove = computerMove(possibleNumbers)
        possibleNumbers.remove(coMove)
        updateGrid(grid, coMove, computerVariable)
        createGrid(grid)

if __name__ == '__main__':
    main()
