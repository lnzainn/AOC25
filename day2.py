# with open('input.txt', 'r') as f:
#     input_range = f.readline()

input_range = '100-12000'
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
            if str(j)[0:3] == str(j):
                pass


        else:
            lj = str(j)
            ll = len(lj)
            if lj[0:int(ll/2)] == lj[int(ll/2)+1::] and lj[0] == lj[int(ll/2)]:
                invalid_range.append(j)





            
print(invalid_range)
sum = 0

for l in invalid_range:
    sum += l

print(sum)


