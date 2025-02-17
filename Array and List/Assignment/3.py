n = int(input("How many numbers do you have to calculate the average?: "))
a = []
for i in range(n):
    var = int(input(f"enter the number {i+1}: "))
    a.append(var)
print(f"The Average of {n} numbers is: {sum(a)/len(a)}")