import random
print("---------------------------------------------------------")
print("~~~~~~ WELCOME TO PETASCO ROCK/PAPER/SCISSORS GAME ~~~~~")
print("~~~~~~~~~~~~~~~~ PLAY  WITH  PETASCO ~~~~~~~~~~~~~~~~~")
print("---------------------------------------------------------")


user_score = 0
petasco_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("TYPE ROCK/PAPER/SCISSORS OR Q TO QUIT: ").lower()
    if user_input == "q":
        quit()
        break
    if user_input not in options:
        continue

    random_option = random.randint(0, 2)
    petasco_pick = options[random_option]
    print("Petasco Picks", petasco_pick + ".")

    if user_input == "rock" and petasco_pick == "scissors":
        print("<=**********=> CONGRATS! YOU WON! <=*****************=>")
        user_score += 1

    elif user_input == "paper" and petasco_pick == "rock":
        print("<=**********=> CONGRATS! YOU WON! <=*****************=>")
        user_score += 1

    elif user_input == "scissors" and petasco_pick == "paper":
        print("<=**********=> CONGRATS! YOU WON! <=*****************=>")
        user_score += 1

    else:
        print("<=**********=> OOPs! YOU LOST! <=*****************=>")
        petasco_score += 1

    print("YOU WON ", user_score, "TIMES")
    print("PETASCO WON", petasco_score, "TIMES")
    print("<=*************-> PLAY AGAIN! <-************************=>")
print("--------- THANK YOU FOR PLAYING WITH PETASCO ------------")