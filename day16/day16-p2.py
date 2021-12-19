# Evaluate the expression represented by the hexadecimal-encoded transmission
#
# ID 4 = literal value
# ID 0 = sum
# ID 1 = product
# ID 2 = minimum
# ID 3 = maximum
# ID 5 = greater than
# ID 6 = less than
# ID 7 = equal to


import math

with open('input.txt', 'r') as file:
    packet = file.read().rstrip()

data = ''

for hex_value in packet:
    data += bin(int(hex_value, 16))[2:].zfill(4)  # Pad out binary number


def parse_header(pos):
    packet_version = int(data[pos:pos+3], 2)
    packet_type_id = int(data[pos+3:pos+6], 2)
    
    if packet_type_id == 4:
        pos, result = parse_literal(pos+6)
    else:
        pos, result = parse_operator(pos+6, packet_type_id)
    
    return pos, result


def parse_literal(pos):
    literal = ''
    group_end = False

    while not group_end:
        group = int(data[pos])
        literal += data[pos+1:pos+5]

        group_end = group == 0
        pos += 5
    
    return pos, int(literal, 2)


def parse_operator(pos, operator):
    length_type_id = int(data[pos])
    
    if length_type_id == 1:
        num_sub_packets = int(data[pos+1:pos+12], 2)
        pos, values = parse_sub_packets(pos+12, num_sub_packets)
    else:  # length_type_id == 0
        length_sub_packets = int(data[pos+1:pos+16], 2)
        pos, values = parse_length(pos+16, length_sub_packets)
    
    return pos, apply_operator(operator, values)


def parse_sub_packets(pos, num):
    values = []

    for _ in range(num):
        pos, result = parse_header(pos)
        values.append(result)

    return pos, values


def parse_length(pos, length):
    values = []
    end = pos + length
    
    while pos != end:
        pos, result = parse_header(pos)
        values.append(result)

    return pos, values


def apply_operator(operator, values):
    # Sum
    if operator == 0:
        return sum(values)
    # Product
    elif operator == 1:
        return math.prod(values)
    # Minimum
    elif operator == 2:
        return min(values)
    # Maximum
    elif operator == 3:
        return max(values)
    # Greater than
    elif operator == 5:
        return 1 if values[0] > values[1] else 0
    # Less than
    elif operator == 6:
        return 1 if values[0] < values[1] else 0
    # Equal to
    else:  # operator == 7
        return 1 if values[0] == values[1] else 0


print(parse_header(0)[1])  # Answer: 68703010504
