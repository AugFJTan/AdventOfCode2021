# How many distinct initial velocity values can enter target area?


from trajectory import *


data = 'target area: x=102..157, y=-146..-90'

target = data[13:].split(', ')
x_target = list(map(int, target[0][2:].split('..')))
y_target = list(map(int, target[1][2:].split('..')))

hit_count = 0


for vx in range(-200, 200):
    for vy in range(-200, 200):
        position = [0, 0]
        velocity = [vx, vy]

        move = True

        while move:
            hit, move = check_hit(position, x_target, y_target)

            if hit:
                hit_count += 1

            update_trajectory(position, velocity)


print(hit_count)  # Answer: 5247
