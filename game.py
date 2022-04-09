from Components import Variables, Functions


print("██████► ◄██████ Marvel YES or NO Game ██████► ◄██████")
print(" Choose between these Marvel characters: ")
print(*Variables.characters,sep=", ")


counter = 0
while(counter<len(Variables.questions)):
    print(Variables.questions[counter])
    Functions.pointSystem(counter)
    print("Points: ",Variables.points)
    counter=counter+1


Functions.guessTheCharacter(Variables.points)

