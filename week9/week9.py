import random
print("your life is in the line ")
def death():
    while True:
        random_number = random.randint(1, 100)
        attempts = 0
        while True:
            user_guess = int(input("guess the number or die: "))
            attempts += 1
            if user_guess == random_number:
                print("Congratulations! You live", attempts, "attempts.")
                break
            elif attempts == 3:
                print("your dead.")
                play_again = input("Want to play again bastard? (Y/N)")
                if play_again.upper() == "Y":
                    break
                else:
                    print("you live")
                    exit()
            else:
                print("die you bastard")
                        
    death()
