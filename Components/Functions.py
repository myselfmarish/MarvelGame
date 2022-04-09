from Components import Variables


def pointSystem(quest):
   
    x = input("Choose yes or no: ")
    if x == "yes" or x=="y":
        Variables.points =  Variables.points + 10
    elif x == "no" or x =="n":
         Variables.points =  Variables.points + 0
    elif x == "quit":
        quit()
    else :
        print("Error you've entered something else")
        print(Variables.questions[quest])
        pointSystem(quest)
   

def guessTheCharacter(points):
   
    if  Variables.points == 20:
         Variables.finalCharacter =  Variables.characters[3] #Thanos
    elif  Variables.points == 30:
         Variables.finalCharacter =  Variables.characters[4] #Deadpool
    elif  Variables.points == 40:
         Variables.finalCharacter =  Variables.characters[2] #Black Widow
    elif  Variables.points == 50:
         Variables.finalCharacter =  Variables.characters[1] #Iron Man
    elif  Variables.points == 60:
         Variables.finalCharacter =  Variables.characters[0] #Spider Man

    else:
        print ("Sorry, something went wrong. The computer can't guess. Please, try again.")
        quit()
    print("Your character is: ", Variables.finalCharacter)