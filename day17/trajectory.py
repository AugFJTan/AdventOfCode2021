def check_hit(pos, xbox, ybox):
    x, y = pos

    if x >= xbox[0] and x <= xbox[1] and \
       y >= ybox[0] and y <= ybox[1]:
        return True, False   # Hit, stop

    if x > xbox[1]:
        return False, False  # Miss, stop

    if y < ybox[0]:
        return False, False  # Miss, stop

    return False, True       # Continue


def update_trajectory(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]

    if vel[0] > 0:
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1

    vel[1] -= 1
