# Find the first illegal character in each corrupted line of the navigation subsystem
# What is the total syntax error score for those errors?

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def find_illegal(data):
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
                    else:
                        return symbol

    return None


result = 0

with open('input.txt', 'r') as file:
    for line in file:
        illegal = find_illegal(line)
        if illegal:
            result += score[illegal]

print(result)  # Answer: 268845
