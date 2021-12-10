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
