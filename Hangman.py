import random

wordsList = ['algoritmization', 'math', 'apple', 'then', 'anything', 'idk', 'fighter', 'roblox', 'minecraft']

def random_chooser(list):
    return random.choice(list)

def display_letters(word, letter, secret_word):
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            word[i] = letter
    print(''.join(word))

    return word

def display(ramdom_word):
    print('_' * len(ramdom_word))

def playAgain():
    return input('Do you want play again? (yes or no)').lower().startswith('y')

def sayWord(secret_word):
    isGameOver = False
    Guestword = input('Enter a secret word: ').lower()
    if Guestword == secret_word:
        print('You  won, congrats!!!')
        isGameOver = True
    else:
        print('You lost, stay determined')
        print(f'Secret word was: {secret_word}')
        isGameOver = True

    return isGameOver


def main():
    lifes = 6
    secret_word = random_chooser(wordsList)
    word = ["_"] * len(secret_word)
    wrongLetters = []
    correctLetters = []
    isGameOver = False

    print('*H A N G M A N*')
    print('*Instuction: 1 If you want to exit game enter quit 2 If you know the word, enter say to write word*')
    print('')
    display(secret_word)

    while True:
        if isGameOver:
            if playAgain():
                lifes = 6
                secret_word = random_chooser(wordsList)
                word = ["_"] * len(secret_word)
                wrongLetters = []
                correctLetters = []
                isGameOver = False
                print('')
                display(secret_word)
            else:
                break

        
        print(f'Lifes: {lifes}')
        print(f'Wrong letters: {', '.join(wrongLetters)}')

        letter = input('Enter a letter: ')

        if letter.lower() == 'quit':
            break
        elif letter.lower() == 'say':
            isGameOver = sayWord(secret_word)
            continue
        elif letter.isdigit() or len(letter) > 1:
            print('Enter a letter pls')
            continue

        if letter in wrongLetters or letter in correctLetters:
            print("You've already entered that letter, please try another one")
    
        if letter in secret_word:
            if letter not in correctLetters:
                correctLetters.append(letter)
            display_letters(word, letter, secret_word)
            if '_' not in word:
                print('You  won, congrats!!!')
                isGameOver = True
        else: 
            if letter not in wrongLetters:
                wrongLetters.append(letter)
            print('Oops you are wrong')
            lifes -= 1
            if lifes < 1:
                print('You lost, stay determined')
                isGameOver = True


if __name__ == '__main__':
    main()