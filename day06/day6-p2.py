# How many lanternfish would there be after 256 days?
#
# Note: Using my Part 1 solution, the algorithm would use up too much memory and slow
#       to a crawl after 100+ iterations. A better solution is to use recursion!
#
# P.S.: This solution should work, it's just that Python is really bad with recursion :(
# P.P.S: Hooray for functools!!

import functools


with open('input.txt', 'r') as file:
    lanternfish = list(map(int, file.readline().split(',')))


@functools.lru_cache(256)   # Cache results of up to 256 recursive calls
def simulate(clock, days):
    if days == 0:
        return 1
    
    if clock == 0:
        return simulate(8, days-1) + simulate(6, days-1)
    else:
        return simulate(clock-1, days-1)


count = 0

for clock in lanternfish:
    count += simulate(clock, 256)
    
print(count)
