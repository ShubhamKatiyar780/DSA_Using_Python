def fun(n):
    if n == 1:            # Base case
        return 2
    return 2*n + fun(n - 1)  # Recursive case
n = int(input("Enter the Value: "))
print("Sum of",n,"Even Natural Numbers is:",fun(n))