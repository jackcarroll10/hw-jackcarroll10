

import random
global credits
credits = 10
all_scores = []



def game_intro():
    print('Welcome to the Guessing Game!')
    print('Enter a three-digit number between 100-999')
    print('Earn credits by winning with fewer guesses')
    print('The game will give you hints')

def split(word):
    return [char for char in word]


def matches(i):
    common_digits = 0
    guess_string = str(i)
    answer_string = str(answer)
    guess_string_list = split(guess_string)
    answer_string_list = split(answer_string)
    for i in guess_string_list:
        if i in answer_string_list:
            common_digits += 1
    print('Guess and answer have {} digits in common'.format(common_digits))

def statistics():
    if len(all_scores) == 0:
        return('No games have been played')
    else:
        print('Total games:', len(all_scores))
        print('Total guesses:', sum(all_scores))
        print('Your average score is', sum(all_scores) / len(all_scores))
        print('Your best score was', max(all_scores))
        print('You have', credits, 'credit(s)')

def check_range(i):
    while i:

        try:
            i = int(i)
            if (100 <= i <= 999):
                return True
        except ValueError:
            return False
            print('Invalid Input')
    else:
        return('Invalid Input')

def guessing_game():
    global answer
    global credits
    answer = random.randint(100, 999)
    print(answer)
    guesses_count = 0
    guess = 0
    guess = input('Input a three-digit number from 100-999')
    credits -= 5
    while credits >= 0:
        if check_range(guess):
            if int(guess) > int(answer):
                print('Try a lower number')
                matches(guess)
                guesses_count += 1
                guess = input('Guess again')
                check_range(guess)
            if int(answer) > int(guess):
                print('Try a higher number')
                matches(guess)
                guesses_count += 1
                guess = input('Guess again')
            else:
                guess = int(guess)
                guesses_count += 1
                print('You guessed it!')
                if guesses_count < 5:
                    credits += 20
                elif (5 <= guesses_count <= 10):
                    credits += 10
                else:
                    credits = credits
                print('Credits:', credits)
                all_scores.append(guesses_count)


                end_input = input('Play again?')
                if end_input == False:
                    print('Goodbye!')
                else:
                    end_input = str(end_input)
                    if (end_input[0] == 'Y') or (end_input[0] == 'y'):
                        guessing_game()
                    else:

                        print("Goodbye!")
                        statistics()
                        break


    else:
        print('Not enough credits!')




game_intro()
guessing_game()