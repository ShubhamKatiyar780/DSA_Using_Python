def fun(n):
    if n == 1:            # Base case
        return 1
    return 2*n-1 + fun(n - 1)  # Recursive case
n = int(input("Enter the Value: "))
print("Sum of",n,"Odd Natural Numbers is:",fun(n))