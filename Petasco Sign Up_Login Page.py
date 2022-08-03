print("~~~~~~~~~~~~~~=> WELCOME TO PETASCO GH <=~~~~~~~~~~~~~~~~~~~")
print("____________________________________________________________")
print("~~~~~~~~~~~~~~=> SIGN UP <=~~~~~~~~~~~~~~~~~~~")
print("____________________________________________________________")

firstName = input("ENTER YOUR FIRST NAME:  ").upper()
lastName = input("ENTER YOUR LAST NAME:  ").upper()
username = input("ENTER YOUR USERNAME:  ")
email = input("ENTER YOU EMAIL:  ")
password = input("ENTER PASSWORD:  ")
con_password = input("CONFIRMED PASSWORD: ")

if password != con_password:
    print("***************= PASSWORD MISMATCHED! =*****************")
else:
    print("FIRST NAME:", firstName)
    print("LAST NAME: ",lastName)
    print("EMAIL: ",email)
    submit = input("DO YOU WANT TO SUBMIT?[Yes/No] ").lower()
    if submit == 'no':
        print("----------------> RE-ENTER YOUR DETAILS <--------------------")
    elif submit == 'yes':
        print("~~~~~~~~~~~~~~=> SIGN UP SUCCESSFULLY! <=~~~~~~~~~~~~~~~~~~~")
        print("____________________________________________________________")
        print("------------------------------------------------------------")
        # LOGIN FORM
        print("~~~~~~~~~~~~~~~~~~~~~~~=> LOGIN  <=~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            Username = input("ENTER YOUR USERNAME:  ")
            Password = input("ENTER YOUR PASSWORD:  ")
            if Username != username and Password != password:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!-> INCORRECT LOGIN <-!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue
            else:
                print("~~~~~~~~~~~~~~=> LOGIN SUCCESSFULLY! <=~~~~~~~~~~~~~~~~~~~")
                break

    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!-> ERROR <-!!!!!!!!!!!!!!!!!!!!!!!!!!!!")