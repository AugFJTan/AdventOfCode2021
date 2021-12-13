# Finish folding the transparent paper according to the instructions
# What code do you use to activate the infrared thermal imaging camera system?

from instruction import fold

paper = []

paper_width = 1311
paper_height = 895

for i in range(paper_height):
    paper.append([0] * paper_width)

with open('input.txt', 'r') as file:
    for line in file:
        if line.rstrip() == '':
            break
        
        x, y = list(map(int, line.rstrip().split(',')))
        
        paper[y][x] = 1
    
    result = paper
    
    # Parse instructions
    for line in file:
        instruction = line.rstrip().split()[2].split('=')

        axis = instruction[0]
        value = int(instruction[1])
        
        result = fold(result, axis, value)

# Print out code with block characters and spaces
for row in result:
    for dot in row:
        if dot == 1:
            print('\u2588', end='')
        else:
            print(' ', end='')
    print()

# Answer: EBLUBRFH
