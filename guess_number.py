number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))


if guess == number:
   print("Congratulations! You guessed the right number.")
else:
   while guess != number:
    guess = (input("Sorry, Try again "))
    if guess == 'q':
      print(f"The number was {number}")
      break
    if int(guess) == number:
      print("Congratulations! You guessed the right number.")
      break

