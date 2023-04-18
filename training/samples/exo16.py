voyelles =["a","e","i","o","u","y"]
count_voyelle = 0
word=input(" enter a  word :")
for char in word :
    if char in voyelles: 
        count_voyelle= count_voyelle+1
print(f"{count_voyelle}")

## Unit test 
list_words_test = ["tomate", "citron", "voiture","e","h", " hftg"]
list_voyelles_test = [3, 2, 4,1,0,0]

for word in list_words_test :
    count_voyelle =0
    # code to test 
    for char in word :
        if char in voyelles: 
            count_voyelle= count_voyelle+1
    index = list_words_test.index(word)
    #################################################
    if count_voyelle != list_voyelles_test[index]:
        print(f" Test NOK {word} found  {count_voyelle} expected {list_voyelles_test[index]}")
    else:
        print (f" Test OK {word} found  {count_voyelle} expected {list_voyelles_test[index]}")