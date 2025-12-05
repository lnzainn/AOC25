with open('input.txt', 'r') as f:
    turn_command = [line.strip() for line in f]

# turn_command = ['R300']
facing_direction = []
starting_point = 0
passing_counter = 0

for command in turn_command:

    if command[0] == 'L':
        coordinate = (starting_point - (int(command[1:]) % 100))
        nsum = starting_point - (int(command[1:]))
        if nsum < 0:
            passing_counter = passing_counter + 1 + nsum//-100


        if coordinate == 100 or coordinate == 0:
            facing_direction.append(0)
        elif coordinate < 0:
            facing_direction.append(100 + coordinate)
        elif coordinate > 100:
            facing_direction.append(coordinate % 100)
        else:
            facing_direction.append(coordinate)

    elif command[0] == 'R':
        coordinate = (starting_point + (int(command[1:]) % 100))
        nsum = starting_point + (int(command[1:]))
        if nsum > 100:
            passing_counter = passing_counter + nsum//100
        
        if coordinate == 100 or coordinate == 0:
            facing_direction.append(0)
        elif coordinate < 0:
            facing_direction.append(100 + coordinate)
        elif coordinate > 100:
            facing_direction.append(coordinate % 100)
        else:
            facing_direction.append(coordinate)

    else:
        continue

    starting_point = facing_direction[-1]

# print(f'Starting point = {starting_point}, passing counter = {passing_counter}')
# print(facing_direction)
# print(starting_point)

sum = 0

for i in facing_direction:
    if i == 0:
        sum += 1

print(sum + passing_counter)