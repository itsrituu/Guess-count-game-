guess = int(input("what is your guess?:"))
correct_number = 5
guess_cout = 0
while guess != correct_number:
  guess_cout += 1
  guess = int(input("what is your guess?:"))
print(f"The right answer was {correct_number}.It took you right {guess_cout} guesss")