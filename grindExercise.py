#Name: Filip Skotarski
#Date: 12/13/2016
#Course: ICS4U-1
#Program Description: This program will let a user create their own work out plan/schedule so they'll be ready to get big
#Program Name: Culminating Activity, Grind Time

####################################################################################
####################################################################################

class Exercise:
    
    allReps = [] #Create an empty array to store all reps
    
    def __init__(self, name, reps, sets, lowering, pauseMid, lifting, pauseEnd, rest): #When initializing an object, create an Exercise with these attributes
        
        #Main exercise info
        self.name = name
        self.reps = reps 
        self.sets = sets 
        
        #Tempo values
        self.lowering = lowering
        self.pauseMid = pauseMid
        self.lifting = lifting
        self.pauseEnd = pauseEnd
        
        #Resting between sets in seconds
        self.rest = rest
        
        #Every rep of each exercise
        self.allReps.append(reps)
        
    
    def read(self): #create a function that returns a string of values
        return str(str(self.name) + ': ' + str(self.sets) + ' sets of ' + str(self.reps) + ' reps with tempo: [' + str(self.lowering) + ', ' + str(self.pauseMid) + ', ' + str(self.lifting) + ', ' + str(self.pauseEnd) + '] and rest for ' +str(self.rest) + ' seconds')
    
    #Recursively sum all reps in the exercise
    def sum(self):
        if len(self.allReps) == 1: #base case
            return self.allReps[0]
        else: #recursive call
            return self.allReps[0] + sum(self.allReps[1:])