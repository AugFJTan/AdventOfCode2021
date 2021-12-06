# Each lanternfish will have an internal timer that counts to 0
#  - A lanternfish that create a new lanternfish will reset its internal timer to 6
#  - The new lanternfish will have an internal timer of 8
# How many lanternfish would there be after 80 days?

with open('input.txt', 'r') as file:
    lanternfish = list(map(int, file.readline().split(',')))


# Naïve solution; kept here for posterity :P
def simulate(clock, days):
    for _ in range(days):
        for i in range(len(clock)):
            if clock[i] == 0:
                clock.append(8)
                clock[i] = 6
            else:
                clock[i] -= 1

    return len(clock)


print(simulate(lanternfish, 80))  # Answer: 380612
