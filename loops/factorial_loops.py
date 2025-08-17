#factorial of first n natural numbers using for loop
n=int(input("enter a number: "))
pro=1
for i in range(1,n+1):
    pro=pro*i
    i=i+1
print(pro)

#using while 

k=int(input("enter a number: "))
multi=1 
i=1 
while i<=k:
    multi=multi*i
    i=i+1
print(multi)