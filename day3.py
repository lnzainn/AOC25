# with open('input.txt', 'r') as f:
#     joltages = [line.strip() for line in f]

joltages = '123455'

max1 = max2 = float('-inf')
for n in joltages:
    if int(n) > max1:
        max2 = max1  
        max1 = int(n)
    elif int(n) > max2 and int(n) != max1:
        max2 = int(n)
print(max1, max2)