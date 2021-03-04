## Python Initialization:
import numpy as np
#import pandas
import matplotlib

field = np.zeros((10,10))

field[4][4] = 2
field[3][4] = 2
field[2][4] = 2
field[1][4] = 2
field[4][5] = 2
field[3][5] = 2
field[2][5] = 2
field[1][5] = 2
field[4][6] = 2
field[3][6] = 2
field[2][6] = 2
field[1][6] = 2
## Problem Definitions
DIM = 10


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

def scan(robot):
    d =1
    flag = 0
    out = np.zeros((DIM,DIM))+9
    out[robot.x][robot.y] = 1
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
                    j=DIM
                if field[i][j]==2:
                    flag = 1
                out[i][j] = field[i][j]
        d+=1
    return out
            
        
def move(robot, x, y):
    out = np.zeros((DIM,DIM))
    robot.x = x
    robot.y = y
    for i in range(len(robot.shape)):
        tempx = robot.shape[i][0]+robot.x
        tempy = robot.shape[i][1]+robot.y
        out[tempx][tempy] = 1
    return out
    

def check(robot):
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
        
            


        
## Other Definitions
all_steps = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[-1,1],[0,-1],[-1,-1]]

## Build Map
        #Robots
R1 = Robot(31,31,[0,0],all_steps)
R2 = Robot(14,16,[[0,0],[1,0],[1,1],[0,1]],all_steps)           
R3 = Robot(15,49,[[0,0],[0,1]],all_steps)
R4 = Robot(37,28,[[0,0],[0,1],[1,0]],all_steps)

tr = Robot(2,4,[[0,0],[0,1],[1,1]],all_steps) #Test Robot



r1_shape = [[0,0],[0,0],[0,0],[0,0]]
r2_shape = [[0,0],[1,0],[1,1],[1,1]]
r3_shape = [[0,0],[1,0],[1,1],[0,1]]
r4_shape = [[0,0],[1,0],[1,0],[0,0]]

scan(tr)
