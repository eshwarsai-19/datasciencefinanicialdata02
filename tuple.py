''' in tuple is a inmutable we cant change it'''


# practicing the tuple here

t1=()

t3=(1,2,3,4)
t4=tuple('abc')
t5=tuple([1,2,3])

print(t1,t3,t4,t5,sep="\n")


# indexing of tuple


print(t3[0])
print(t3[2])
print(t3[-1])

# example of tuple using methods

tup=(1,6,2,6,4,6)
print(tup.count(6))


''' this count method is used to count how many are there in a tuple

'''

t8=(20,30,40,50,60)
print(t8[::2])      # it will  skip the by depending on what we assign index
print(t8[::-1])     # it will show all elemnets in reverse order
print(t8[2:])       #it will print the beyond we mention the element
print(t8[:3])       #it will print how many index we mention
