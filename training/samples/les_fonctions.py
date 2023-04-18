from random import randint
def say_hello():
    say_hello=["Bjr","Hello","Ola"]
    for i in range(100):
        if (i % randint(1,10) == 0):
            end_char="\n"
        print(f"{say_hello[randint(0,2)]} ",end=end_char)
        end_char=""
        return  "******end****"

def say_something():
    say_something="saigkjfdqdskfkqjdGFKJQLD<HGFKJHDQGBFKHBGFHDGQFHQGKHDQGFKDGQKFDSQGKFJGDSQKJFGDQSKG?NKhfihgzi"
    return  say_something[randint(0,len(say_something)-1)]


def random_range(range_val,length):
    txt=""
    for _ in range(0,length):
        txt= txt+range_val[randint(0,len(range_val)-1)]
    return txt
        
#for k in range(20):
#    print ("\n what are you sayi"+"i"*k+"ng !!!")
#    print ("I said :",end="")
#    for i in range(7):
#        print (f"{say_something()}",end="")
range_val="test"
while len(range_val)!=0:
    range_val=input("give a set of characters to randomize :")
    try:
        length=int(input("how many charcter you would like to get:"))
        print (random_range(range_val, length))
    except:
        print("bye!!!")
        break