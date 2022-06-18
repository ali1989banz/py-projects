import random

userWins=0
computer=0
options=["rock","paper","scissors"]
while True:
    userInput=input("type Rock/Paper/Scissors or Q to quit\n").lower()

    if userInput == "q":
        break
    if userInput not in options:
        print("this is not avilable option please try agin")
        continue

    randomNumber=random.randint(0,2)
    # rock:0 , paper:1 , scissor:2
    computerPick=options[randomNumber]
    print(f"computer picked {computerPick}.")

    if userInput == "rock" and computerPick =="scissors":
        print("you won!")
        userWins+=1

    elif userInput == "paper" and computerPick =="rock":
        print("you won!")
        userWins+=1

    elif userInput == "scissors" and computerPick =="paper":
        print("you won!")
        userWins+=1
    elif userInput == computerPick:
        print("equal")

    else:
        print("you lost!")
print(f"your score is {userWins}")
print("goodbye")