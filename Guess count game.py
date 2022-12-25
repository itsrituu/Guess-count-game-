import random
import time
print("Welcome to guesing game.Please guess a number between 1 and 100")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("what is your guess?:"))
correct_number = random.randint(1,100)
guess_cout = 0
while guess != correct_number:
  guess_cout += 1
  if guess < correct_number:
    guess = int(input("Wrong yon need to guess higher, What is you guess:"))
  else:
    guess = int(input("Wrong yon need to guess lower, , What is you guess:"))
print(f"The right answer was {correct_number}.It took you {guess_cout} guesss")
