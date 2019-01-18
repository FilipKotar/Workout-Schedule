#Name: Filip Skotarski
#Date: 12/13/2016
#Course: ICS4U-1
#Program Description: This program will let a user create their own work out plan/schedule so they'll be ready to get big
#Program Name: Culminating Activity, Grind Time

####################################################################################
####################################################################################

#All imports here
import sys #import a quit library
from grindSchedule import Schedule #import Schedule class from grindSchedule.py
from builtins import str

####################################################################################
####################################################################################

class Menu:

    def __init__(self): #on creating a menu object, execute
        print('==========================')
        print('  Welcome to Grind Time!  ') #print test to welcome the user
        print('==========================')

        program = True #assign True to program to start the program

        while program: #when program is true, execute the following code
            #print users options
            print('\n------------------------')
            print("'S' - start the program")
            print("'H' - open the help menu")
            print("'Q' - quit the program")
            print('------------------------')
            userInput = str(input('Enter an Option: ')) #takes user input converts it into a string to compare in statements


            if userInput == 'S' or userInput == 's': #if the user inputs S or s, execute
                beginGrind = True #Set 'beginGrind' to true

                while beginGrind: #When 'beginGrind' is true, execute the following code

                    #print users options
                    print('\n--------------------------------------')
                    print("'1' - Create a new schedule")
                    print("'2' - Open a previously made schedule")
                    print("'3' - Enter weights used and calculate max volume")
                    print("'B' - back to the main menu")
                    print('--------------------------------------')

                    pickOption = str(input('Enter another Option: ')) #takes user input converts it into a string to compare in statements

                    #User creates their own schedule
                    if pickOption == '1': #If user inputs 1, execute
                        askUser() #Call askUser function to get all the input that is required to make the schedule

                    #User opens a previously made schedule
                    elif pickOption == '2': #if user inputs 2, execute
                        fileName = '' #Create a variable for reading and writing text files
                        invalid = True #Assign True to invalid variable
                        while invalid: #while invalid is true, execute
                            fileName = str(input('What is the name of the text file?')) #get input from the user and turn it into a string
                            readFromFile(fileName) #print the text file the user enters
                            invalid = False #assign False to invalid

                        valid = True #assign True to valid
                        while valid: #while valid is True, execute
                            print('Would you like to print a certain day?') #print user guideline text
                            yesOrNo = str(input("Enter 'Y' for Yes: ")) #get user input and convert it into a string
                            yesOrNo = yesOrNo.capitalize() #Capitalize user input
                            if yesOrNo == 'Y': #if user input equals a string, execute
                                day = str(input('Which day?')) #get input and set it to a string
                                day.capitalize() #Capitalize string
                                if day == 'Day 1' or day == 'Day 2' or day == 'Day 3' or day == 'Day 4' or day == 'Day 5' or day == 'Day 6' or day == 'Day 7': #Check if user input equals any of these string values, if true, execute
                                    searchForDay(fileName, day) #Call function with 2 parameters
                                    valid = False #Assign False to valid
                                else: #if above doesn't execute, execute
                                    print('That day does not exist.') #print string
                            else:#if above doesn't execute, execute
                                valid = False #Assign False to valid

                    #User enters weights used in exercises to check the greatest volume of a single exercise
                    if pickOption == '3': #If user inputs 3, execute
                        print('\nEnter number for weight. Enter Q to quit.')
                        entering = True #set True to entering variable
                        weights = [0] #get the first value in weights
                        while entering: #when entering variable is true, execute
                            userInput = str(input('Enter weight: ')) #get user input and turn it into a string
                            if userInput != 'Q': #if user input doesn't equal 'Q', execute
                                weights.append(int(userInput)) #turn user input into an integer and append it into weights
                            else: #if above doesn't execute, execute
                                entering = False #Assign False to variable

                        reps = int(input('Enter reps completed: ')) #get input and turn it into an integer
                        calculateMaxVolume(weights, reps) #Call function with 2 parameters

                    #User goes back to the main program
                    elif pickOption == 'B' or pickOption == 'b': #if user inputs B or b, execute
                        beginGrind = False #assign False to beginGrind

                    else: #If other statements are false, execute
                        print('================================') #Print information


            elif userInput == 'H' or userInput == 'h': #if user inputs h, execute
                #print a help menu
                print('\nWelcome to the Help Menu')
                print('==========================================================================================================')
                print('This program will...')
                print('Create a personal workout schedule for the user')
                print('This workout schedule is created based on:')
                print('1. Days a week the user would like the workout')
                print('2. Their Level of experience')
                print('3. If they want to lose or gain weight')
                print('4. If they want to increase strength or endurance')
                print('PreCondition: user has to give input based on what they want out of their schedule.')
                print('the program runs data through the objects and generates a schedule based on this information')
                print("Additional information will be in the external document called, 'grindtime_README.txt'")
                print("Enter 'S' to start the program")
                print('==========================================================================================================')

            elif userInput == 'Q' or userInput == 'q': #if user inputs Q or q, execute
                print('\n==================================')
                print('May the God of Gains Bless You')
                print('               -=-    ')
                print('            (\  _  /) ')
                print('            ( \( )/ ) ')
                print('            (       ) ')
                print('              >   <  ')
                print('             /     \  ')
                print('              -._.-  ')
                print('==================================')
                sys.exit() #exit and turn off the program

            else: #if other statements are false, execute
                print('\nThat is not an option') #Print information


#Function for user input; get the user input to decide what kind of schedule they want
def askUser():

        #Temperary variables
        currentInput = 0 #Set variable to 0

        #More temporary variables for Schedule object
        days = 1 #Set variable to 1
        exp = '' #Empty string variable for temporary use
        weight = '' #Empty string variable for temporary use
        conditioning = '' #Empty string variable for temporary use


        invalid = True #Assign True to variable
        while invalid: #While invalid is true
            fileName = str(input('\nWhat would you like to name the text file? '))
            if fileName is not ('/' or '\'' or '|' or '?' or '<' or '>' or '*' or ':' or '"'):
                invalid = False #Assign False to invalid
            else: #if above doesn't execute, execute
                print('You cannot use symbols to name your text file.') #print

        #Check input of user and send it to Schedule object
        invalid = True #Assign True to variable
        while invalid:#While invalid is true
            currentInput = int(input('\nHow many days of the week would you like to work out? (1-7)\nEnter a Value: '))
            typ = type(currentInput)
            if typ == int and currentInput > 0 and currentInput < 8: #check and execute if true
                days = currentInput #set a variable equal to the users current input
                invalid = False #assign False to boolean
            else:
                print('Incorrect input.')

        invalid = True #Assign True to variable
        while invalid: #While invalid is true
            currentInput = int(input("\nWhat is your level of experience?\n'1' - Beginner\n'2' - Intermediate\n'3' - Advanced\nEnter a Value: ")) #get user input and turn it into a string
            typ = type(currentInput) #put the users input into a variable
            if typ == int: #if variable equals an int, execute
                if currentInput == 1: #check if user input equals a value
                    exp = 'Beginner' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                elif currentInput == 2: #check if user input equals a value
                    exp = 'Intermediate' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                elif currentInput == 3: #check if user input equals a value
                    exp = 'Advanced' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                else: #if above doesn't execute, execute
                    print('Incorrect input.') #print string
            else: #if above doesn't execute, execute
                print('Incorrect input.') #print string

        invalid = True #Assign True to variable
        while invalid: #While invalid is true
            currentInput = int(input("\nWould you like to lose or gain weight?\n'1' - Gain Weight \n'2' - Lose Weight\nEnter a Value: ")) #get user input and turn it into a string
            typ = type(currentInput) #put the users input into a variable
            if typ == int: #if variable equals an int, execute
                if currentInput == 1: #check if user input equals a value
                    weight = 'Gain Weight' #Set temporary variable to string
                    invalid = False#Assign False to invalid
                    pass
                elif currentInput == 2: #check if user input equals a value
                    weight = 'Lose Weight' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                else: #if above doesn't execute, execute
                    print('Incorrect input.') #print string
            else: #if above doesn't execute, execute
                print('Incorrect input.') #print string

        invalid = True #Assign True to variable
        while invalid: #While invalid is true
            currentInput = int(input("\nWould you like to increase strength or endurance?\n'1' - Strength\n'2' - Endurance\nEnter a Value: "))
            typ = type(currentInput) #put the users input into a variable
            if typ == int: #if variable equals an int, execute
                if currentInput == 1: #check if user input equals a value
                    conditioning = 'Strength' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                    pass
                elif currentInput == 2: #check if user input equals a value
                    conditioning = 'Endurance' #Set temporary variable to string
                    invalid = False #Assign False to invalid
                else: #if above doesn't execute, execute
                    print('Incorrect input.') #print string
            else: #if above doesn't execute, execute
                print('Incorrect input.') #print string

        userSchedule = Schedule(days, exp, weight, conditioning) #gather and send variables to schedule object
        userSchedule.saveToFile(fileName) #call class and send the filename to write to a file

#Create a function to read text and print from file
def readFromFile(name):
    name = name + '.txt' #make file name with user input
    with open(name, 'r') as f: #open file
        for line in f: #loop to print in file
            print(line.rstrip('\n')) #print from file
    f.close() #close file

#Linear search for the right block of text; the text under the day
def searchForDay(name, day):
    print('The day is: ' + day)
    name = name + '.txt'
    target = False
    divider = '---------------------------------------------------------------------------------------' #print variable with string
    print(divider) #print the variable with a string
    with open(name, 'r') as f:
        for line in f:
            #if end of day is reached, print divider then do not print anymore
            if divider in line and target:
                print(line.rstrip('\n'))
                target = False #Assign False to target

            #search for day until found, print
            if day in line or target:
                print(line.rstrip('\n'))
                target = True

    f.close() #close file

#User insertion sort to put the largest weight at the end of the array
def calculateMaxVolume(listOfWeights, reps):
    #Sorts the weights used for each exercise (in pounds), puts in order, then multiplies by reps
    for index in range(1,len(listOfWeights)):
        currentvalue = listOfWeights[index] #set current value equal to the value of index in the array of weights
        position = index #set position variable equal to index variable

        while position>0 and listOfWeights[position-1]>currentvalue: #while this statement is true, execute
            listOfWeights[position]=listOfWeights[position-1] #replaces the number with the one below/above
            position = position-1 #subtract 1 from the position variable each time it loops

        listOfWeights[position]=currentvalue #make current value equal the current position of the weights array


    volume = reps*(listOfWeights[len(listOfWeights)-1]) #Volume is total amount of weight lifted
    print('\nYour max volume is: ' + str(volume)) #Max volume is using the highest weight
