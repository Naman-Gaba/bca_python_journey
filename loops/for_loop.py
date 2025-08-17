#q1 print the numbers in list
nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

#q2 search for a number x using truples in loop
num=(1,4,9,16,25,36,49,64,81,100)
x=64
ind=0
for val in num:
    if(val==x):
        print("number found at index",ind)
        break
    ind=ind+1

