## Python Initialization:
import numpy as np
#import pandas
import matplotlib

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
    d =1 #Scan area diameter
    for i in range(robot.x -d, robot.x+d):
        for j in range(robot.y-d, robot.y+d):
            out = np.zeros((robot.x+2*d, robot.y+2*d))
            if i<0:
                i=0
            if i>52:
                i=52
            if j<0:
                j=0
            if j>52:
                j=52
            out[i][j] = i+j
    return out
            
        




## Other Definitions
all_steps = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[-1,1],[0,-1],[-1,-1]]

## Build Map
        #Robots
R1 = Robot(31,31,[0,0],all_steps)
R2 = Robot(14,16,[[0,0],[1,0],[1,1],[0,1]],all_steps)           
R3 = Robot(15,49,[[0,0],[1,0]],all_steps)
R4 = Robot(37,28,[[0,0],[0,1],[1,0]],all_steps)



r1_shape = [[0,0],[0,0],[0,0],[0,0]]
r2_shape = [[0,0],[1,0],[1,1],[1,1]]
r3_shape = [[0,0],[1,0],[1,1],[0,1]]
r4_shape = [[0,0],[1,0],[1,0],[0,0]]

