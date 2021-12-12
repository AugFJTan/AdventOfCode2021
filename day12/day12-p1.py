# A single small cave can be visited at most once
# How many paths through this cave system are there?


def traverse(node, paths, path_so_far, final_paths):
    if node.islower():
        if node in path_so_far:
            return
    
    path_so_far.append(node)

    if node == "end":
        final_paths.append(path_so_far)
        return

    for path in paths:
        if node in path:
            dest = path[0] if node == path[1] else path[1]
            if dest == "start":
                continue
            traverse(dest, paths, path_so_far[:], final_paths)


all_paths = []

with open('input.txt', 'r') as file:
    for line in file:
        n1, n2 = line.rstrip().split('-')
        all_paths.append((n1, n2))


final_paths = []

traverse("start", all_paths, [], final_paths)

print(len(final_paths))  # Answer: 3485
