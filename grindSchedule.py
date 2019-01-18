#Name: Filip Skotarski
#Date: 12/13/2016
#Course: ICS4U-1
#Program Description: This program will let a user create their own work out plan/schedule so they'll be ready to get big
#Program Name: Culminating Activity, Grind Time

####################################################################################
####################################################################################

#All imports here
from datetime import datetime #import date and time
from grindExercise import Exercise #import class from grindExercise Module
import random #import random number generator

####################################################################################
#Library of exercises grouped by difficulty
####################################################################################

#Shoulder exercises
shoulderBeginner = ['Front Raise', 'Lateral Raises', 'Bent Over Rear Delt Raise']
shoulderIntermediate = ['Deltoid Rows', 'Face Pulls', 'Machine Shoulder Press']
shoulderAdvanced = ['Dumbbell Shoulder Press', 'Barbell Shoulder Press', 'Arnold Dumbbell Press']
shoulders = [shoulderBeginner, shoulderIntermediate, shoulderAdvanced] #2D Array

#Chest exercises
chestBeginner = ['Seated Chest Press', 'Seated Upright Flys', 'Machine Decline Press']
chestIntermediate = ['Flat Dumbbell Press', 'Incline Dumbbell Press', 'Cable Flys']
chestAdvanced = ['Flat Bench Press', 'Incline Bench Press', 'Decline Bench Press', ]
chest = [chestBeginner, chestIntermediate, chestAdvanced] #2D Array
    
#Back exercises
backBeginner = ['Pull Ups', 'Chin Ups', 'Dumbbell Bent Over Reverse Flys', 'Upright Row']
backIntermediate = ['Dumbbell Bent Over Rows', 'Barbell Bent Over Rows', 'Close-Grip Pull-Down']
backAdvanced = ['Deadlift', 'Rack Pulls', 'Lat Pull Down']
back = [backBeginner, backIntermediate, backAdvanced] #2D Array

#Arms exercises
armsBeginner = ['Barbell Curls', 'Dumbbell Curls', 'Tricep Extensions'] 
armsIntermediate = ['Tricep Rope Extensions', 'Bicep Cable Curls', 'Dips']
armsAdvanced = ['Concentrated Curls', 'Skull Crushers', 'Close Grip Barbell Bench Press']
arms = [armsBeginner, armsIntermediate, armsAdvanced] #2D Array

#Core exercises
coreBeginner = ['Sit Ups', 'Crunches', 'In & Out Crunches', 'Bird Dog', 'Decline Crunches']
coreIntermediate = ['Weighted Crunches', 'Reverse Crunches', 'Weighted Decline Crunches']
coreAdvanced = ['Cable Twist', 'Barbell Hip Thrust', 'Dumbbell Suitcase Hold']
core = [coreBeginner, coreIntermediate, coreAdvanced] #2D Array

#Legs exercises
legsBeginner = ['Body Weight Squats', 'Body Weight Lunges', 'Calf Raises', 'Leg Extensions', 'Leg Curls']
legsIntermediate = ['Dumbbell Lunges', 'Kettle Squat', 'Weighted Calf Raises', 'Leg Press']
legsAdvanced = ['Barbell Back Squat', 'Barbell Front Squat', 'Romanian Deadlift']
legs = [legsBeginner, legsIntermediate, legsAdvanced] #2D Array

divider = '---------------------------------------------------------------------------------------' #create a variable that holds string

####################################################################################
#End of library
####################################################################################

class Schedule:
    
    #Default attribute values on creation
    def __init__(self, days, exp, weight, conditioning):
        
        #Schedule attributes with default values and creation date/time
        dt = datetime.now()
        dt = ('Created on: ' + str(dt))
        
        #Values will determine routine creation algorithm
        self.days = days
        self.exp = exp
        self.weight = weight
        self.conditioning = conditioning
        self.arrayOfRoutines = []
        
        ###############################################################################
        #Algorithm being broken down before finalized in createRoutines
        #Experience defaults at 'Beginner'
        self.exerciseRow = 0
        
        #Tempo, rest and reps/sets determined on Schedule creation, default values
        self.tempo = [2, 0, 4 , 0]
        self.rest = 45
        self.sets = 3
        self.reps = 10
        ###############################################################################

        #Collection of routines determined by algorithm, arrayOfRoutines is 2D
        self.arrayOfRoutines.append(dt)
        self.arrayOfRoutines.append('\n' + divider)
        
        #According to Schedule parameters, adjust experience and intensity
        self.determineExp()
        self.determineInt()
        
        #Create the routines and put it into arrayOfRoutines
        self.createRoutines()
    
    #Main functions
    #Creates an array of routines, which makes up the Schedule
    #Routines will have an array of Exercises
    #Routines will be named(i.e. "Leg Day"), with a date of the week to do it    
    def createRoutines(self):
        
        emptyExercise = Exercise('', 0, 0, 0, 0, 0, 0, 0)
        
        #Full body workout
        if self.days == 1:
            print('\nCreating 1 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Full Body Workout')
            routine.append(Exercise(random.choice(shoulders[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(chest[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(back[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(arms[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(core[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(legs[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
        
        #Push/Pull & Legs/Core
        elif self.days == 2:
            print('\nCreating 2 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push & Pull')
            routine.append(Exercise(random.choice(shoulders[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(chest[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(back[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(random.choice(arms[self.exerciseRow]), self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Legs & Core')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
        
        #Push/pull/legs split
        elif self.days == 3:
            print('\nCreating 3 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Pull')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 3')
            routine.append('Legs & Core')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
        
        #Push/pull/legs/arms&core
        elif self.days == 4:
            print('\nCreating 4 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Pull')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 3')
            routine.append('Legs')
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 4')
            routine.append('Arms & Core')
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
            
        #Push/pull/legs/arms/core
        elif self.days == 5:
            print('\nCreating 5 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Pull')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 3')
            routine.append('Legs')
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 4')
            routine.append('Arms')
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 5')
            routine.append('Core')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
        
        #Push/pull/legs/arms/shoulders/core
        elif self.days == 6:
            print('\nCreating 6 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push')
            routine.append(Exercise(chest[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(chest[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(chest[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(chest[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Pull')
            routine.append(Exercise(back[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(back[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(back[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(back[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 3')
            routine.append('Legs')
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(legs[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(legs[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(legs[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 4')
            routine.append('Arms')
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(arms[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(arms[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(arms[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 5')
            routine.append('Core')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(core[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(core[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(core[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 6')
            routine.append('Shoulders')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(shoulders[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(shoulders[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(shoulders[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)
            
        #Push/pull/legs/arms/shoulders/core/cardio
        else:
            print('\nCreating 7 Day Week')
            routine = []
            routine.append('Day 1')
            routine.append('Push')
            routine.append(Exercise(chest[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(chest[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(chest[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(chest[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(chest[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(chest[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 2')
            routine.append('Pull')
            routine.append(Exercise(back[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(back[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(back[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(back[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(back[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(back[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 3')
            routine.append('Legs')
            routine.append(Exercise(legs[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(legs[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(legs[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(legs[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(legs[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(legs[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 4')
            routine.append('Arms')
            routine.append(Exercise(arms[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(arms[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(arms[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(arms[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(arms[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(arms[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 5')
            routine.append('Core')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(core[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(core[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(core[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(core[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 6')
            routine.append('Shoulders')
            routine.append(Exercise(shoulders[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(shoulders[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            #When there aren't enough exercises in the same level of experience, take some from others
            if self.exerciseRow == 0:
                routine.append(Exercise(shoulders[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            elif self.exerciseRow == 1:
                routine.append(Exercise(shoulders[0][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[2][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            else:
                routine.append(Exercise(shoulders[1][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
                routine.append(Exercise(shoulders[1][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            self.arrayOfRoutines.append(routine)
            
            routine = []
            routine.append('Day 7')
            routine.append('Cardio')
            routine.append('30 Minutes on Treadmill')
            routine.append(Exercise(core[self.exerciseRow][0], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][1], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(Exercise(core[self.exerciseRow][2], self.reps, self.sets, self.tempo[0], self.tempo[1] ,self.tempo[2], self.tempo[3], self.rest))
            routine.append(divider)
            routine.append('The total amount of reps: ' + str(emptyExercise.sum()))
            self.arrayOfRoutines.append(routine)            
        
    #Create a function that checks the user input to choose a row on the 2D array of exercises
    def determineExp(self):
        if self.exp == 'Intermediate': #check if value equals string
            self.exerciseRow = 1
        elif self.exp == 'Advanced': #check if value equals string
            self.exerciseRow = 2
        
    #Create a function to determine the intensity of the workout
    def determineInt(self):
        if self.weight == 'Gain Weight' and self.conditioning == 'Strength': #check if value equals string
            self.tempo = [3, 0, 1, 0]
            self.rest = 90
            self.sets = 5
            self.reps = 5
            
        elif self.weight == 'Lose Weight' and self.conditioning == 'Endurance': #check if value equals string
            self.tempo = [2, 1, 4, 1]
            self.rest = 30
            self.sets = 4
            self.reps = 15
        
    # After the Schedule object is created send it into this function to save it        
    def saveToFile(self, name):
        name = name + '.txt'
        through = False #checks to see if datetime is completely printed
        # Writes Schedule to text file
        with open(name, 'w') as f:
            for row in self.arrayOfRoutines:
                for element in row:
                    if element == 'Day 1':#Writes to new line and loop has gone through datetime
                        f.write('\n')
                        through = True
                    if (through and ((type(element) == Exercise))): #Writes to new line using function that converts Exercise object to string
                        f.write((element.read() + '\n'))
                    elif through: #writes the first line, involving datetime, properly, otherwise would print vertically
                        f.write(str(element) + '\n')
                    else: #Writes normally to file
                        f.write(str(element)) 
                
        f.close() #close the file