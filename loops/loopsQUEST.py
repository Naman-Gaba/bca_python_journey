#q1 WAP to find sum of first n natural numbers using while.
n=int(input("enter a number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i=i+1
print("sum of all numbers",sum)

#using for
k=int(input("enter a number: "))
sum=0
for j in range(1,k+1):
    sum=sum+j
print("total sum=",sum)