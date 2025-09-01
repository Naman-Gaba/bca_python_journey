num=int(input("enter a number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
#wth for loop
sum1=0
for i in range(0,num):
    dig1=num%10
    sum1=sum1+dig1
    num=num//10
print(sum1)
