numbers_and_ranges = input().split(';')
counter = 0
for number_or_range in numbers_and_ranges:
    if '-' not in number_or_range:
        counter += 1
    else:
        start = int(number_or_range.split('-')[0])
        end = int(number_or_range.split('-')[1])
        counter += end - start + 1

print(counter)
