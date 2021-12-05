# Use the binary numbers in your diagnostic report:
# Calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together.
# What is the life support rating of the submarine?

O2_bucket = []
CO2_bucket = []

with open('input.txt', 'r') as file:
    for line in file:
        if line[0] == '1':
            O2_bucket.append(line.rstrip())
        else:
            CO2_bucket.append(line.rstrip())

def bit_filter(bucket, priority):
    remaining = bucket[:]
    
    for i in range(1, 12):
        bit_count = 0
        candidates = []
        
        for value in remaining:
            if value[i] == '1':
                bit_count += 1
    
        one_bits = bit_count
        zero_bits = len(remaining) - bit_count
        
        for value in remaining:
            if one_bits == zero_bits:
                evaluate = priority
            elif priority == '1':
                evaluate = '1' if one_bits > zero_bits else '0'
            else:
                evaluate = '1' if one_bits < zero_bits else '0'

            if value[i] == evaluate:
                candidates.append(value)
        
        remaining = candidates[:]
        
        if len(candidates) == 1:
            return candidates[0]
    
    return None   # Check for error

O2_rating = bit_filter(O2_bucket, '1')
CO2_rating = bit_filter(CO2_bucket, '0')

print(int(O2_rating, 2) * int(CO2_rating, 2))  # Answer: 1613181
