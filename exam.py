#LECTURE 11 NOV
st='I Like Python'
print(st[2]) #printing using +ve index
print(st[-10]) #printing using -ve index
print(st[4])
print(st[-8]) 
print(st[7:13:1]) #1 means leaving no index
print(st[2:6]) #default is one
print(st[0:6:2]) #2 means leaving 1 index
print(st[12:6:-1]) #-1 will be printing reverse
print(st[-11:-7]) #negative index printing
print(st[:]) #printing all
print(st[:6]) #0 is default starting index
print(st[7:]) #end index is default
print(st[::-1]) #print all in reverse
print(st[2:6:-1]) #it should be +1 for printing  its in increasing order 
stnew=st.capitalize() #capitalize first letter
print(stnew)
stnew2=st.casefold() #lowercase
print(stnew2)
n=st.count('e') #count an alphabet or word occuring
print(n)
print('-'.join(st))

#LECTURE 12TH NOV
st='python'
st1='ja'
st2='va'
print(st1+st2) #concatenation
print(st*3) #replication
print('python' in st) #membership
print('java' not in st) #reverse of membership
a='hello how are you.\
    I am fine' #ignores new line
print(a)
b='https:\\\\abes.ac.in' #backslash
print(b)
c='Good morning Mr, \'BOB\'' #need single quotes in the string
print(c)
print("Good {}! Mr,{}".format('Morning', 'BOB')) #formatting
print("{1} and {0} play football".format('Bob','Ram')) #index formatting
val=10
print("to binary {0:b}".format(val)) #use for binary
val1=10.8914
print("in float {0:f}".format(val1)) #decimal value
print("in float {0:.2f}".format(val1)) #two numbers after decimal
x=10
y=20
z=x+y
print(f"sum of {x} and {y} = {z}")
line="Hello how are you"
L=line.split('a')
for i in L:
    print(i, end='')  #a is not printed 

example="ABES Engineering College"
print(example[::-1].startswith("A")) #false

v="MANGO"
for i in range(len(v)):
    print(v[i]) 







#LECTURE 19TH NOV
