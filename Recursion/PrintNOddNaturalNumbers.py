def function(n):
    if n > 0:               # Base case
        function(n - 1)     # Recursive case
        print(2 * n - 1, end=' ')
print("---------------Print N Odd Natural Numbers---------------")
n = int(input("Enter the Value of N: "))
function(n)