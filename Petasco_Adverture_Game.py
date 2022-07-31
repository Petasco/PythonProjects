name = input("ENTER YOUR NAME:  ").upper()
print("<============= WELCOME",name,"TO PETASCO ADVERTURE GAME ==================>")

user_options = ["start", "quit"]
while True:
    play = input("TYPE [START] TO START OR [QUIT] TO QUIT: ").lower()
    if play not in user_options:
        print("INVALID OPTION, TYPE [START/QUIT] NEXT TIME!")

    elif play == 'quit':
        quit()

    elif play == 'start':
        answer = input("YOU ARE ON DEAD ROAD,DO YOU WANT TO TAKE LEFT OR RIGHT? ").lower()
        if answer == 'left':
            print("GREAT CHOICE")
            answer == input("BUT YOU ARE AT A RIVER SIDE, DO YOU WANT TO SWIM ACROSS OR WALK AROUND? [swim/walk]: ").lower()
            if answer == 'swim':
                print("YOU ARE SWIMMING NOW, BE CAREFUL OF ALLIGATORS")
                answer == input("YOU HAVE ENCOUNTERED AN ALLIGATOR, DO YOU WANT TO SHOOT? [yes/no]: ").lower()
                if answer == 'no':
                    print("OOPs, YOU GOT EATEN BY THE ALLIGATOR")
                    print("YOU LOST")
                    print("!==================! GOOD LUCK NEXT TIME !====================!")
                elif answer == 'yes':
                    print("CONGRATS, YOU HAVE KILLED THE ALLIGATOR")
                    answer == input("DO YOU WANT TO CONTINUE SWIMMING? [yes/no]: ").lower()
                    if answer == 'no':
                        print("OOPs! YOU GOT SANK")
                        print("YOU LOST")
                        print("!================! CONTINUE SWIMMING NEXT TIME TO WIN !===============!")
                    elif answer == 'yes':
                        print("CONGRSTS, YOU HAVE MADE IT TO THE OTHER END OF THE RIVER")
                        answer == input("YOU HAVE SEEN A BOX, DO YOU WANT TO OPEN IT? [yes/no]: ").lower()
                        if answer == 'no':
                            print("OH SORRY, YOU HAVE MISSED THE GOLD")
                            print("YOU LOST")
                            print("!================! NEXT TIME OPEN THE BOX FOR THE GOLD !===============!")
                        elif answer == 'yes':
                            print("CONGRATS", name, "YOU HAVE FOUND THE GOLD")
                            print("YOU WON")
                            print("!=$$$$$$$$$$$$$$$$$$=! ENJOY YOUR WEALTH !=$$$$$$$$$$$$$$$$$$$$=!")
                        else:
                            print("6.OOPs! INVALID OPTION")

                else:
                    print("OOPs!, INVALID CHOICE")
            elif answer == 'walk':
                print("YOU NOW WALKING AROUND RIVER")
                answer == input("YOU HAVE MET A LION, DO YOU WANT TO SHOOT OR RUN? [shoot/run]: ").lower()
                if answer == 'run':
                    print("OH SORRY, YOU GOT EATEN BY THE LION BECOS YOU COULDN'T RUN FASTER")
                    print("!================! NEXT TIME RUN FASTER TO SAVE YOUR LIFE !===============!")
                elif answer == 'yes':
                    print("CONGRATS", name, "YOU HAVE KILLED THE LION")
                    answer == input("SEEMS YOU ARE EXHUSTED, DO WANT TO WANT TO CONTINUE WALKING OR REST? [walking/rest]: ").lower()
                    if answer == 'rest':
                        print("OH SORRY, WHILE YOU WERE RESTING, YOUR OPPONENT FOUND THE GOLD")
                        print("YOU LOST")
                        print("!================! NEXT TIME DON'T WASTE TIME RESTING !===============!")
                    elif answer == 'walking':
                        print("GREAT! YOU HAVE COVERED A LOT OF MILES, KEEP WALKING")
                        answer == input("YOU HAVE SEEN A BOX, DO YOU WANT TO OPEN IT? [yes/no]: ").lower()
                        if answer == 'no':
                            print("OH SORRY!, YOU HAVE MISSED THE GOLD")
                            print("YOU LOST")
                            print("!================! NEXT TIME OPEN THE BOX FOR THE GOLD !===============!")
                        elif answer == 'yes':
                            print("CONGRATS", name, "YOU HAVE FOUND THE GOLD")
                            print("YOU WON")
                            print("!=$$$$$$$$$$$$$$$$$$=! ENJOY YOUR WEALTH !=$$$$$$$$$$$$$$$$$$$$=!")
                        else:
                            print("1.OOPs! INVALID OPTION")
                    else:
                        print("2.OOPs! INVALID OPTION")
                else:
                    print("3.OOPs! INVALID OPTION")
            else:
                print("4.OOPs! INVALID OPTION")
    # the right option section
        elif answer == 'right':
            print("GREAT OPTION")
            answer == input("BUT YOU HAVE REACHED A BRIDGE, DO YOU WANT TO CROSS OR TURN BACK? [cross/back]:" ).lower()

        else:
            print("INVALID OPTION, TYPE [LEFT/RIGHT] NEXT TIME!")

    else:
        print()