## MAIN CODE V3: SW Integration test 1

## Python Initialization:
import numpy as np
import pandas as pd
import matplotlib

## Field Generator:
STEP=0
ob4 = [[37,30],['U']] #coordinated of the center cell & mooving direction U/D
ob31 = [[41,32],['R']] #coordinated of the center cell & mooving direction R/L
ob32 = [[52,40],['R']] #coordinated of the center cell & mooving direction R/L

field = np.genfromtxt('finalProjectMap.csv', delimiter=',')

# Obsticle Position Update Functions
def obstcl4(step):
    STEP=step
    if STEP%4==0:

        if ob4[1][0]=='U':
            print(ob4[0][0])
            
            if ob4[0][0]==0:
                ob4[1][0]='D'
                print(ob4[1][0])
                
            if ob4[0][0]>0: #if the "row" location is grather than 0
                
                if field[ ob4[0][0]-1 ][ ob4[0][1] ]==0 and field[ ob4[0][0]-1 ][ ob4[0][1]+1 ]==0 and field[ ob4[0][0]-1 ][ ob4[0][1]-1 ]==0: #if the path up is clear
                    
                    field[ ob4[0][0]][ ob4[0][1]-1 ]=0
                    field[ ob4[0][0]][ ob4[0][1] ]=0
                    field[ ob4[0][0]][ ob4[0][1]+1 ]=0
                    
                    field[ ob4[0][0]-1 ][ ob4[0][1]-1 ]=4
                    field[ ob4[0][0]-1][ ob4[0][1] ]=4
                    field[ ob4[0][0]-1][ ob4[0][1]+1 ]=4
                    ob4[0][0]=ob4[0][0]-1 #move up
                    
                if (field[ ob4[0][0]-1 ][ ob4[0][1] ]!=0 or field[ ob4[0][0]-1 ][ ob4[0][1]+1 ]!=0 or field[ ob4[0][0]-1 ][ ob4[0][1]-1 ]!=0) and ob4[0][0]!=0: #if the path up is not clear
                    ob4[1][0]='D'
            
        if ob4[1][0]=='D':

            print("moving down")
            print(ob4[0][0])
            
            if ob4[0][0]==(len(field)-2):
                ob4[1][0]='U'
                print(ob4[1][0])

            if field[ ob4[0][0]+1 ][ ob4[0][1] ]==0 and field[ ob4[0][0]+1 ][ ob4[0][1]+1 ]==0 and field[ ob4[0][0]+1 ][ ob4[0][1]-1 ]==0: #if the path down is clear

                field[ ob4[0][0]][ ob4[0][1]-1 ]=0
                field[ ob4[0][0]][ ob4[0][1] ]=0
                field[ ob4[0][0]][ ob4[0][1]+1 ]=0

                field[ ob4[0][0]+1 ][ ob4[0][1]-1 ]=4
                field[ ob4[0][0]+1][ ob4[0][1] ]=4
                field[ ob4[0][0]+1][ ob4[0][1]+1 ]=4
                ob4[0][0]=ob4[0][0]+1 #move down
                
            if (field[ ob4[0][0]+1 ][ ob4[0][1] ]!=0 or field[ ob4[0][0]+1 ][ ob4[0][1]+1 ]!=0 or field[ ob4[0][0]+1 ][ ob4[0][1]-1 ]!=0) and ob4[0][0]!=(len(field)-1): #if the path down is clear
                ob4[1][0]='U'



def obstcl31(step):
    STEP=step
    if STEP%2==0:

        if ob31[1][0]=='L':
            print(ob31[0][0])
            
            if ob31[0][1]==0:
                ob31[1][0]='R'
                print(ob31[1][0])
                
            if ob31[0][1]>0: #if the "col" location is grather than 0
                
                if field[ ob31[0][0] ][ ob31[0][1]-1 ]==0: #if the path L is clear
                    
                    field[ ob31[0][0]][ ob31[0][1] ]=0
                    field[ ob31[0][0] ][ ob31[0][1]-1 ]=3
                    ob31[0][1]=ob31[0][1]-1 #move left
                    
                if (field[ ob31[0][0] ][ ob31[0][1]-1 ]!=0) and ob31[0][1]!=0: #if the path L is not clear
                    ob31[1][0]='R'
            
        if ob31[1][0]=='R':
            
            if ob31[0][1]==(len(field)-2):
                ob31[1][0]='L'
                print(ob31[1][0])

            if field[ ob31[0][0] ][ ob31[0][1]+1 ]==0: #if the path R is clear
                    
                    field[ ob31[0][0]][ ob31[0][1] ]=0
                    field[ ob31[0][0] ][ ob31[0][1]+1 ]=3
                    ob31[0][1]=ob31[0][1]+1 #move right
                    
            if ob31[0][1]!=(len(field)-1):    
                if (field[ ob31[0][0] ][ ob31[0][1]+1 ]!=0): #if the path L is not clear
                    ob31[1][0]='L'
                    
                    
def obstcl32(step):
    STEP=step
    if STEP%2==0:

        if ob32[1][0]=='L':
            print(ob32[0][0])
            
            if ob32[0][1]==0:
                ob32[1][0]='R'
                print(ob32[1][0])
                
            if ob32[0][1]>0: #if the "col" location is grather than 0
                
                if field[ ob32[0][0] ][ ob32[0][1]-1 ]==0: #if the path L is clear
                    
                    field[ ob32[0][0]][ ob32[0][1] ]=0
                    field[ ob32[0][0] ][ ob32[0][1]-1 ]=3
                    ob32[0][1]=ob32[0][1]-1 #move left
                    
                if (field[ ob32[0][0] ][ ob32[0][1]-1 ]!=0) and ob32[0][1]!=0: #if the path L is not clear
                    ob32[1][0]='R'
            
        if ob32[1][0]=='R':
            
            if ob32[0][1]==(len(field)-2):
                ob32[1][0]='L'
                print(ob32[1][0])

            if field[ ob32[0][0] ][ ob32[0][1]+1 ]==0: #if the path R is clear
                    
                    field[ ob32[0][0]][ ob32[0][1] ]=0
                    field[ ob32[0][0] ][ ob32[0][1]+1 ]=3
                    ob32[0][1]=ob32[0][1]+1 #move right
                    
            if ob32[0][1]!=(len(field)-1):    
                if (field[ ob32[0][0] ][ ob32[0][1]+1 ]!=0): #if the path R is not clear
                    ob32[1][0]='L'

                          
## Ultra-Functions
def UObstcl():
    obstcl32(STEP)
    obstcl4(STEP)
    obstcl31(STEP)

def UScan():
    scan(R1)
    scan(R2)
    scan(R3)
    scan(R4)

def UCheck():
    check(R1)
    check(R2)
    check(R3)
    check(R4)
    
## Problem Definitions
DIM = len(field)

vmap = np.zeros((DIM,DIM))+9
oblist=[2,3,4]

## Class Definitions 
class Robot:

    def __init__(self, pos_x, pos_y, shape, valid_steps):
        self.shape = shape
        self.x = pos_x
        self.y = pos_y
        self.valid_steps = valid_steps

class Obsticle:

    def __init__(self, pos_x, pos_y, shape):

        self.x = pos_x
        self.y = pos_y
        self.shape = shape


## Functions Definitions

def scan(robot): #Scan robot near field for obsticles and other robots
    d =1
    flag = 0
    out = np.zeros((DIM,DIM))+9
##    out[robot.x][robot.y] = 1
    for k in range(len(robot.shape)):
        tempx = robot.shape[k][0]+robot.x
        tempy = robot.shape[k][1]+robot.y
        out[tempx][tempy] = 1
    while flag ==0:
        for i in range(robot.x -d, robot.x+d+1):
            for j in range(robot.y-d, robot.y+d+1):
                if i<0:
                    i=0
                if i>DIM-1:
                    i=DIM-1
                if j<0:
                    j=0
                if j>DIM-1:
                    j=DIM-1
                if field[i][j]==2:
                    flag = 1
                out[i][j] = field[i][j]
                vmap[i][j]=field[i][j]
        d+=1
    d-=1
## 2nd Scan
    x=robot.x
    y=robot.y
    rf = 0
    lf = 0
    tf = 0
    bf = 0
    ## Scan to the RIGHT
    while rf==0:
        for i in range(x-d,x+d+1):
            if i>DIM-1:
                i=DIM-1
            if i<0:
                i=0
            for j in range(y-d,len(field)):
                if j>DIM-1:
                    j=DIM-1
                if j<0:
                    j=0
                if field[i][j]not in oblist:
                    field[i][j]=0
                else: rf=1

    ## Scan to the LEFT
    while lf==0:
        for i in range(x-d,x+d+1):
            if i>DIM-1:
                i=DIM-1
            if i<0:
                i=0
            for j in reversed(range(0,y-d)):
                if j>DIM-1:
                    j=DIM-1
                if j<0:
                    j=0
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: lf=1
        lf=1
        
        ## Scan to the BOTTOM
    while bf==0:
        for i in range(x-d,DIM-1):
            if i>DIM-1:
                i=DIM-1
            if i<0:
                i=0
            for j in range(y-d,y+d+1):
                if j>DIM-1:
                    j=DIM-1
                if j<0:
                    j=0
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: bf=1
        bf=1

        ## Scan to TOP
    while tf==0:
        for i in reversed(range(0,x-d)):
            if i>DIM-1:
                i=DIM-1
            if i<0:
                i=0
            for j in range(y-d+1,y+d-1):
                if j>DIM-1:
                    j=DIM-1
                if j<0:
                    j=0
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: tf=1
        tf=1        


    print('\n scan output:')    
    out[robot.x][robot.y] = 1
    #return out #,x_val,y_val,d, horizontal_scan, vertical_scan
                      
def move(robot, x, y): #Move robot position to x,y
    out = np.zeros((DIM,DIM))
    robot.x = x
    robot.y = y
    for i in range(len(robot.shape)):
        tempx = robot.shape[i][0]+robot.x
        tempy = robot.shape[i][1]+robot.y
        out[tempx][tempy] = 1
    return out

def pos(robot): # Display Self Position of robot
    return move(robot,robot.x,robot.y)

def check(robot): # Check valid steps for robot
    out = [[0,0]] # Initialize list of valid steps
    x = robot.x
    y = robot.y
    for i in range(len(robot.shape)):
        tempx = robot.shape[i][0]+robot.x
        tempy = robot.shape[i][1]+robot.y
        if field[tempx-1][tempy+1]==0 or field[tempx-1][tempy+1]==1:
            out.append([-1,1])
        if field[tempx-1][tempy]==0 or field[tempx-1][tempy]==1:
            out.append([-1,0])
        if field[tempx+1][tempy+1]==0 or field[tempx+1][tempy+1]==1:
            out.append([1,1])

        if field[tempx-1][tempy]==0 or field[tempx-1][tempy]==1:
            out.append([-1,0])
        if field[tempx+1][tempy]==0 or field[tempx+1][tempy]==1:
            out.append([1,0])

        if field[tempx-1][tempy-1]==0 or field[tempx-1][tempy-1]==1:
            out.append([-1,-1])
        if field[tempx+1][tempy]==0 or field[tempx+1][tempy]==1:
            out.append([1,0])
        if field[tempx+1][tempy-1]==0 or field[tempx+1][tempy-1]==1:
            out.append([1,-1])
    sort_out = [[0,0]]
    for i in range(len(out)):
        if out[i] not in sort_out:
            sort_out.append(out[i])
    robot.valid_steps = sort_out
        
def mapstatus():
    section_1_stat = 0 # Top Left Section
    for i in range(0,int(DIM/2)):
        for j in range(0,int(DIM/2)):
            if vmap[i][j]==9:
                section_1_stat+=1
        section_2_stat = 0 # Top Right Section
    for i in range(0,int(DIM/2)):
        for j in range(int(DIM/2),int(DIM)):
            if vmap[i][j]==9:
                section_2_stat+=1
    section_3_stat = 0 # Bottom Left Section
    for i in range(int(DIM/2),int(DIM)):
        for j in range(0,int(DIM/2)):
            if vmap[i][j]==9:
                section_3_stat+=1
    section_4_stat = 0 # Bottom Right Section
    for i in range(int(DIM/2),int(DIM)):
        for j in range(int(DIM/2),int(DIM)):
            if vmap[i][j]==9:
                section_4_stat+=1
    print([section_1_stat,section_2_stat,section_3_stat,section_4_stat])
    return section_1_stat,section_2_stat,section_3_stat,section_4_stat


        
## Other Definitions
all_steps = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[-1,1],[0,-1],[-1,-1]]

## Build Map
        #Robots
R1 = Robot(31,31,[[0,0]],all_steps)
R2 = Robot(14,16,[[0,0],[1,0],[1,1],[0,1]],all_steps)           
R3 = Robot(15,49,[[0,0],[0,1]],all_steps)
R4 = Robot(37,28,[[0,0],[0,1],[1,0]],all_steps)

## ========= MAIN SCRIPT========##

while STEP<100:
    
    print("STEP: ")
    print(STEP)
    print("Map Status: ")
    mapstatus()

    UObstcl() # Update Field
    UScan()     # Robot Scan
    UCheck()    # Robots check for valid coordinates to moove to

###MOVE EACH ROBOT RANDOMLY 
##    move(R1,R1.x+R1.valid_steps[STEP%len(R1.valid_steps)][0],R1.x+R1.valid_steps[STEP%len(R1.valid_steps)][1])
##    move(R2,R2.x+R2.valid_steps[STEP%len(R2.valid_steps)][0],R2.x+R1.valid_steps[STEP%len(R2.valid_steps)][1])
##    move(R3,R3.x+R3.valid_steps[STEP%len(R3.valid_steps)][0],R3.x+R1.valid_steps[STEP%len(R3.valid_steps)][1])
##    move(R4,R4.x+R4.valid_steps[STEP%len(R4.valid_steps)][0],R4.x+R1.valid_steps[STEP%len(R4.valid_steps)][1])

# Move each robot to its 1st valid position:

    move(R1,R1.x + R1.valid_steps[0][0],R1.y + R1.valid_steps[0][1])
    move(R2,R2.x + R2.valid_steps[0][0],R2.y + R2.valid_steps[0][1])
    move(R3,R3.x + R3.valid_steps[0][0],R3.y + R3.valid_steps[0][1])
    move(R4,R4.x + R4.valid_steps[0][0],R4.y + R4.valid_steps[0][1])

    STEP+=1

# ADD HERE EXPORT TO .CSV FILE





























    
