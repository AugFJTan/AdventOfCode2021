def absolute(r1, r2):
    return (r1[0] - r2[0], r1[1] - r2[1], r1[2] - r2[2])

def offset(r1, r2):
    return (r1[0] + r2[0], r1[1] + r2[1], r1[2] + r2[2])


def rotateX90(pos):
    return (pos[0], -pos[2], pos[1])

def rotateY90(pos):
    return (pos[2], pos[1], -pos[0])

def rotateZ90(pos):
    return (-pos[1], pos[0], pos[2])


def get_orientations(point):
    orientations = []

    for i in range(6):
        for _ in range(4):
            orientations.append(point)
            point = rotateZ90(point)
        
        if i == 0:
            point = rotateX90(point)
        elif i >= 1 and i <= 3:
            point = rotateY90(point)
        else:
            point = rotateX90(point)

    return orientations


beacons = []

with open('input.txt', 'r') as file:
    file.readline()
    coords = []

    for line in file:
        if line.rstrip() == '':
            file.readline()
            beacons.append(coords)
            coords = []
        else:
            coords.append(tuple(map(int, line.rstrip().split(','))))

    beacons.append(coords)


aligned = []
scanners = []

for _ in range(len(beacons)):
    aligned.append(False)
    scanners.append((0,0,0))

aligned[0] = True



def align_to_s0(ref, algn):
    beacons_s0 = beacons[ref]
    beacons_s1 = beacons[algn]

    s1_orientations = []

    for beacon in beacons_s1:
        s1_orientations.append(get_orientations(beacon))

    matches = set()
    orientations = []
    finish = False

    for b0 in beacons_s0:
        for j in range(24):
            
            b1_set = [s1_orientations[k][j] for k in range(len(s1_orientations))]
            
            # Find overlap
            for i in range(len(s1_orientations)):
                b1 = s1_orientations[i][j]
                s1 = absolute(b0, b1)

                for beacon1 in b1_set:
                    if beacon1 == b1:
                        continue
                    
                    test = offset(s1, beacon1)
                    
                    if test in beacons_s0:
                        scanners[algn] = s1
                        orientations.append(j)
                        matches.add(test)

    if len(matches) > 0:
        adj = max(orientations, key=orientations.count)
        beacons[algn] = [s1_orientations[k][adj] for k in range(len(s1_orientations))]
        aligned[algn] = True


tried = []
unaligned = [i for i in range(1, len(beacons))]
ref = 0

while unaligned:
    for idx in range(len(beacons)):
        if aligned[idx] and idx not in tried:
            ref = idx
            break

    for idx in unaligned:
        align_to_s0(ref, idx)

    for idx in unaligned:
        if aligned[idx]:
            unaligned.remove(idx)

    tried.append(ref)
    print(unaligned)


all_beacons = set()

for b in beacons[0]:
    all_beacons.add(b)

for i in range(1, len(beacons)):
    for j in range(len(beacons[i])):
        all_beacons.add(offset(scanners[i], beacons[i][j]))

print(len(all_beacons))
