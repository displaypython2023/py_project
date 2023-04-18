while 1 == 1 :
    nbr=input("ennemy is between 1 and 10 coordinates try to hit him:")
    try:
        int_nbr=int(nbr) 
        if int_nbr >= 1 and int_nbr <= 10:
            print("Mission complete :) !!, ennemy nutralized at coordinate !"+ nbr)
            break
        else :
            print( " Missed  :( !! the ennemy is not in "+nbr)
    except  ValueError:
        print("Sorry,"+nbr+ " is not a valid coordinate  ")
    
    