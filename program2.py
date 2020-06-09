#program to print fibonacci  series...

num = int(input("Enter the range upto which you want to print the series :  "))
a = 0
b = 1
if num <= 0:
    print("Please enter a number greater than 0")
elif num == 1:
    print(b)
else:
    print("Fibonacci series is:")
    for i in range(2,num):
     c = a + b
     a = b
     b = c
     print(b)




