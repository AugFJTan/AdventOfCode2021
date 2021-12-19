# Find initial velocity to reach highest y position and still enter target area
# What is the highest y position on this trajectory?


from trajectory import *


data = 'target area: x=102..157, y=-146..-90'

target = data[13:].split(', ')
x_target = list(map(int, target[0][2:].split('..')))
y_target = list(map(int, target[1][2:].split('..')))

y_max = []


for vx in range(200):
    for vy in range(200):
        position = [0, 0]
        velocity = [vx, vy]

        move = True

        y_pos = []

        while move:
            hit, move = check_hit(position, x_target, y_target)

            y_pos.append(position[1])

            if hit:
                y_max.append(max(y_pos))

            update_trajectory(position, velocity)


print(max(y_max))  # Answer: 10585

# Note: This max height is achived at: vx = 14 to 17, vy = 145
