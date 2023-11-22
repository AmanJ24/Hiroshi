import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
      |
      |
      |
========= '''
,
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ['Aman', 'Naman', 'Hello', 'World']

chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"  

end_of_game = False
lives = 6
stage_len = 0


while end_of_game == False:
    if lives > 0:
        guess = input("Guess the letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:    
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            stage_len += 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[stage_len])
        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")
    else:
        print("Game Over!")
        break       