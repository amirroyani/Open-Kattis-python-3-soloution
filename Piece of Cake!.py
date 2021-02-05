n, h, v = map(int, input().split())
j = []
j.append(h * v)
j.append((n-h) * v)
j.append((n-v) * h)
j.append((n - h) * (n - v))
print(max(j) * 4)
