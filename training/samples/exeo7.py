while 1 == 1 :
    nbr=input("type a number :")
    try:
        int_nbr=int(nbr) 
        print("Good !! you have typed  "+nbr)
        if int_nbr > 10 :
            print("bravo !")
        elif int_nbr > 8 :
            print("PAs mal !")
        elif int_nbr > 5 :
            print("Mouais, bof!")
        else :
            print("Pas terrible !")
        break
    except  ValueError:
        print("you should type a number  error ")
    
    