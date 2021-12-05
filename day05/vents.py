def stepping(a, b):
    if b > a:
        b += 1
        step = 1
    else:
        b -= 1
        step = -1

    return a, b, step


def get_overlap(diagonal=False):
    # Create 1000x1000 map
    vent_map = []

    for _ in range(1000):
        row = [0]*1000
        vent_map.append(row)


    with open('input.txt', 'r') as file:
        for line in file:
            a, b = line.rstrip().split(' -> ')
            x1, y1 = a.split(',')
            x2, y2 = b.split(',')
            
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)
            
            if x1 == x2:
                start, end, step = stepping(y1, y2)
                
                for y in range(start, end, step):
                    vent_map[y][x1] += 1
            
            elif y1 == y2:
                start, end, step = stepping(x1, x2)

                for x in range(start, end, step):
                    vent_map[y1][x] += 1

            elif diagonal:
                x_start, x_end, x_step = stepping(x1, x2)
                y_start, y_end, y_step = stepping(y1, y2)
                
                x_points = [x for x in range(x_start, x_end, x_step)]
                y_points = [y for y in range(y_start, y_end, y_step)]

                for i in range(len(x_points)):
                    x, y = x_points[i], y_points[i]
                    vent_map[y][x] += 1


    count = 0

    for y in range(1000):
        for x in range(1000):
            if vent_map[y][x] >= 2:
                count += 1

    return count
    