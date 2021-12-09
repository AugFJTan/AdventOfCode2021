# For each entry, determine all of the wire/segment connections and 
# decode the four-digit output values.
# What do you get if you add up all of the output values?


#  111
# 2   3
# 2   3
#  444
# 5   6
# 5   6
#  777

ground_truth = {
    0: [1, 2, 3, 5, 6, 7],
    1: [3, 6],
    2: [1, 3, 4, 5, 7],
    3: [1, 3, 4, 6, 7],
    4: [2, 3, 4, 6],
    5: [1, 2, 4, 6, 7],
    6: [1, 2, 4, 5, 6, 7],
    7: [1, 3, 6],
    8: [1, 2, 3, 4, 5, 6, 7],
    9: [1, 2, 3, 4, 6, 7]
}


def set_segment(seg, pair, a, b, found):
    other = pair[0] if found == pair[1] else pair[1]
    
    seg[a] = found
    seg[b] = other


def decode_signals(data):
    input_values, output_values = data.split('|')

    decoder = {}
    possible235 = []
    possible069 = []

    for i in range(10):
        decoder[i] = []


    # Initialise decoder
    for value in input_values.split():
        n = -1

        if len(value) == 2:
            n = 1
        elif len(value) == 4:
            n = 4
        elif len(value) == 3:
            n = 7
        elif len(value) == 7:
            n = 8
        elif len(value) == 5:
            possible235.append(value)
        elif len(value) == 6:
            possible069.append(value)

        if n != -1:
            decoder[n] = [c for c in value]


    # Pair ambiguous segments
    remaining = list(set("abcdefg") - set(decoder[4]) - set(decoder[7]))

    segments = {}
    segments[1] = list(set(decoder[7]) - set(decoder[1]))[0]

    guess_24 = list(set(decoder[4]) - set(decoder[1]))
    guess_36 = decoder[1]
    guess_57 = remaining


    # Deduce segments
    for i in range(3):
        for j in range(3):
            outlier = list(set(possible235[i]) - set(possible235[j]))
            if len(outlier) == 1:
                 if outlier[0] in guess_24:
                    set_segment(segments, guess_24, 2, 4, outlier[0])
        
            outlier = list(set(possible069[i]) - set(possible069[j]))
            if len(outlier) == 1:
                if outlier[0] in guess_36:
                    set_segment(segments, guess_36, 3, 6, outlier[0])
                elif outlier[0] in guess_57:
                    set_segment(segments, guess_57, 5, 7, outlier[0])


    # Assign letters to decoder
    for i in range(10):
        if len(decoder[i]) == 0:
            for j in range(len(ground_truth[i])):
                decoder[i].append(segments[ground_truth[i][j]])

    # Sort final decoder values
    for i in range(10):
        decoder[i] = sorted(decoder[i])


    # Get final 4 digit output
    result = ''

    for value in output_values.split():
        sorted_value = sorted(value)
        
        for i in range(10):
            if decoder[i] == sorted_value:
                result += str(i)

    return int(result)


final_result = 0

with open('input.txt', 'r') as file:
    for data in file:
        final_result += decode_signals(data)

print(final_result)
