# Count the number of times a depth measurement increases from the previous measurement

count = 0

with open('input.txt', 'r') as file:
    prev_measurement = int(file.readline())
    
    for line in file:
        measurement = int(line)
        
        if measurement > prev_measurement:
            count += 1
        
        prev_measurement = measurement

print(count)  # Answer: 1215
