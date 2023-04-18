from random import randint
import time
code=[]
letters_list=[]
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
list_colors =[HEADER,OKBLUE , OKCYAN, OKGREEN , WARNING, FAIL ,BOLD, UNDERLINE]
pool_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code_length =0
letters_length =0
while code_length >6 or code_length < 1:
    try:
        code_length=int(input("choose complexity from 1-6 :"))
    except ValueError:
        print("enter a number please)")
while letters_length >28 or letters_length < 6:
    try:
        letters_length=int(input("choose complexity from 6-28 :"))
    except ValueError:
        print("enter a number please)")

for i in range(0,letters_length-1):
    letters_list.append(pool_list[randint(0,len(pool_list)-1)])
print(letters_list)
while len(code) != code_length :
    code.append(letters_list[randint(0,len(letters_list)-1)])
print(code)
found= False
# ùain loop
# printing the start time
#print("The time of code execution begin is : ", time.ctime())
while found != True :
    # user proposal
    guess=[]
    guess=list(input(f"{OKBLUE}guess the code :{ENDC}"))
    while len(guess) != code_length :
            len_guess= len(guess)
            print(f"{OKBLUE}code lenght not correct you typed {len_guess}  you must have {code_length} characters please ! {ENDC}",end='')
            guess=list(input(":"))
    # calculate good placed
    good_placed=[]
    for i in range(0,code_length):
        if guess[i]==code[i]:
            good_placed.append(i)
    print("good_place", str(len(good_placed)))
    
    # calculate  correctly guessed but not in the good place
    existing=[]
    for i in range(0,code_length):
        if guess[i] in code and i not in good_placed :
                existing.append(i)
                
    print("found and wrong placed", str(len(existing)))
    
    #  guess is OK, you deserve a celebration  before  stop game 
    str_string=''
    play =0
    if(len(good_placed) == code_length):
        while play < 3:
            print("\n"*43)
            for i in range(0,120,2):
                print("\n"*43)
                time.sleep(0.01)
                target =40-i
                print (" "*i+"YOU WIN!!!!!!! ")
                print ( " "*i+"  .--.   ")                      
                print ( " "*i+" / _.-'  ")
                print ( " "*i+" \  '-."+" "*target+ str_string.join(code))
                print ( " "*i+"  '--'   ") 
                time.sleep(0.3)
                if target <=0 :   
                    for k in range(1,20):
                        print("\n"*43)
                        time.sleep(0.1)
                        print (" "*i+"YOU WIN!!!!!!! ")
                        print ( " "*i+"  .--.   ")                      
                        print ( " "*i+" / __'_'.  ")
                        print ( " "*i+" \    .'  ")
                        print ( " "*i+"  '--'   ") 
                        time.sleep(0.3)
                    play = play +1
                    time.sleep(3)
                    found = True
                    break