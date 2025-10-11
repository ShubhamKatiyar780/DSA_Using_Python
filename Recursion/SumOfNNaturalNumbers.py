def fun(n):
    if n == 1:            # Base case
        return 1
    return n + fun(n - 1)  # Recursive case
n = int(input("Enter the Value: "))
print("Sum of",n,"Natural Numbers is:",fun(n))