T=int(input())  #T is the number of test cases. Each test case represents a scenario where we need to check if Chef could have eaten exactly K slices using N oranges.
res=[]  #This list will store the output ("YES" or "NO") for each test case 
for _ in range(T): #We use a loop to handle each test case one by one
    N,K=map(int,input().split()) #reads two integers separated by space and assigns them to N and K.
    #Since each orange has between 10 and 12 slices, the minimum possible slices for N oranges would be 10×N and the maximum possible slices would be 12×N
    min_slices=10*N 
    max_slices=12*N 
    #We check if K lies between min_slices and max_slices. If it does, it means it's possible for Chef to have eaten exactly K slices, so we add "YES" to the results.Otherwise, we add "NO" to indicate it’s not possible to reach exactly K slices with N oranges.
    if(min_slices<=K<=max_slices):
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res)) #Finally, we print each result ("YES" or "NO") on a new line for each test case.converts the list of results into a single string, where each result is separated by a newline.

#time complexity: O(n)



T=int(input())
for i in range(T):
      n,k=map(int,input().split())
      if (k<10*n or k>12*n):
         print("no")
      else:
         print("yes")