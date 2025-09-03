str='google.com'
fre={}
for i in str:
    if i in fre:
        fre[i] +=1
    else:
        fre[i]=1
for i,char in fre.items():
    print(f"{i}:{char}")