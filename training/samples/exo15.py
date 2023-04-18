input_ok = False
number_limit = 0
while input_ok == False :
    try :
        number_limit=int(input("enter a number form 1 to 100 :"))
    except: 
        input_ok = False 
        print ("you must enter an integer  number please")
    if number_limit > 100 or  number_limit < 1 :
        print ("you must enter an integer number between 10 and 100")
    else:
        input_ok= True
        
total = int((1 + number_limit)* number_limit/2)
print (f"{total}")

total_verif = 0
for i in range (0,number_limit):
    total_verif = total_verif + (i+1)

if total_verif == total :
    print (" Test is OK")
else:
    print(f"something is wrong {total_verif}")