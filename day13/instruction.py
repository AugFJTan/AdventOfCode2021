def fold(paper, axis, value):
    result = []
    width = len(paper[0])
    height = len(paper)

    if axis == 'x':
        folded_width = value

        for i in range(height):
            left_half = paper[i][:folded_width]
            right_half = paper[i][folded_width+1:]
            right_half.reverse()

            for j in range(folded_width):
                if left_half[j] == 0:
                    left_half[j] = right_half[j]

            result.append(left_half)

    else:  # axis == 'y'
        folded_height = value

        for i in range(folded_height):
            top_half = paper[i]
            bottom_half = paper[height-1-i]

            for j in range(width):
                if top_half[j] == 0:
                    top_half[j] = bottom_half[j]

            result.append(top_half)

    return result
