def function(n):
    if n > 0:               # Base case
        function(n - 1)     # Recursive case
        print(n, end=' ')
print("---------------Print N Natural Numbers---------------")
n = int(input("Enter the Value of N: "))
function(n)