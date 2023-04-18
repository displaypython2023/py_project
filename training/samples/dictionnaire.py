def enter_number(text):
    while True:
        try:
            return int(input(text))
        except:
            print (" you need to enter a number")
    
    
    

scores={"MokoSempai":16,"Grungi":30, "ELocin":56}
#player=input ("enter the name of the player :")
#score=enter_number("enter the score :")
#scores[player]=score
#print (scores)
#print ("Nom: ELocin \n score :" + str(scores["ELocin"]))
print ("######## Print with the key #############")
for player  in scores:
    print ("Nom:" + player +"- score :" + str(scores[player]))

print ("######## Print with the val #############")
for score  in scores.values():
    print ("score :" + str(scores[player]))

print ("######## Print with the item #############")
for player,score  in scores.items():
    print ("Nom:" + player +"- score :"+ str (score))

try:
    item = scores.pop("smail")
    print(item)
    print(scores)
except:
    print("doesn't exist")

for i in range(0,100):
    scores["player_"+str(i)]=i
for player,score  in scores.items():
    print ("Nom:" + player +"- score :"+ str (score))
#dynamic list
produit= [x *3 for x in range(1,11)]
print (produit)

scores_moy=[name  for name, score in scores.items() if score >=90]
print (scores_moy)

#dictionnaire dynamic
scores_moy={name:score  for name, score in scores.items() if score >=97}
print (scores_moy)

#complex dictionaries
scores ={
        "pierre" : {
                "math" : 5,
                "langue" : 10
                },
        "Aline" : {
                "math" : 10,
                "langue" : 15
                }
         }

print (scores["pierre"]["math"])

squares =[]
for x in range(10):
    if x % 2 == 0:
        squares.append(x*x)
print (squares)

squares = [x*x for x in range(10) if x % 2 ==0 ]
print (squares)

if squares == squares :
    print (" they are the same")
    print (squares)