n = int(input())

answers = []
for i in range(n):
    answers.append(input())

count = 0
for i in range(n-1):
    if answers[i] == answers[i+1]:
        count += 1

print(count)
