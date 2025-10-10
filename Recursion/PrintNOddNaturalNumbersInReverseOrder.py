def function(n):
    if n > 0:               # Base case
        print(2 * n - 1, end=' ')
        function(n - 1)     # Recursive case
print("---------------Print N Odd Natural Numbers in Reverse Order---------------")
n = int(input("Enter the Value of N: "))
function(n)