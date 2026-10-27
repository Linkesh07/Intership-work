# 1 Write a Python program to check whether a given number is positive, negative, or zero.
n = int(input())
if n > 0:
    print ("positive")
elif n < 0:
    print ("negative")
else:
    print ("Zero")

# 2 Write a Python program to check whether a given number is even or odd.

n = int(input())
if n % 2 == 0:
    print ("even ")
else:
    print ("odd")

# 3 Write a Python program to find the largest of two numbers without using max().


a = int(input(" first number: "))
b = int(input(" second number: "))

if a > b:
    print("The largest number is:", a)
elif b > a:
    print("The largest number is:", b)
else:
    print("Two numbers are equal")

# 4 Write a Python program to find the largest of three numbers using if/elif/else.

a = int(input(" first number: "))
b = int(input(" second number: "))
c = int(input(" Third number: "))

if a >= b and a >= c :
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

# 5 Write a Python program to check whether a person is eligible to vote based on age. Handle invalid ages.

n = int(input())
if n >= 18:
    print ("This person is eligible to vote")
else :
    print (" Not eligible for vote")

# 6. Write a Python program to accept marks and print the grade based on the following: 90–100 = A, 75–89 = B, 50–74 = C, below 50 = Fail.

n = int(input())
if n >= 90:
    print ("A grade")
elif n>= 75:
    print ("B grade")
elif n>= 50:
    print ("C grade")
else:
    print("Fail")

# 7. Write a Python program to check whether a given year is a leap year.
n = int(input())
if n % 4 == 0 :
    print ("Leap year")
else :
    print (" Non Leap year")

# 8. Write a Python program to check whether a number is divisible by both 3 and 5.
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print ("Divisible")
else :
    print (" Not Divisible")

# 9. Write a Python program to determine whether a character is uppercase, lowercase, a digit, or a special character.

name = input("Enter a character: ")

if name.isupper():
    print(" character is uppercase")
elif name.islower():
    print(" character is  lowercase")
elif name.isdigit():
    print(" character is a digit")
else:
    print(" character is a special character")

# 10. Write a simple calculator using if/elif/else that accepts two numbers and an operator (+, -, *, /).

a = int(input("First number: "))
b = int(input("Second number: "))
op = input()
if op == "+":
    print("Addition:", a + b)

elif op == "-":
    print("Subtraction:", a - b)

elif op == "*":
    print("Multiplication:", a * b)

elif op == "%":
    print("Division:", a % b)

else:
    print("Error")

# 11.Write a Python program to print all numbers from 1 to N using a loop.

n = int(input())

for i in range(1, n + 1):
    print(i)




#  12.Write a Python program to print all even numbers between 1 and N.

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


# 13. Write a Python program to calculate the sum of all numbers from 1 to N.
n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)


# 14. Write a Python program to print the multiplication table of a given number from 1 to 10.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 15. Write a Python program to count the number of digits in an integer using a loop.
n = int(input())
count = 0

n = abs(n)

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count = count + 1

print("Number of digits:", count)

# 16. Write a Python program to reverse a number using a loop. Do not convert the number to a string.

n = int(input())
num = abs(n)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if n < 0:
    reverse = -reverse

print("Reversed number:", reverse)

# 17. Write a Python program to calculate the sum of the digits of a given number.


n = int(input("Enter a number: "))
n = abs(n)
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits:", total)

#  18. Write a Python program to calculate the factorial of a given number using a loop.

n = int(input())
factorial = 1

if n < 0:
    print("Factorial is not defined ")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial:", factorial)

# 19. Given a list of numbers, write a Python program to count how many numbers are even and how many are odd.


n = [10, 15, 20, 7, 8, 13, 4]

even_count = 0
odd_count = 0

for i in n:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 20. Given a list of numbers, find the largest number without using max() or sort().

n = [12, 45, 7, 89, 23, 56]

largest = n[0]

for i in n:
    if i > largest:
        largest = i

print("Largest number:", largest)

# 21. Write a Python program to check whether a given number is prime.

n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# 22. Write a Python program to print all prime numbers between 1 and N.


n = int(input("Enter the value of N: "))

for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

# 23. Write a Python program to print the first N numbers in the Fibonacci series.
n = int(input())

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 24. Write a Python program to reverse a string using a loop without using slicing.

name = input("Enter a string: ")
reverse = ""

for i in name:
    reverse = i + reverse

print("Reversed string:", reverse)

# 25. Write a Python program to print the following pattern using nested loops:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# 26. Write a Python program to check whether a given number is a palindrome. Do not convert the number to a string.
n = int(input("Enter a number: "))
original, reverse = n, 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Palindrome" if original == reverse else "Not palindrome")

# 27. Write a Python program to check whether a given number is an Armstrong number.


n = int(input("Enter a number: "))
digits, total, temp = len(str(n)), 0, n
while temp > 0:
    total += (temp % 10) ** digits
    temp //= 10
print("Armstrong" if total == n else "Not Armstrong")
# 28. Given a list of numbers, write a Python program to find and print all duplicate numbers. First solve it without using set().

n = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicates = []
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j] and n[i] not in duplicates:
            duplicates.append(n[i])
print("Duplicate numbers:", duplicates)

# 29. Given a list of numbers, write a Python program to find the second-largest unique number without using sort() or sorted().

n = [10, 20, 4, 45, 45, 30, 20]
largest = None
second_largest = None
for i in n:
    if largest is None or i > largest:
        if i != largest:
            second_largest = largest
        largest = i
    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i
if second_largest is None:
    print("No second-largest unique number")
else:
    print("Second-largest unique number:", second_largest)

# 30. Write a Python program that gives a user three attempts to enter the correct password. Display the remaining attempts after each failed attempt and print 'Account locked' if all attempts fail.
password = "python123"
for i in range(3):
    if input("Enter password: ") == password:
        print("Login successful")
        break
    else:
        print("Remaining attempts:", 2 - i) if i < 2 else print("Account locked")

