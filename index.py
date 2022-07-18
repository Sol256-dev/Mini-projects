print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("lets play")
score = 0

answer = input("What does CPU Stand for? ")

if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU Stand for? ")

if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM Stand for? ")

if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("your score is " + str(int((score/3)*100)) + "%")

the end
