import numpy as np
dim = 15
field = np.zeros((dim,dim))+9
x = 1
y = 0
oblist = [2,3,4]
field[x][y] = 1
field [6][3] = 2
field [7][3] = 2
field [6][4] = 2
d =3

print('\n')
print('Raw Data')
field[x][y]=1
print(field)

for i in range(x-d,x+d+1):
    for j in range(y-d,y+d+1):
        if field[i][j] ==9:
            field[i][j]=0
print('\n')
print('first scan')
field[x][y]=1
print(field)


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
print('\n')
print('right scan')
field[x][y]=1
print(field)

## Scan to the LEFT
while lf==0:
    for i in range(x-d,x+d+1):
        for j in reversed(range(0,y-d)):
            if field[i][j]not in oblist:
                field[i][j]=0
            else: lf=1
    lf=1
    
print('\n')
print('left scan')
field[x][y]=1
print(field)

    ## Scan to the BOTTOM
while bf==0:
    for i in range(x-d,dim):
        for j in range(y-d,y+d+1):
            if field[i][j]not in oblist:
                field[i][j]=0
            else: bf=1
    bf=1
print('\n')
print('bottom scan')
field[x][y]=1
print(field)

    ## Scan to TOP
while tf==0:
    for i in reversed(range(0,x-d)):
        for j in range(y-d,y+d+1):
            if field[i][j]not in oblist:
                field[i][j]=0
            else: tf=1
    tf=1        
print('\n')
print('top scan')
field[x][y]=1
print(field)
