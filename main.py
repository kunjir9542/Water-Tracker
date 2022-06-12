measurement = input("Before we begin, do you use the Customary or Metric system (C/M)")
global waterDrank
global goal
waterDrank = 0

if measurement == "C":
    print("units set to Customary")
    units = "fl oz."

elif measurement == "M":
    print("units set to Metric")
    units = "ml"

print("--------------------------------------------------------------------")



def mainMenu():
    print("--------------------------------------------------------------------")
    global waterDrank
    choice = input("Would you like to add water you drank,edit your goal, or clear your progress? (A/E/C)")
    if choice == "A":
        addWater()
    if choice == "E":
        editGoal()
    if choice == "C":
        waterDrank = 0
        print("Cleared Progress")
        mainMenu()

def addWater():
    print("--------------------------------------------------------------------")
    waterAdded = input("Enter the amount of water you drank in " + units)
    if (waterAdded.isnumeric()):
        global waterDrank
        waterDrank += int(waterAdded)
        checkGoal()
        mainMenu()
    else:
        print("Please enter a number")
        addWater()


def editGoal():
    print("--------------------------------------------------------------------")
    global goal
    goal = input("Please set a goal for yourself to drink for the day")
    print("Goal Set. You can always edit this later")
    mainMenu()

def checkGoal():
    global waterDrank
    if waterDrank >= int(goal):
        print("Goal Reached!!")
        mainMenu()
    else:
        print("You are " + str(waterDrank) + " / " + goal + " toward your goal")

editGoal()
mainMenu()
