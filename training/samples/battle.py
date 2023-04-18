from random import randint
ennemy_position = randint(1,10)
ennemy_area= "    ennemy is some where between 1-10"
found = False
print("                ******YOUR ENNEMY IS BETWEEN 1-10 COORDINATES TRY TO HIT HIM **********")
print("                             1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10")
while found == False :
    for i in range (0,3):
        try:
            nbr =input(ennemy_area+" ( "+str(3-i)+ " tries left ) : ")
            int_nbr=int(nbr) 
            if int_nbr == ennemy_position :
                print("\n        Mission complete :) !!, ennemy neutralized at coordinate ! "+ str(int_nbr))
                found = True
                break
            elif int_nbr < ennemy_position :
                ennemy_area="    "  + nbr +" >>> ennemy  is  that direction"
            else :
                ennemy_area ="    " + "ennemy is that direction  <<< " + nbr 
        except  ValueError:
            print("Sorry,"+nbr+ " is not a valid coordinate  ")
    else: 
            print("Sorry, no more tries , ennemy escaped he was in  :" + str(ennemy_position) )
            break
    
    
    