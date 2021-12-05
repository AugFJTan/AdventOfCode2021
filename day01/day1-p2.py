# Count the number of times the sum of measurements in this sliding window increases

count = 0

with open('input.txt', 'r') as file:
    prev_window = [ int(file.readline()) ]
    
    for line in file:
        current_window = prev_window[:]
        current_window.append(int(line))
        
        if len(current_window) > 3:
            current_window.pop(0)
        
            if sum(current_window) > sum(prev_window):
                count += 1
        
        prev_window = current_window[:]

print(count)  # Answer: 1150

