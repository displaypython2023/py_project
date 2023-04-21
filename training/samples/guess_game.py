from random import randint
right_answer = randint(1,10)

guess = int( input("Guess  the magic number between 1 an 10  :"))
for i in range (2,4):
    if guess == right_answer :
        print("Eureka, it is indeed :"+str(right_answer))
        break;
    elif guess > right_answer :
        result=" bigger"
    else :
        result =" smaller"
    guess = int( input(str(guess) + " is "+result+" than  the magic number ( "+str(i)+ " try ) :"))
else: 
    print("Sorry, no more tries it was :" + str(right_answer) )