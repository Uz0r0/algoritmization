import random

def randomNumber():
    n = random.randint(100, 999)
    nAsList = []
    for i in str(n):
        nAsList.append(i)
    return nAsList

def checkNumber(secret_number, number):
    count = {}
    for ch in secret_number:
        count[ch] = count.get(ch, 0) + 1

    checkList = [''] * len(secret_number)

    for i in range(len(secret_number)):
        if number[i] == secret_number[i]:
            checkList[i] = 'A'
            count[number[i]] -= 1 

    for i in range(len(secret_number)):
        if checkList[i] == '':
            digit = number[i]
            if digit in count and count[digit] > 0:
                checkList[i] = 'B'
                count[digit] -= 1
            else:
                checkList[i] = 'C'

    if all(ch == 'A' for ch in checkList):
        return True

    print(checkList)
    return False

def playAgain():
    return input('Do you want play again? (yes or no)').lower().startswith('y')

def reset_game(): 
    return randomNumber(), 6, False, 

def main():
    secret_number, lifes, isGameOver = reset_game()

    print('*N U M B E R L E*')
    print('*Instuction:  A - Correct number and place, B - Correct number, but wrong place, C - Wrong number and place*')

    print(secret_number)

    while True:
        print()

        print(f'Lifes: {lifes}')

        print()

        number = input('Enter your number here: ')

        if number.isdigit() == False:
            print('Please entere a number')
            continue
        elif len(number) < 3:
            print('Pleae enter a 3 digit number')
            continue

        if checkNumber(secret_number, number):
            print('Congrats, you won!!!')
            isGameOver = True
        else:
            lifes -= 1

        if lifes == 0:
            isGameOver = True

        if isGameOver:
            if playAgain():
                secret_number, lifes, isGameOver = reset_game()
            else:
                break

if __name__ == '__main__':
    main()