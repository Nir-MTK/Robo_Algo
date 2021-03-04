## Python Initialization:
import numpy as np
#import pandas
import matplotlib

field = np.zeros((10,10))
field[2][8] = 1
field[4][4] = 2
field[3][4] = 2


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
    out = np.zeros((10,10))+9
    out[robot.x][robot.y] = 1
    out[robot.x][robot.y] = 0
    
    while flag ==0:
        for i in range(robot.x -d, robot.x+d+1):
            for j in range(robot.y-d, robot.y+d+1):

                if i<0:
                    i=0
                if i>9:
                    i=9
                if j<0:
                    j=0
                if j>9:
                    j=9
                if field[i][j]==2:
                    flag = 1
                out[i][j] = field[i][j]
        d+=1
    return out
            
        




## Other Definitions
all_steps = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[-1,1],[0,-1],[-1,-1]]

## Build Map
        #Robots
R1 = Robot(31,31,[0,0],all_steps)
R2 = Robot(14,16,[[0,0],[1,0],[1,1],[0,1]],all_steps)           
R3 = Robot(15,49,[[0,0],[1,0]],all_steps)
R4 = Robot(37,28,[[0,0],[0,1],[1,0]],all_steps)

tr = Robot(2,8,[0,0],all_steps) #Test Robot

r1_shape = [[0,0],[0,0],[0,0],[0,0]]
r2_shape = [[0,0],[1,0],[1,1],[1,1]]
r3_shape = [[0,0],[1,0],[1,1],[0,1]]
r4_shape = [[0,0],[1,0],[1,0],[0,0]]

scan(tr)
