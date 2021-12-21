# If any pair is nested inside 4 pairs, the leftmost such pair explodes
# To explode a pair:
#  - The pair's left value is added to the first regular number to the left (if any)
#  - The pair's right value is added to the first regular number to the right (if any)
#  - The exploding pair is replaced with the regular number 0
#
# If any regular number >= 10, the leftmost such regular number splits
# To split a regular number, replace it with a pair:
#  - The left element should be the regular number divided by 2 and rounded down
#  - The right element should be the regular number divided by 2 and rounded up
#
# Magnitude:
#  - Pair = 3x magnitude of left element + 2x magnitude of right element
#  - Regular number = itself
#  - Magnitude calculations are recursive
#
# Add up all of solutions in the order they appear
# What is the magnitude of the final sum?


class Pair:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def get_value(self):
        return [self.lhs.get_value(), self.rhs.get_value()]
    
    def reduce(self, parent=None, level=0):
        current = self
        
        if isinstance(current.lhs, Pair):
            current.lhs.reduce(current, level+1)
        elif isinstance(current.rhs, Pair):
            current.rhs.reduce(current, level+1)
        elif level == 4:
            parent.explode()
    
    def explode(self):
        if isinstance(self.lhs, Pair):
            pair = self.lhs
            regular = self.rhs
            
            self.lhs = RegularNumber(0)
            self.rhs = RegularNumber(pair.rhs.get_value() + regular.get_value())
        elif isinstance(self.rhs, Pair):
            regular = self.lhs
            pair = self.rhs
            
            self.lhs = RegularNumber(pair.lhs.get_value() + regular.get_value())
            self.rhs = RegularNumber(0)


class RegularNumber:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


data = 'RAW DATA HERE'


def parse_number(raw):
    if raw.isnumeric():
        return RegularNumber(int(raw))

    comma = -1
    level = 0
    
    for pos in range(len(raw)):
        if raw[pos] == '[':
            level += 1
        elif raw[pos] == ']':
            level -= 1
        elif raw[pos] == ',':
            if level == 1:
                comma = pos
    
    lhs = raw[1:comma]
    rhs = raw[comma+1:-1]
    
    return Pair(parse_number(lhs), parse_number(rhs))


number = parse_number(data)
number.reduce()

print(number.get_value())
