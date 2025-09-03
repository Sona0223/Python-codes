def min_cost(X,Y,Z):  #defining the function
    cost_in= (2*X)+(3*Y)  #taking case 1
    cost_cin=Z+X+(2*Y)    #taking case 2
    cost_com=(2*Z)+Y      #taking case 3
    return min(cost_in,cost_cin,cost_com)  #return the minimum value
X,Y,Z=map(int,input().split()) #taking inputs
print(min_cost(X,Y,Z)) #print the output




X,Y,Z=map(int,input().split())
A=2*Z+Y
B=2*X+3*Y
if(A<B):
    print(A)
else:
    print(B) 

























#The line def minimum_cost(X, Y, Z): is the start of a function definition in Python. Here's a breakdown of its components: 
# "def" keyword is used to define a new function in Python. 
# "min_cost" is the name of the function. You can call this function later in the code by using this name.
# "(X, Y, Z)" are the parameters of the function. Parameters are variables that hold values passed into the function when it is called. In this case, X, Y, and Z will hold the values for the prices of one bucket of popcorn, one drink, and the combo offer, respectively.
# ":"is the colon at the end of this line indicating the start of the function's body, where the actual code for the function is written.