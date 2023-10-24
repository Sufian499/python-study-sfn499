# Guess the number (computer)
import random
def guess(x):
    rand_num = random.randint(1,x)
    loop = True
    while loop == True:
        guess_num = int(input("Guess a number between 1 and 10: "))
        if guess_num < rand_num:
            print("Sorry, guess again. Too low.")
        elif guess_num > rand_num:
            print("Sorry, guess again. Too high.")
        else:
            loop = False
            print(f"Congrats king. You have guessed the number {guess_num} correctly!!! :)")

def main():
    guess(10)
    
if __name__ == "__main__":
    main()