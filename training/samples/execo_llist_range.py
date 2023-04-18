from random import randint
list_words=["I", "really","love","Python"]
iterator = range(len(list_words))
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
# we use underscore as a coding convention to indicate that this variable is not used in the loop
for _ in range(8):
	print("\n")
	for i in iterator:
		icolor = randint(0,len(list_colors)-1)
		print(f"{list_colors[icolor]}{list_words[i]} {ENDC}", end='')