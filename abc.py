message="welcome to Mysore"
word=message[-7:] #include gap also
if(word=="mysore"): 
    print("got it")
else:
    message=message[3:14]
    print(message) 

example="ABES engineering college" 
print("%s" %example[2:7]) #ES en 