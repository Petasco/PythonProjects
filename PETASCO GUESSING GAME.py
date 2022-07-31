import random
print("---------------------------------------------------------")
print("~~~~~~~ WELCOME TO PETASCO GUESSING GAME ~~~~~~~~~~~~~~~~")
print("---------------------------------------------------------")

range_limit = input("ENTER A NUMBER: ")
#convert the input to string if it is a digital
if range_limit.isdigit():
    range_limit = int(range_limit)
    if range_limit <= 0:
      print("OOPS! ENTER A NUMBER GREATER THAN 0 NEXT TIME")
      quit()
# end the program if the user enter a string
else:
    print("OOPS! ENTER A NUMBER NEXT TIME!!!")
    quit()

random_num = random.randint(0, range_limit)
guesses = 0

while True:
    guesses += 1
    user_guess = input("MAKE A GUESS: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    # end the program if the user enter a string
    else:
        print("OOPS! ENTER A NUMBER NEXT TIME!!!")
        continue
    if user_guess == random_num:
        print("CONGRATS, YOU GOT IT")
        break
    else:
        print("+++++++++++++ OOPS!!! ++++++++++++++")

print("YOU GOT IN", guesses, "GUESSES")