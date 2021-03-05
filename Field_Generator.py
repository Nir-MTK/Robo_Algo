import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt


np.set_printoptions(threshold=np.inf)

STEP = 8
ob4 = [[37,30],['U']] #coordinated of the center cell & mooving direction U/D
ob31 = [[41,32],['R']] #coordinated of the center cell & mooving direction R/L
ob32 = [[52,40],['R']] #coordinated of the center cell & mooving direction R/L


field = genfromtxt('finalProjectMap.csv', delimiter=',')

def obstcl4():
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



def obstcl31():
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
                    
                    
def obstcl32():
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

                          
##### saving array to csv: ###############
#save the array to a csv

import pandas as pd

df = pd.DataFrame(field)
df.to_csv('file.csv',index=False, header=False)
