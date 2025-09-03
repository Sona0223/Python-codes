# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return (n*fact(n-1))
# n=int(input("enter:"))
# result=fact(n)
# print(result)



a=input("Enter a string: ")
str= a.replace(" ", "").lower()
if (str == str[::-1]):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")