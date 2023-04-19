#display(grid)
#display2(grid)

#global
grid =[
       [".",".",".",".",".","."]
     , [".",".",".",".",".","."]
     , [".",".",".",".",".","."]
     , [".",".",".",".",".","."]
     , [".",".",".",".",".","."]
     , [".",".",".",".",".","."]
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
    grid2=[]
    for element in grid:
        grid2.append(element)
    grid2.append([i for i in range(0,len(grid2[0]))])
    for line in range(0,len(grid2)):
        if line!=len(grid2)-1:
            txt = str(line)+" "
        else: 
            txt ="  "
        for column in grid2[line]:
            txt=txt + str(column) + " " 
        print(txt)
    grid2.clear()

def check_horizontal(grid,line,column):
#check horizontal
    if(len(grid[line])-column >= 3  ):
        if(grid[line][column]==grid[line][column+1]==grid[line][column+2]):
            return True
    if(column >= 2  ):
        if( grid[line][column]==grid[line][column-1]==grid[line][column-2] ):
                return True
    return False
def check_vertical(grid,line,column):
#check vertical
    if(len(grid)-line < 3):
        return False
    if(grid[line][column]==grid[line+1][column]==grid[line+2][column]):
        return True
    return False
def check_axes(grid,line,column):
#check axes
    if(line+2 < len(grid) and column +2 < len(grid[line])):
        if(grid[line][column]==grid[line+1][column+1]==grid[line+2][column+2]):
            return True
    if(line-2 >= 0 and column -2 >= 0):
        if(grid[line][column]==grid[line-1][column-1]==grid[line-2][column-2]):
            return True
    if(line-2 >=0 and column +2 < len(grid[line])):
        if(grid[line][column]==grid[line-1][column+1]==grid[line-2][column+2]):
            return True
    if(line+2 < len(grid) and column -2 <= 0):
        if(grid[line][column]==grid[line+1][column-1]==grid[line+2][column-2]):
            return True
    return False
def check_winner(grid, line,column):
    if check_horizontal(grid,line,column)== True:
        return True
    if check_vertical(grid,line,column)== True:
        return True
    if check_axes(grid,line,column)== True:
        return True
    return False
def add_token(grid,player,column):
    token="X"
    if player == 1:
        token="O"
    line =0
    prev_line =0
    while line < len(grid) and grid[line][column] == "."  :
        prev_line=line
        line= line + 1
    if  prev_line >=0 and prev_line < len(grid):
        grid[prev_line][column]=token
    display3(grid)
    return prev_line
    
print("")
display3(grid)
winner = None
current_player =1
token=[".","X","O"]
while winner == None:
    column=int(input (f"player {token[current_player%2+1]} play please:"))
    line_pos=add_token(grid,current_player,column)
    if check_winner(grid,line_pos,column):
        winner=current_player
    elif current_player== 1:
        current_player=2
    else:
        current_player=1
print ("Congratulation player"+ str(winner))
        
            
    
    
    





 


