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


import math

class Pair:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def get_value(self):
        return [self.lhs.get_value(), self.rhs.get_value()]
    
    def reduce(self, level=0):
        left_reduce = self.lhs.reduce(level+1)
        right_reduce = self.rhs.reduce(level+1)

        if level == 4:
            return self

        if left_reduce:
            return left_reduce
        elif right_reduce:
            return right_reduce
        else:
            return None
    
    def contains(self, value):
        if self == value:
            return True
        else:
            return self.lhs.contains(value) or self.rhs.contains(value)
    
    def get_leftmost(self):
        if isinstance(self.lhs, RegularNumber):
            return self.lhs
        else:
            return self.lhs.get_leftmost()
    
    def get_rightmost(self):
        if isinstance(self.rhs, RegularNumber):
            return self.rhs
        else:
            return self.rhs.get_rightmost()
    
    def replace(self, parent, existing, new):
        if parent.lhs == existing:
            parent.lhs = new
        elif parent.rhs == existing:
            parent.rhs = new
        elif parent.lhs.contains(existing):
            parent.lhs.replace(self, existing, new)
        else:
            parent.rhs.replace(self, existing, new)
    
    def get_magnitude(self):
        return self.lhs.get_magnitude() * 3 + self.rhs.get_magnitude() * 2


class RegularNumber:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def reduce(self, level):
        if self.value >= 10:
            return self
        else:
            return None
    
    def contains(self, value):
        return self == value
    
    def replace(self, parent, existing, new):
        if self == existing:
            self.value = new.value
    
    def get_magnitude(self):
        return self.value


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


def explode_pair(root, exploded):
    current = root
    left = None
    right = None

    while current != exploded:
        if current.lhs.contains(exploded):
            right = current.rhs
            current = current.lhs
        else:
            left = current.lhs
            current = current.rhs

    if left:
        if isinstance(left, Pair):
            left_regular = left.get_rightmost()
        else:
            left_regular = left

        left_replace = RegularNumber(current.lhs.get_value() + left_regular.get_value())
        root.replace(root, left_regular, left_replace)

    if right:
        if isinstance(right, Pair):
            right_regular = right.get_leftmost()
        else:
            right_regular = right

        right_replace = RegularNumber(current.rhs.get_value() + right_regular.get_value())
        root.replace(root, right_regular, right_replace)

    root.replace(root, exploded, RegularNumber(0))


def split_regular(root, split):
    round_down = math.floor(split.value / 2)
    round_up   = math.ceil(split.value / 2)
    split_pair = Pair(RegularNumber(round_down), RegularNumber(round_up))
    root.replace(root, split, split_pair)


with open('input.txt', 'r') as file:
    lhs = parse_number(file.readline().rstrip())

    for line in file:
        rhs = parse_number(line.rstrip())

        number = Pair(lhs, rhs)

        while True:
            reduced = number.reduce()

            if not reduced:
                break

            if isinstance(reduced, Pair):
                explode_pair(number, reduced)
            else:
                split_regular(number, reduced)

        lhs = rhs

    print(number.get_magnitude())
