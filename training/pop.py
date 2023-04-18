kangoroo="Pneumonoultramicroscopicsilicovolcanoconiosis"
list_numbers=[]
for i in range(0,len(kangoroo)):
    list_numbers.append(kangoroo[:len(kangoroo)-i])
print(list_numbers)
while len(list_numbers) != 0 :
    element= list_numbers.pop() # print(str(list_numbers) +" we removed   " + element)
    print(list_numbers)