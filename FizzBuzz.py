x, y , N = map(int, input().split())
for i in range(1, N + 1):
    if i % y != 0 and i % x == 0:
        print('Fizz')
    elif i % x != 0 and i % y == 0:
        print('Buzz')
    elif i % x == 0 and i % y == 0:
        print('FizzBuzz')
    else:
        print(i)
    i += 1
