#remove from llist the randomly generated list of strings 
from random import randint
kangoroo="encourage"
list_numbers=[]
for i in range(0,10):
    list_numbers.append(kangoroo[:randint(1,len(kangoroo))])
print(list_numbers)
while len(list_numbers) != 0 :
    number=input( "chosse one element to eleminate :")
    try :
        list_numbers.remove(number)
        print(list_numbers)
    except ValueError:
        print(" error not in the list try again")
    