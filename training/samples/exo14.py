input_command = ""
while input_command != "end" :
    input_command=input ("type a word please:")
    input_command=input_command.rstrip()
    if input_command !="" :
        if input_command[0] == "t" :
            print (f"{input_command}!!!")