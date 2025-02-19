n = int(input("enter a number: "))
l = []
a, b = 0, 1
for i in range(n):
    l.append(a)
    # a, b = b, a+b
    ccc=a+b
    a=b
    b=ccc
print(l)