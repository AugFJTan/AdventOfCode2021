# Parse hierarchy of packets and add up all version numbers
#
# Every packet begins with a standard header:
# - First 3 bits: Packet version
# - Next 3 bits : Type ID
# - Length type ID
#    + 0: next 15 bits = total length in bits of sub-packets
#    + 1: next 11 bits = number of sub-packets
#
# If packet type ID is 4, packet is literal value
# For each 5-bit value in this packet, 1 is not last group and 0 is last group


version_count = 0

with open('input.txt', 'r') as file:
    packet = file.read().rstrip()

data = ''

for hex_value in packet:
    data += bin(int(hex_value, 16))[2:].zfill(4)  # Pad out binary number


def parse_header(pos):
    global version_count

    packet_version = int(data[pos:pos+3], 2)
    packet_type_id = int(data[pos+3:pos+6], 2)
    
    version_count += packet_version
    
    if packet_type_id == 4:
        pos = parse_literal(pos+6)
    else:
        pos = parse_operator(pos+6)
    
    return pos


def parse_literal(pos):
    group_end = False

    while not group_end:
        group = int(data[pos])

        group_end = group == 0
        pos += 5
    
    return pos


def parse_operator(pos):
    length_type_id = int(data[pos])
    
    if length_type_id == 1:
        num_sub_packets = int(data[pos+1:pos+12], 2)
        return parse_sub_packets(pos+12, num_sub_packets)
    else:  # length_type_id == 0
        length_sub_packets = int(data[pos+1:pos+16], 2)
        return parse_length(pos+16, length_sub_packets)


def parse_sub_packets(pos, num):
    for _ in range(num):
        pos = parse_header(pos)

    return pos


def parse_length(pos, length):
    end = pos + length
    
    while pos != end:
        pos = parse_header(pos)

    return pos


parse_header(0)

print(version_count)  # Answer: 871
