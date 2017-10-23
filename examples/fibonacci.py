# Python program to find the factorial of a number provided by the user.

print('This is Fibonacci! Starts with 0, 1 and every other number in sequence is sum of last 2.')
print('Tell me how many terms you want to see, and I ll compute them for you!')
# take input from the user
n = -1
while not (0 <= n <= 35):
    n = int(input("Enter a number between 0 and 35: "))

# first 2 terms are 0 and 1
print(0, end=', ')
if n > 0:
    print(1, end=', ')

a = 0
b = 1
for i in range(n):
    tmp = a
    a = b
    b = tmp + b
    # previous 3 lines could be written shortly as
    # a, b = b, a + b
    # try it!
    print(b, end=', ')
