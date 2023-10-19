Correct_password = "DEV@2023"
attempts_remaining = 3

while attempts_remaining > 0:
    password = input("Enter the password : ")

    if password== Correct_password:
        print("Bonjour !")
        break

    else:
        attempts_remaining -= 1
        if attempts_remaining > 0:
            print("The password you entered is incorrect !. You have ", attempts_remaining , "attempts left.")

        else:
            print('the name of favorite anime ??')
            question_secrete = input("The password you entered is incorrect. Answer the secret question : ")
 
    print("Bonjour !")
