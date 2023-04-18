#display(grid)
#display2(grid)

#global
grid =[
       [".",".",".",".",".",]
     , [".",".",".",".",".",]
     , [".",".",".",".",".",]
     , [".",".",".",".",".",]
     , [".",".",".",".",".",]
     ]
#functions
def display(grid):
    
    i=-1
    for line in grid:
        i= i+1
        print(f"{i} ",end="")
        for column in line:
            print  (f"{column} ",end="")
        print ("")
    print(f"  ",end="")
    for i in range(0,len(line)):
        print(f"{i} ",end="") 
def display2(grid):
    lines=[i for i in range(0,len(grid[0]))]
    grid.append(lines)
    i=-1
    for line in grid:
        i= i+1
        print(f"{i} ",end="")
        for column in line:
            print  (f"{column} ",end="")
        print ("")
def display3(grid):
    grid.append([i for i in range(0,len(grid[0]))])
    for line in range(0,len(grid)):
        if line!=len(grid)-1:
            txt = str(line)+" "
        else: 
            txt ="  "
        for column in grid[line]:
            txt=txt + str(column) + " " 
        print(txt)
def check_winner(grid, player):
    if player == 2 :
        return True
    return False
def add_token(grid,player,column):
    token="X"
    if player == 1:
        token="O"
    line =0
    while grid[line][column] == "." and line < len(grid):
        line= line + 1
    if line < len(grid) and line-1 >0:
        grid[line-1][column]=token
    display3(grid)
    return grid
    
print("")
display3(grid)
winner = None
current_player =1
while winner == None:
    grid=add_token(grid,1,1)
    if check_winner(grid,current_player):
        winner=current_player
    elif current_player== 1:
        current_player=2
    else:
        current_player=1
print ("Congratulation player"+ str(winner))
        
            
    
    
    





 


