numbers = list(map(int, input().split()))

max_inlist = numbers[0]
min_inlist = numbers[0]

for i in numbers[1:]:
    if i > max_inlist:
        max_inlist = i
    elif i < min_inlist:
        min_inlist = i

print(min_inlist, max_inlist)