n = int(input())
x = 0
s = 0
z = 0
while x != n:
    string = input()
    q = float(string.split()[0])
    y = float(string.split()[1])
    x += 1
    s = q * y
    z += s
print(z)
