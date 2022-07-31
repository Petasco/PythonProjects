username = input("ENTER YOUR NAME: ").upper()
print("#############################################################################################")
print("<=============> HELLO " + username + ", WELCOME TO PETASCO QUIZ GAME <=================>")
print("#############################################################################################")
play_option = input("DO YOU WANT TO PLAY? ")
if play_option.lower() != "yes":
    quit()
print("OKAY! LET'S PLAY,GET READY!")

# question 1
score = 0
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF GUI? ")
if answer.lower() == "graphical user interface":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS GRAPHICAL USER INTERFACE")

# question 2
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [2] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF ICT? ")
if answer.lower() == "information and communication technology":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS INFORMATION and COMMUNICATION TECHNOLOGY ")

# question 3
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [3] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHO IS THE DEVELOPER OF PETASCO QUIZ GAME? ")
if answer.lower() == "diyouh peter":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS DIYOUH PETER")

# question 4
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [4] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF OS? ")
if answer.lower() == "operating system":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS OPERATION SYSTEM")

# question 5
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [5] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF SSD? ")
if answer.lower() == "solid state drive":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS SOLID STATE DRIVE")

# question 6
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [6] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE CAPITAL CITY OF GHANA? ")
if answer.lower() == "accra":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS ACCRA")

# question 7
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [7] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF USB? ")
if answer.lower() == "universal serial bus":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS UNIVERSAL SERIAL BUS")

# question 8
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [8] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("HOW MANY MONTHS ARE THERE IN TWO AND HALF YEARS? ")
if answer == "30":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS 30")

# question 9
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [9] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHICH YEAR DID GHANA GAINED INDEPENDENCE? ")
if answer == str(1957):
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS 1957")

# question 10
print("~~~~~~~~~~~~~~~~~~~~~~~~~ [10] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("WHAT IS THE FULL MEANING OF USA? ")
if answer.lower() == "united states of america":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")
    print("THE CORRECT ANSWER IS UNITED STATES OF AMERICA")

# total score
print("YOU GOT " + str(score) + " QUESTIONS CORRECT")
percentage = str((score/10) * 100)

percentage_score = print("YOU SCORED " + percentage +"%.")

percentage = float(percentage)
if percentage >= 80:
    print("GRADE : A")
    print("EXCELLENT JOB", username, "KEEP IT UP!")
elif percentage >= 75:

    print("GRADE : B+")
    print("GREAT JOB", username, "WELL DONE!")

elif percentage >= 70:
    print("GRADE : B")
    print("GOOD JOB", username, "KEEP LEARNING")

elif percentage >= 65:
    print("GRADE : C+")

elif percentage >= 60:
    print("GRADE : C")

elif percentage >= 55:
    print("GRADE : D+")

elif percentage >= 50:
    print("GRADE : D")

else:
    print("GRADE : E")
    print("SIT UP",username)
