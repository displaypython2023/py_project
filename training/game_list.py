grid = [
    ["a","x","y"],
    ["w","v","u"],
    ["t","s","r"],
    ]
grid =[[1, 2, 3, 4], 
       [5, 6, 7, 8], 
       [9, 10, 11, 12]]

#for line in range (3):
#    txt =""
#    for column in range(4):
#        txt=txt + str(int(grid[line][column]/2)) + " " 
#    print(txt)

for line in grid:
    txt =""
    for value in line:
        txt=txt + str(value/2) + " " 
    print(txt)
i=0
