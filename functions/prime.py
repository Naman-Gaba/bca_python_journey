def prime(num):
    if num < 2:
        print("not prime")
        return
    
    for i in range(2, num):
        if num % i == 0:   # found divisor
            print("not prime")
            return
    
    # if loop completes, no divisor found
    print("prime", num)

prime(17)  # prime
prime(12)  # not prime

##def prime(num):
#    if num < 2:
     #   print("not prime")
    #    return  # stop here if <2
   # 
  #  for i in range(2, num):
    #    if num % i == 0:
   #         print("not prime")
  #          return  # stop as soon as one divisor is found
 #   
#    print("prime", num)

