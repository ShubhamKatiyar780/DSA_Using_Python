a = [12, 'Shubham', 10.5, "A", 1.2, 6, 0, 'Katiyar']
# a.append('p')
# a.extend('Shu')
# a.pop(1)
# a.remove(10.5)
# print(a)

for i in a.copy():
    if (type(i) != int):
        a.remove(i)
print(a)