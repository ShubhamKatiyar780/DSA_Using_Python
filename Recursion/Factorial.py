def fun(n):
    if n == 1:            # Base case
        return 1
    return n * fun(n - 1)  # Recursive case
print("---------------Print Factorial Number---------------")
n = int(input("Enter the Value: "))
print("Factorial of",n, "is:",fun(n))