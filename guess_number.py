number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

guess_left = 5
if int(guess) != number:
      if int(guess) > number:
        print("Your guess was higher than the expected number")
      if int(guess) < number:
        print('Your guess was lower than the expected number')



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
    guess_left -= 1
    print(f'{guess_left} more guesses left')
    if guess_left == 0:
      break
    
    if int(guess) != number:
      if int(guess) > number:
        print("Your guess was higher than the expected number")
      if int(guess) < number:
        print('Your guess was lower than the expected number')
