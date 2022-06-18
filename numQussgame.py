import random

top_of_rang = input("type a number: ")

if top_of_rang.isdigit():
    top_of_rang = int(top_of_rang)

    if top_of_rang <= 0:
        print("please type number larger than 0 next time")
        quit()
else:
    print("please type number next time")
    quit()

random_number = random.randint(0,top_of_rang)

score = 0

while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        
    else:
        print("please type number next time")
        continue
    if user_guess == random_number:
        print("you got it!")
        print(f"you try for {score} times to get it")
        break
    else:
        score+=1
        print("you got it wrong")

