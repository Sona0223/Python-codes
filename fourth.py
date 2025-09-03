f=open("practice.txt","r")
data= f.read()
if(data.find("learning")!=-1):
    print("found")
else:
    print("not found") 
f.close() 