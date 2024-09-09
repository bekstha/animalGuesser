import random
from collections import Counter

animals = '''cat dog elephant tiger lion leopard zebra giraffe kangaroo monkey horse rabbit deer bear fox wolf cheetah panda koala squirrel'''

animals = animals.split(' ')

def play_game():
    word_to_guess = random.choice(animals)
    chances = len(word_to_guess) + 2
    print('Guess the word! HINT: It is an animal. You have {} chances to guess'. format(chances) )

    for i in word_to_guess:
        print('_', end=' ')
    print()

        # storing values
    letterGuessed = ''
    correct = 0
    flag = 0

    while (chances != 0) and flag == 0:
        print()
        chances -=1

        guess = str(input('Enter a letter to guess:'))

        if not guess.isalpha():
            print('Only a letter please!')
            continue
        elif len(guess) > 1:
            print('Please enter only 1 letter at a time')
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        if guess in word_to_guess:
                k = word_to_guess.count(guess)
                for _ in range(k):
                    letterGuessed += guess

        for char in word_to_guess:
            if char in letterGuessed and (Counter(letterGuessed) != Counter(word_to_guess)):
                print(char, end=' ')
                correct += 1

            elif(Counter(letterGuessed) == Counter(word_to_guess)):
                print('The word is: ', end=' ')
                print(word_to_guess)
                flag = 1
                print('You won!!')
                break
            else:
                print('_', end=' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word_to_guess)):
            print()
            print('You loose... Try again!')
            print('The word was {}'. format(word_to_guess))
            break

def main():
    while True:
        play_game()
        restart = input("\nWould you like to play again? (y/n): ").strip().lower()

        if restart == 'n':
            print("Thank you for playing. Exiting....")
            break
        elif restart != 'y':
            print("Invalid input. Exiting game.")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")