# Hungman
import random
from wordlist import words
# def hm():
    
#     print(word)
#     len_word = len(word)
#     c_word = 0
#     array_word = create_array_word(word)
#     used_letters = []
#     lives = 3
#     # print(f'you have used these letters: ')    
#     while lives != 0:
#         letter = input("Guess letter: ")
#         used_letters.append(letter)
#         print("Current Word: ", end="")
#         for i in array_word:
#             for j in used_letters:
#                 if i == j:
#                     print(j,end=" ")
#                 else:
#                     print("-",end=" ")
        
#         print()
    
def valid_word(words):
    word = random.choice(words) # Elegir un valor random de la lista.
    while "-" in word or ' ' in word: # Hay palabras con guiones y espacios, esas las filtramos con esta condición dentro de un bucle.
        word = random.choice(words) 
    return word.upper() # Que nos devuelva la palabra si ha cumplido la condición.

def hangman():
    word = valid_word(words)
    word_letters = set(word)
    print(word_letters)
    
def main():
    hangman()
    
if __name__ == "__main__":
    main()