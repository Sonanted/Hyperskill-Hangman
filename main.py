import random
print('H A N G M A N')
game_start = ''
while game_start != 'exit' or game_start != 'play':
    game_start = input('Type "play" to play the game, "exit" to quit:')
    if game_start == 'exit':
        break
    if game_start == 'play':
        words = ['python', 'java', 'kotlin', 'javascript']
        random.shuffle(words)
        hidden_word_len = len(words[0])
        hidden_letters_set = set(words[0])
        letters_set = set()
        lives = 8
        while lives > 0:
            guessed_word = list(words[0])
            for x in range(hidden_word_len):
                if guessed_word[x] in hidden_letters_set:
                    guessed_word[x] = '-'
            guessed_word = ''.join(guessed_word)
            if len(hidden_letters_set) == 0:
                print('You guessed the word', guessed_word, '!')
                break
            print('')
            print(guessed_word)
            letter = input('Input a letter: ')
            if letter in hidden_letters_set:
                hidden_letters_set.remove(letter)
                letters_set.add(letter)
            elif letter in letters_set:
                print('You already typed this letter')
            elif len(letter) != 1:
                print('You should print a single letter')
            elif not letter.isalpha() or letter.isupper():
                print('It is not an ASCII lowercase letter')
            else:
                print('No such letter in the word')
                letters_set.add(letter)
                lives -= 1
        if lives == 0:
            print('You are hanged!')
        else:
            print('You survived!')
