def fun(n):
    if n == 1:            # Base case
        return 1
    return n**2 + fun(n - 1)  # Recursive case
n = int(input("Enter the Value: "))
print("Sum of Squares",n,"Natural Numbers is:",fun(n))