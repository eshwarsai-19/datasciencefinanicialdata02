# here practice the stars using loops


for i in range(5):                                         
    for j in range(5):
        print("*",end=" ")

    print(" ") 


#for left reverse pattern triangle star

l=int(input("enter the number:"))
for i in range(l,0,-1):
    for j in range(i,0,-1):  
        print("*",end=" ")
    print()

#a left star pattern triangle



n=int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# #or


m=6
for i in range(1,m+1):
    x=''*(m-i)     #here no space between the ''
    y='*'*(1*i-1)
    print(x+y) 


#generate a equalateral triangle star pattern

e=int(input("enter a number :"))
for i in range(1,e+1):
    x=' '*(e-i)     #here a  space  needed between the ''
    y='*'*(2*i-1)
    print(x+y) 


   