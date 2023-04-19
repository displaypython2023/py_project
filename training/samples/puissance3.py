#display(grid)
#display2(grid)

#global
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
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
    global winner
    global token
    for element in grid:
        grid2.append(element)
    grid2.append([i for i in range(0,len(grid2[0]))])
    for line in range(0,len(grid2)):
        if line!=len(grid2)-1:
            txt = str(line)+" "
        else: 
            txt ="  "
        for column in grid2[line]:
            if(str(column) in ["/","\\","-","|","/"]):
                
                txt=txt + f"{OKBLUE}{str(token[winner])}{ENDC}" + " " 
            else:
                txt=txt + str(column) + " " 
        print(txt)
    grid2.clear()
def color(line, column, direction):
    if(direction =="hr"):
        grid[line][column]="-"
        grid[line][column+1]="-"
        grid[line][column+2]="-"
    if(direction =="hc"):
        grid[line][column]="-"
        grid[line][column-1]="-"
        grid[line][column+1]="-"
    if(direction =="hl"):
        grid[line][column]="-"
        grid[line][column-1]="-"
        grid[line][column-2]="-"
    if(direction =="v"):
        grid[line][column]="|"
        grid[line+1][column]="|"
        grid[line+2][column]="|"
    if(direction =="dr"):
        grid[line][column]="\\"
        grid[line+1][column+1]="\\"
        grid[line+2][column+2]="\\"
    if(direction =="dl"):
        grid[line][column]="\\"
        grid[line-1][column-1]="\\"
        grid[line-2][column-2]="\\"
    if(direction =="dr2"):
        grid[line][column]="/"
        grid[line-1][column+1]="/"
        grid[line-2][column+2]="/"
    if(direction =="dl2"):
        grid[line][column]="/"
        grid[line+1][column-1]="/"
        grid[line+2][column-2]="/"
    if(direction =="cl"):
        grid[line][column]="/"
        grid[line+1][column-1]="/"
        grid[line-1][column+1]="/"
    if(direction =="cr"):
        grid[line][column]="\\"
        grid[line+1][column+1]="\\"
        grid[line-1][column-1]="\\"
   
def check_horizontal(grid,line,column):
#check horizontal
    if(len(grid[line])-column >= 3  ):
        if(grid[line][column]==grid[line][column+1]==grid[line][column+2]):
            color(line,column,"hr")
            return True
    if(column >= 2  ):
        if( grid[line][column]==grid[line][column-1]==grid[line][column-2] ):
                color(line,column,"hl")
                return True
    if(len(grid[line])-column > 1 and  column-1 >=0 ):
        if(grid[line][column]==grid[line][column+1]==grid[line][column-1]):
            color(line,column,"hc")
            return True
    return False
def check_vertical(grid,line,column):
#check vertical
    if(len(grid)-line < 3):
        return False
    if(grid[line][column]==grid[line+1][column]==grid[line+2][column]):
        color(line,column,"v")
        return True
    return False
def check_axes(grid,line,column):
#check axes
    if(line+2 < len(grid) and column +2 < len(grid[line])):
        if(grid[line][column]==grid[line+1][column+1]==grid[line+2][column+2]):
            color(line,column,"dr")
            return True
    if(line-2 >= 0 and column -2 >= 0):
        if(grid[line][column]==grid[line-1][column-1]==grid[line-2][column-2]):
            color(line,column,"dl")
            return True
    if(line-2 >=0 and column +2 < len(grid[line])):
        if(grid[line][column]==grid[line-1][column+1]==grid[line-2][column+2]):
            color(line,column,"dr2")
            return True
    if(line+2 < len(grid) and column -2 <= 0):
        if(grid[line][column]==grid[line+1][column-1]==grid[line+2][column-2]):
            color(line,column,"dl2")
            return True
    
    if(line+1 < len(grid) and line -1 >= 0 and column -1 >= 0 and column +1 < len(grid[line])):
        if(grid[line-1][column-1]==grid[line][column]==grid[line+1][column+1]):
            color(line,column,"cr")
            return True
        
    if(line-1 >=0 and column +1 < len(grid[line]) and line+1 < len(grid) and column +1 < len(grid[line]) ):
        if(grid[line][column]==grid[line+1][column-1]==grid[line-1][column+1]):
            color(line,column,"cl")
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
    if player == 2:
        token="O"
    line =0
    prev_line =0
    placed=False
    while line < len(grid) and grid[line][column] == "."  :
        prev_line=line
        line= line + 1
    if  prev_line >=0 and prev_line < len(grid) and grid[prev_line][column]== "." :
        placed= True
        grid[prev_line][column]=token
    
    display3(grid)
    return prev_line , placed
def check_game_over(grid):   
    for line in grid:
        for column in line:
            if column==".":
                return False
    return True        
print("")
winner = None
display3(grid)
current_player =1
token=[".","X","O"]
while winner == None:
    if check_game_over(grid)==True:
        print(" GAME OVER NO WINNER")
        break
    try:
        column=int(input (f"player {token[current_player]} play please:"))
        if(column >= len(grid[0]) or column < 0):
            print (f"(out of range) ",end="")
            continue 
    except :
        print (f"(wrong input ) ",end="")
        continue
    line_pos, placed=add_token(grid,current_player,column)
    if placed == False:
        print (f"(full try another column) ",end="")
        continue 
    if check_winner(grid,line_pos,column):
        winner=current_player
    elif current_player== 1:
        current_player=2
    else:
        current_player=1
display3(grid)
print ("        Congratulation player "+ str(winner) + " played as "+ token[winner])
        
            
    
    
    





 


