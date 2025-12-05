# with open('input.txt', 'r') as f:
#     input_range = f.readline()

input_range = '110-111'
invalid_range = []

input_range = input_range.split(',')


for i in range(0, len(input_range)):
    l1 = int(input_range[i].split('-')[0])
    l2 = int(input_range[i].split('-')[1])
    
    for j in range(l1, l2 + 1):    # For cases like 13 13
        if len(str(j)) % 2 == 0:
            if str(j)[0:int(len(str(j))/2)] == str(j)[int(len(str(j))/2):]:
                invalid_range.append(j)

        elif len(str(j)) % 3 == 0:    # For cases like 13 13 13
            nsum = 0

            for a in range(int(str(j)[0]), len(str(j))):
                nsum += a
            print(a)





        elif len(str(j)) % 1 == 0:
            pass

            



            
# print(invalid_range)
# sum = 0

# for l in invalid_range:
#     sum += l

# print(sum)


