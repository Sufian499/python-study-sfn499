# Guess the number (computer)
import random
def computer_guess(x,y):
    loop = True
    while loop == True:
        try_num = random.randint(x,y)
        feed = input(f"Is {try_num} to high (H), too low (L) or correct (C)?? ").lower()
        if feed == 'c' or x == y:
            print(f"Correct. The computer guessed your number, {try_num}.")
            loop = False
        elif feed == 'h':
            y = try_num -1
        elif feed == "l":
            x = try_num +1
        else:
            print("???")
    
def main():
    computer_guess(1,100)
    
if __name__ == "__main__":
    main()