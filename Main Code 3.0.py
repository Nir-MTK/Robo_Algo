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










## Problem Definitions
DIM = len(field)
#field = np.zeros((DIM,DIM))
vmap = np.zeros((DIM,DIM))+9
oblist=[2,3,4]

##field[4][4] = 2
##field[3][4] = 2
##field[2][4] = 2
##field[1][4] = 2
##field[4][5] = 2
##field[3][5] = 2
##field[2][5] = 2
##field[1][5] = 2
##field[4][6] = 2
##field[3][6] = 2
##field[2][6] = 2
##field[1][6] = 2
##
##field[4][4] = 2
##field[3][4] = 2
##field[2][4] = 2
##field[1][4] = 2
##field[4][5] = 2
##field[3][5] = 2
##field[2][5] = 2
##field[1][5] = 2
##field[4][6] = 2
##field[3][6] = 2
##field[2][6] = 2
##field[1][6] = 2
##
##
##field[12][12] = 2
##field[13][13] = 2
##field[12][13] = 2
##field[13][12] = 2



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
            for j in range(y-d,len(field)):
                if field[i][j]not in oblist:
                    field[i][j]=0
                else: rf=1

    ## Scan to the LEFT
    while lf==0:
        for i in range(x-d,x+d+1):
            for j in reversed(range(0,y-d)):
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: lf=1
        lf=1
        
        ## Scan to the BOTTOM
    while bf==0:
        for i in range(x-d,DIM-1):
            for j in range(y-d,y+d+1):
                if j>DIM-1:
                    j=DIM-1
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: bf=1
        bf=1

        ## Scan to TOP
    while tf==0:
        for i in reversed(range(0,x-d)):
            for j in range(y-d+1,y+d-1):
                if j>DIM-1:
                    j=DIM-1
                if field[i][j]not in oblist:
                    out[i][j]=0
                    vmap[i][j]=field[i][j]
                else: tf=1
        tf=1        


    print('\n scan output:')    
    out[robot.x][robot.y] = 1
    return out #,x_val,y_val,d, horizontal_scan, vertical_scan
                      
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
    return section_1_stat,section_2_stat,section_3_stat,section_4_stat


        
## Other Definitions
all_steps = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[-1,1],[0,-1],[-1,-1]]

## Build Map
        #Robots
R1 = Robot(31,31,[0,0],all_steps)
R2 = Robot(14,16,[[0,0],[1,0],[1,1],[0,1]],all_steps)           
R3 = Robot(15,49,[[0,0],[0,1]],all_steps)
R4 = Robot(37,28,[[0,0],[0,1],[1,0]],all_steps)

tr = Robot(7,8,[[0,0],[0,1],[1,1]],all_steps) #Test Robot


## ========= MAIN SCRIPT========##

##Update Field: ## TBD ##

#### Update Virtual Map
##scan(R1)
##scan(R2)
##scan(R3)
##scan(R4)
##
#### Update Valid Steps foe each robot
##check(R1)
##check(R2)
##check(R3)
##check(R4)
##
#### 

