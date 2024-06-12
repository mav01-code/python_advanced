import random

user=None

while True:
    rps={"r":'''
            ______
                ___)_
                (____)
                (_____)
                (____)
            ___(___)

            '''
         ,"p":'''
        ______
            ___)____
             _______)
             ________)
             _______)
        __________)

        ''',"s":'''

        _______
           ____)____
              ______)_
          _ __________)
          (____)
        __(___)

        '''}
    system = random.choice(list(rps.keys()))
    user=input("Please enter r, p, s or q to quit: ")

    if system==user:
        print("User move:", rps[user])
        print("System move:", rps[system])
        print("It's a tie!")
    elif(user=="r"):
        if(system=="p"):
            print("User move:", rps[user])
            print("System move:", rps[system])
            print("You lose!")
        elif(system=="s"):
            print("User move:", rps[user])
            print("System move:", rps[system]) 
            print("You win!")
    elif(user=="p"):
        if(system=="r"):
            print("User move:", rps[user])
            print("System move:", rps[system])
            print("You win!")
        elif(system=="s"):
            print("User move:", rps[user])
            print("System move:", rps[system])
            print("You lose!")
    elif(user=="s"):
        if(system=="r"):
            print("User move:", rps[user])
            print("System move:", rps[system])
            print("You lose!")
        elif(system=="p"):
            print("User move:", rps[user])
            print("System move:", rps[system])
            print("You win!")
    elif(user=="q"):
        print("You quit!")
        break
    else:
        print("You entered wrong input. Please try again.")