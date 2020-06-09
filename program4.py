n= int(input("Enter a number : "))
a = (n - 1)//2
b = 3*n//2-1
for x in range(0,n):
    for y in range(0,n):
        if(x + y <= a or x - y >= a or y - x >= a or x + y >= b):
            print("*",end="")
        else:
            print(" ",end="")
    print()