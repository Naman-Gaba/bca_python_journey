n=int(input("enter a number :"))
count=0
for i in range(1,n+1):
    if(n%2==0):
        count+=1
if(count==2):
    print(n,"number is prime")
else:
    print(n,"number is not prime")