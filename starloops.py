# here practice the stars using loops


for i in range(5):
    for j in range(5):
        print("*",end=" ")

    print(" ") 


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()

rows = 5

for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)



   