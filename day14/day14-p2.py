# Apply 40 steps of pair insertion to the polymer template
# Find difference between quantity of the most common element and least common element

import functools


with open('input.txt', 'r') as file:
    template = file.readline().rstrip()

    file.readline()  # Skip blank line
    
    rules = {}
    elements = set()
    
    for line in file:
        pair, insert = line.rstrip().split(' -> ')
        rules[pair] = insert

        elements.update([pair[0], pair[1], insert])


def get_count_dict():
    return dict.fromkeys(list(elements), 0)


def sum_of_dicts(d1, d2):
    d3 = get_count_dict()
    
    for e in list(elements):
        d3[e] = d1[e] + d2[e]
    
    return d3


@functools.lru_cache(None) 
def insert_pair(pair, step):
    if step == 0:
        count = get_count_dict()
        count[pair[1]] = 1
        return count
    
    element = rules[pair]
    
    return sum_of_dicts(insert_pair(pair[0] + element, step-1),
                        insert_pair(element + pair[1], step-1))


count = get_count_dict()

# Count first character in template
count[template[0]] = 1

for i in range(len(template)-1):
    count = sum_of_dicts(count, insert_pair(template[i:i+2], 40))

most_common = max(count, key=count.get)
least_common = min(count, key=count.get)

print(count[most_common] - count[least_common])  # Answer: 5725739914282
