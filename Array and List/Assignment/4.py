n = int(input("enter a number: "))
b = []
number = 2

# for i in range(n):
while (len(b) < n):
    for i in range(2, number):
        if (number % i == 0):
            break 
    else:         
        b.append(number)
    number += 1
print(b)