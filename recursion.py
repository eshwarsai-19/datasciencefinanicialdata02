#doing practice on recursion method

'''this recursion for like doing calling the function itself
or
when calling the function repeatadly '''

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))


#or we can use math for factorial

import math

print(math.factorial(5))
