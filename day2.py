with open('AOC25/input.txt', 'r') as f:
    input_range = f.readline()

# input_range = '12000-200000'
invalid_range = []

input_range = input_range.split(',')


for i in range(0, len(input_range)):
    l1 = int(input_range[i].split('-')[0])
    l2 = int(input_range[i].split('-')[1])
    
    for j in range(l1, l2 + 1):   
        if len(str(j)) % 2 == 0:
            if str(j)[0:int(len(str(j))/2)] == str(j)[int(len(str(j))/2):]:
                invalid_range.append(j)

            elif len(str(j)) == 6:
                if str(j)[0:2] == str(j)[4:6] == str(j)[2:4]:
                    invalid_range.append(j)

            elif len(str(j)) == 8:
                if str(j)[0:2] == str(j)[6:8] == str(j)[2:4] == str(j)[4:6]:
                    invalid_range.append(j)

            elif len(str(j)) == 10:
                if str(j)[0:2] == str(j)[2:4] == str(j)[4:6] == str(j)[6:8] == str(j)[8:10]:
                    invalid_range.append(j)

            else:
                continue
            

        elif len(str(j)) == 3:
            if str(j)[0] == str(j)[1] == str(j)[2]:
                invalid_range.append(j)

        elif len(str(j)) == 5:
            if str(j)[0] == str(j)[1] == str(j)[2] == str(j)[3] == str(j)[4]:
                invalid_range.append(j)

        elif len(str(j)) == 7:
            if str(j)[0] == str(j)[1] == str(j)[2] == str(j)[3] == str(j)[4] == str(j)[5] == str(j)[6]:
                invalid_range.append(j)

        elif len(str(j)) == 9:
            if str(j)[0:3] == str(j)[3:6] == str(j)[6:9]: 
                invalid_range.append(j)


            
print(invalid_range)

sum = 0
for l in invalid_range:
    sum += l

print(sum)


