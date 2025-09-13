import random

print(
    'Welcome to Hangman! \nIn this game you need to guess machines hidden word by a single letter for each iteration.'
    ' \nFor each wrong guess program will draw a part of picture of a hangman so you have 4 attempts. '
    'There are only nouns and adjectives. Good luck!')


def hangman():
    a_hanged_man = ['_______',
                    ' |   |',
                    ' 0   |',
                    '/|\  |',
                    '/ \  |',
                    '     |',
                    ' ____|_____',
                    '|__________|']

    words = ['house', 'restaurant', 'godzilla', 'mouse', 'hangman', 'clothes', 'redhead', 'curse', 'locomotive',
             'wall', 'prototype',
             'crystal', 'syborg', 'stairs', 'calamity', 'relationship', 'pain', 'hospital', 'train',
             'blessing', 'car', 'random',
             'sister', 'mother', 'brother', 'goddess', 'mercy', 'fatal', 'gratitude', 'blood', 'heart', 'time', 'hour',
             'hero', 'letter']

    wrong_guesses = 0
    memorised_word = random.choice(words)
    letters_left = list(memorised_word)
    score_board = ['_'] * len(memorised_word)
    win = False
    cheater = False
    print('This word has', len(memorised_word), 'letters')

    while wrong_guesses < len(a_hanged_man) - 1:
        print('\n')
        user_input = input('Enter your suggested letter: ')

        if user_input.isalpha() is True:
            if len(user_input) == len(memorised_word) or len(user_input) == 1:
                if user_input == memorised_word:
                    score_board = user_input
                else:
                    for i in user_input:
                        if i.lower() in letters_left:
                            while i.lower() in letters_left:
                                character_index = letters_left.index(i.lower())
                                score_board[character_index] = i.lower()
                                letters_left.pop(character_index)
                        else:
                            wrong_guesses += 2
            else:
                print('\nCheating??? Nuh nonna work. Be gone.\n')
                cheater = True
                break

        elif user_input.isdigit() is True:
            print('\nNot a number, asshole\n')
        else:
            print('\nWTF is this\n')

        print('Word:   ')
        print(''.join(score_board))
        print('\nLose progression:   ')
        print('\n'.join(a_hanged_man[0: wrong_guesses]))

        if '_' not in score_board:
            print('\n\n\n\n\n\n\n\n\n\n\n\n')
            print('You won! The word is: ')
            print(memorised_word)
            win = True

            again_input = input('Again? \n')

            while again_input.lower() != 'no' or again_input.lower() != 'n' or again_input.lower() != 'nuh':
                again_input = input('Again? \n')

                if again_input.lower() == 'yes' or again_input.lower() == 'y' or again_input.lower() == 'yep':
                    hangman()
                else:
                    print('???')

    if cheater is False:
        if win is False:
            print('\n\n\n\n\n\n\n\n\n\n\n\n')
            print('\n'.join(a_hanged_man[0: wrong_guesses]))
            print('You lose! \nThe right answer was:\n{}'.format(memorised_word))

            again_input = input('Again? \n')

            while again_input.lower() != 'no' or again_input.lower() != 'n' or again_input.lower() != 'nuh':
                again_input = input('Again? \n')

                if again_input.lower() == 'yes' or again_input.lower() == 'y' or again_input.lower() == 'yep':
                    hangman()
                else:
                    print('???')


hangman()
