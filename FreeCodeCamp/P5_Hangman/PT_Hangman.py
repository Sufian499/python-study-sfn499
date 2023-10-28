# Hungman
import random
from wordlist import words
import string
def valid_word(words):
    word = random.choice(words) # Elegir un valor random de la lista.
    while "-" in word or ' ' in word: # Hay palabras con guiones y espacios, esas las filtramos con esta condición dentro de un bucle.
        word = random.choice(words) 
    return word.upper() # Que nos devuelva la palabra si ha cumplido la condición.

def hangman():
    word = valid_word(words) # Guardamos el valor que devuelve la función en una variable
    word_letters = set(word) # Guardamos las letras de la palabra en un set.
    alphabet = set(string.ascii_uppercase) # Creamos un set que contenga todas las letras del alfabeto
    letras_usadas = set() # Set para guardar las letras que usamos
    lives = 6 # Vidas
    # Mientras que la longitud del set que contiene las letras de la palabra sean mayor a 0 o tengamos más de 0 vidas se cumple el bucle while
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left.') # Printemos las vidas que tenemos
        # Lista que itera cada letra de la variable word con la siguiente condición:
        # Si la letra que esta iterando esta en las letras usadas, guarda la letra en esa posicion, si no pone un guión.
        word_list = [letter if letter in letras_usadas else "-" for letter in word] # Letter = iteración de cada letra de word
        print("current word: ",' '.join(word_list)) 
        # User input en uppercase
        user_letra = input("Guess letter: ")
        user_letra = user_letra.upper()
        # Si la letra forma parte del alfabeto hacemos la condición
        if user_letra in alphabet - letras_usadas:
            # Añadimos la letra en el set de letras_usadas
            letras_usadas.add(user_letra)
            if user_letra in word_letters:
                # Si la letra esta en el set de word, lo elimina de word.
                word_letters.remove(user_letra)
            else:
                # Si no esta quitamos una vida
                lives = lives - 1
                print("The letter is not in the word. Try again.")
        # Si ya hemos puesto la letra.
        elif user_letra in letras_usadas:
            print(f"Ya has usado la letra {user_letra}")
        # Mostramos las letras que hemos usado. La función ''.join une los valores de una lista en una string.
        print("You have used these letters: ", ' '.join(letras_usadas))
        print()
    if lives > 0:
        print("The word is: ",' '.join(word))    
        print("Wow, ganaste :O")
    else:
        print("You lost.")
        print("The word is: ",' '.join(word))
def main():
    hangman()
    
if __name__ == "__main__":
    main()