def function(n):
    if n > 0:               # Base case
        function(n - 1)     # Recursive case
        print(2*n, end=' ')
print("---------------Print N Even Natural Numbers---------------")
n = int(input("Enter the Value of N: "))
function(n)