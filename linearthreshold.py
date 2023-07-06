# the mapping stores incoming connections. nodeA => nodes that have a directed path to nodeA originating from them
graph = {
    1: [],
    2: [],
    3: [(5, 0.6)],
    4: [(1, 0.7), (2, 0.2)],
    5: [(2, 0.5), (4, 0.5)],
    6: [(3, 0.5), (5, 0.2)],
    7: [(4, 0.3), (8, 0.3)],
    8: [(5, 0.3), (6, 0.7)],
    9: [(7, 0.6)],
    10: [(4, 0.4), (5, 0.2)],
    11: [(10, 0.6)],
    12: [(6, 0.3), (8, 0.1), (11, 0.2)]
}

active = [1, 8, 2]

for k, v in graph.items():
    # print(k, "-->", v)
    for i, j in v:
        print(k, "-->", i, j)
        
# go through each node
# check which nodes becomes active, add it to the list
# if no new nodes become active, break
# use the old state value when checking state for a neighbor and do it in the next iteration

def find_cascade(graph, active, threshold):
    new_active = [n for n in active]
    
    for node, neighbors in graph.items():
        if node in active:
            continue
        
        cumulative_input = 0
        for neighbor, weight in neighbors:
            state = 0
            if neighbor in active:
                state = 1
            val = state * weight
            cumulative_input += val

        if cumulative_input >= threshold:
            new_active.append(node)
    
    if len(new_active) > len(active):
        return find_cascade(graph, new_active, threshold)

    return new_active

# Example
print(find_cascade(graph, active, 0.6))
        
