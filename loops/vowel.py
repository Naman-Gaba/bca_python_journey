string=input("enter a string: ")
vowels="aeiouAEIOU"
count=0
i=0
while i<len(string):
    if string[i] in vowels:
        count+=1
    i+=1
print("number of vowels",count)
