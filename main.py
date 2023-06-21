number = 25000
attempt = 1

while True:
  guess_number=int(input("Please enter the number between 0 and 1000000: "))
  if guess_number < 0:
    print("The number can not be negative")
    exit()
  if guess_number < number:
    print("too low. Try again!")
    attempt += 1
  elif guess_number > number:
    print("too high. Try again!")     
    attempt += 1
  elif guess_number == number:
    print("You guessed the right number. you are the winner! 🥳🥳")
    break
  else:
    print("number not found!")
print("it took", attempt, "attempts to guess the correct number!") 