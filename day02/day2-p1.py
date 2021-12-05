# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

position = [0, 0]  # xy coordinates

with open('input.txt', 'r') as file:
    for line in file:
        direction, magnitude = line.split()
        
        if direction == "forward":
            position[0] += int(magnitude)
        elif direction == "down":
            position[1] += int(magnitude)
        elif direction == "up":
            position[1] -= int(magnitude)

print(position[0] * position[1])  # Answer: 2019945
