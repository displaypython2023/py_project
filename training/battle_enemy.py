from random import randint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    max_chance=int(input("how many bullets you have  :"))
    battle_field_size=int(input("enter battle field size "))
except  ValueError:
        print("Sorry, type a valid number  ")
        exit(-1)
ennemy_position = randint(1,battle_field_size)
ennemy_area= "    ennemy is some where between 1-"+str(battle_field_size)
found = False
print("                ******YOUR ENNEMY IS BETWEEN 1-10 COORDINATES TRY TO HIT HIM **********")

battle_field="                             "
for f in range(1,battle_field_size+1):
    battle_field=battle_field+str(f)+" | "
print(battle_field)

while found == False :
    for i in range (0,max_chance):
        try:
            nbr =input(ennemy_area+" ( "+str(max_chance-i)+ " tries left ) : ")
            int_nbr=int(nbr) 
            if(int_nbr > battle_field_size or int_nbr < 1):
                print("Come on !!!!   between 1 and "+str(battle_field_size))
                break
            if int_nbr == ennemy_position :
                print(f"{bcolors.HEADER}\n        Mission completed :) !!, ennemy neutralized at coordinate ! {bcolors.ENDC}"+ str(int_nbr))   
                found = True
                break
            elif int_nbr < ennemy_position :
                print(battle_field)
                ennemy_area="                             "
                for j in range(1,int_nbr):
                    ennemy_area=ennemy_area+"    "
                    if j >= 10:
                        ennemy_area=ennemy_area+" "
                ennemy_area=ennemy_area+"X >>> enmy "
            else :
                print(battle_field)
                ennemy_area="                   "
                for j in range(1,int_nbr):
                    ennemy_area=ennemy_area+"    "
                    if j >= 10:
                        ennemy_area=ennemy_area+" "
                ennemy_area=ennemy_area+"enemy <<< X " 
        except  ValueError:
            print("Sorry,"+nbr+ " is not a valid coordinate  ")
    else: 
            print("Sorry, no more tries , ennemy escaped he was in  :" + str(ennemy_position) )
            break
    
    
    