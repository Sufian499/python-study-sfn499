# Piedra papel y tijera
import random

# def play_rps():
#     options_computer = ["r","p","s"]
#     computer_choice = random.choice(options_computer)
#     user_option = input("'r' roca, 'p' papel, 's' tijeras: " )
#     if (user_option == "r" and computer_choice == "s") or (user_option == "s" and computer_choice =="p") or (user_option == "p" and computer_choice =="r"):
#         print(f"{computer_choice}\nYou won!")
#     elif (user_option == "r" and computer_choice =="p") or (user_option == "p" and computer_choice =="s") or (user_option == "s" and computer_choice =="r")
#         print(f"{computer_choice}\nYou lost!")
#     else:
#         print(f"{computer_choice}")
#         print("Empate")

def win(user, computer): # Función para definir las condiciones de victoria, si alguna se cumple devuelve un booleano.
    if (user == "s" and computer == "p") or (user == "p" and computer == "r") or (user == "r" and computer == "s"):
        return True
def play(): # Función que ejecuta el juego.
    # El ordenador tiene una array donde elije una de las 3 opciones de forma random.
    options_computer = ["r","p","s"]
    computer_choice = random.choice(options_computer)
    # Pregunatmos el input del user y mostramos también un output del pc. Si tienen el mismo valor, que nos devuelva una string indicanonos un empate.
    user_option = input("'r' roca, 'p' papel, 's' tijeras: " )
    print(computer_choice)
    if user_option == computer_choice:
        return "Empate."
    # Ejecutamos la anterior función y si devuelve True nos indicará que ganamos
    if win(user_option,computer_choice):
        return "u won :)"
    # Si no se ejecuta ninguna otra función que nos devuelva una string inidcando que hemos perdido.
    return "u lost XD"

def main():
    # play_rps()
    print(play())
    
if __name__ == "__main__":
    main()