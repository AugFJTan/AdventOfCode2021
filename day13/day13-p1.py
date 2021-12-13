# How many dots are visible after completing just the first fold instruction?

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
    
    # Parse first instruction only
    instruction = next(file).rstrip().split()[2].split('=')

    axis = instruction[0]
    value = int(instruction[1])
     
    result = fold(paper, axis, value)

count = 0

for row in result:
    count += sum(row)

print(count)  # Answer: 708
