# here practcing the strings methods in python

s1="welcome to my world"

s2="PyThoN"
s3="     namaste   "

print(s1.capitalize())

print(s2.center(16,"$"))

print(s1.count('o'))

print(s1.endswith("rld"))

print(s1.startswith("wel")) 

print(s1.find('m'))          #it will find the index position of element from starting

print(s1.rfind('y'))        #it will find the index position of element from reverse order

print(s1.index('c'))        #it will find the index position of element from starting

print(s2.rindex('h'))       #it will find the index position of element from reverse order

print(s1.title())           #it will captialize the each intial word in string

print(s1.upper())
print(s1.lower())

print(s2.lower())
print(s2.upper())


print(s3.strip())       #it will remove the gaps btw the strings

print(s1.replace("world","data science"))

print(s2.replace("python","data science"))

print(s1.split(" ",))

print(s1.split("o"))

print(s1.split(" ",1))

print(s2.swapcase())        #it will swap the small to captial and captial to small

