def function(n):
    if n >= 1:               # Base case
        print(n, end=' ')
        function(n - 1)     # Recursive case
print("---------------Print N Natural Numbers in Reverse Order---------------")
n = int(input("Enter the Value of N: "))
function(n)