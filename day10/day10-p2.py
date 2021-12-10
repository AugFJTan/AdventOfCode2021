# Find the completion string for each incomplete line
# What is the middle score?

from corrupted import find_illegal

score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def find_incomplete(data):
    level = 0
    chunk_tree = []

    for symbol in list(data):
        # Opening
        if symbol in "([{<":
            level += 1
            chunk_tree.append((level, symbol))

        # Closing
        if symbol in ")]}>":
            for chunk_data in chunk_tree:
                open_level, open_symbol = chunk_data
                
                if level == open_level:
                    if (open_symbol == '(' and symbol == ')') or \
                       (open_symbol == '[' and symbol == ']') or \
                       (open_symbol == '{' and symbol == '}') or \
                       (open_symbol == '<' and symbol == '>'):
                        level -= 1
                        chunk_tree.remove(chunk_data)

    chunk_tree.reverse()

    missing = []
    
    for _, open_symbol in chunk_tree:
        if open_symbol == '(':
            close_symbol = ')'
        elif open_symbol == '[':
            close_symbol = ']'
        elif open_symbol == '{':
            close_symbol = '}'
        else:  # open_symbol == '<'
            close_symbol = '>'
        
        missing.append(close_symbol)

    return missing


incomplete = []

with open('input.txt', 'r') as file:
    for line in file:
        if not find_illegal(line):
            incomplete.append(line)


all_scores = []

for line in incomplete:
    current_score = 0

    for symbol in find_incomplete(line):
        current_score *= 5
        current_score += score[symbol]
    
    all_scores.append(current_score)

all_scores.sort()

# Get middle score
print(all_scores[len(all_scores) // 2])  # Answer: 4038824534
