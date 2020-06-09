#Program to print the nature of a number..
"""
1 - odd
2 - even
3 - prime
4 - palindrome
5 - armstrong
"""
number = int(input("Enter a number : "))
#Logic to print even/odd:-
if number % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

#Logic to print number is prime or not:-
for i in range(2,number-1):
    if number % i != 0:
        print("Given number is prime")
        break
    else:
        print("Number is not prime")
        break
#Logic to check given number is palindrome or not:-
num = int(input("Enter a number.: "))
reverse = 0
temp = num
while(temp > 0):
    Reminder = temp % 10
    reverse = (reverse * 10) + Reminder
    temp = temp //  10
if num == reverse:
    print(num," is a palindrome number")
else:
    print(num,"is not a palindrome number")

#Logic to check given no. is armstrong or not:-

# take input from the user
num = int(input("Enter a number: "))
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")








