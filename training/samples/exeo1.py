while 1 == 1 :
    nbr=input("type a number :")
    try:
        int_nbr=int(nbr) 
        print("Good !! you have typed  "+nbr)
        if int_nbr < 10 :
            print("the number is smaller than 10")
        break
    except  ValueError:
        print("you should type a number  error ")
    
    