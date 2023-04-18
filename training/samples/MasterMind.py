#shuffle charcater name and calculate the probabily to get the name 
print(" calculate your name shuffability, a very useless measuremet")
from random import randint
from statistics import median
random_str=""
list_prob_space=[]
shuffles=[]
total =0
name=input( "input name :")

for i in range(1,1000):
    proba=0
    random_str=""
    list_prob_space=[]
    while random_str != name:
        random_str=""
        for i in range(0, len(name)):
            list_prob_space.append((name[i]))
        for i in range(1,len(name)+1):
            random_str=random_str+list_prob_space[randint(0,len(name)-1)]
            proba=proba+1#        print(random_str)
    print(" chance to get your name back after a random shuffle is 1/"+str(proba)+ " shuffle")
    shuffles.append(proba)
for i in range(0,len(shuffles)):
    total=total+shuffles[i]
moy=total/len(shuffles)
print(" **********************statistics*********************")
print("     average chance to get your name back after a random shuffle is 1/"+str(int(moy))+ " shuffle")
print("     median chance to get your name back after a random shuffle is 1/"+str(median(shuffles))+ " shuffle")