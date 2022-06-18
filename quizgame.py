print("my first quiz game ")

playing = input("do you want play quiz game? ")

if playing.lower() != "yes":
    quit()

print("okay let's play :)")


score = 0


answer = input("what dose cpu stand for? ")

if answer.lower() == "central processing unit":
    score+=1
    print("correct!")
else:
    print("incorrect")

answer = input("what dose GPU stand for? ")

if answer.lower() == "graphic processing unit":
    score+=1
    
    print("correct!")
else:
    print("incorrect")
    
answer = input("what dose ram stand for? ")

if answer.lower() == "random access memory":
    score+=1
    print("correct!")
else:
    print("incorrect")
    
answer = input("what dose psu stand for? ")

if answer.lower() == "power supply":
    score+=1
    print("correct!")
else:
    print("incorrect")
    
print(f"you got {score} questions correct")
print(f"you got {(score/4) * 100}%")