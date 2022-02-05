import random
import os
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
"YOU LOOSE"]


def read_data(filepath="./files/data.txt"):
    words = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    data = read_data(filepath="./files/data.txt")
    chosen_word_accent = random.choice(data)
    chosen_word_woaccent = chosen_word_accent.maketrans('áéíóú','aeiou')
    chosen_word = chosen_word_accent.translate(chosen_word_woaccent)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        #print(idx,letter)
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
        
    print("Reglas del juego: Debes utilizar solamente palabras \nSi entras números o dobles letras, el juego terminará")
    print("¡Adivina la palabra!")
    incorrect_tries = 0
    while True:
        print("Reglas del juego: Debes utilizar solamente palabras \nSi entras números o dobles letras, el juego terminará")
        print("¡Adivina la palabra!")
        os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("Rules: You must use letters, consonants and vowels, if you use numbers, the game will crash")
        print("Guess the word!")
        print(IMAGENES_AHORCADO[incorrect_tries])
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")
        letter = input("Enter a letter: ").strip().upper()
        assert letter.isalpha(), "You just can add letters"
            
        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        if letter not in chosen_word_list:
            incorrect_tries += 1
           
        if incorrect_tries == 7:
            print("You have lost the game :c")
            break


        
        if "_" not in chosen_word_list_underscores:
            winned_match = +1
            os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era", chosen_word)
            break
        

if __name__ == '__main__':
    run()
