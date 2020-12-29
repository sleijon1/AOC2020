cups = list(map(int, list("135468729")))
for more_cups in range(max(cups)+1, 1000001):
    cups.append(more_cups)


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None
    def __str__(self):
        return f"Val {self.data_val} Next {self.next_val.data_val}"
    def __repr__(self):
        return str(self)


nodes = {}
node_list = [Node(cup) for cup in cups]
for i, node in enumerate(node_list):
    nodes[node.data_val] = node
    if i+1 < len(node_list):
        node.next_val = node_list[i+1]
    else:
        # last, link to first
        node.next_val = node_list[0]

cup = node_list[0]
max_cup = 1000000
min_cup = 1
for _ in range(10000000):
    pick_up1 = cup.next_val
    pick_up2 = pick_up1.next_val
    pick_up3 = pick_up2.next_val
    curr_next = pick_up3.next_val
    pick_up = [0, pick_up1.data_val, pick_up2.data_val, pick_up3.data_val]
    dest = cup.data_val-1
    while dest in pick_up:
        dest = dest-1
        if dest < min_cup:
            dest = max_cup
    dest_node = nodes[dest]
    dest_node_next = dest_node.next_val
    # relink pick up nodes
    pick_up3.next_val = dest_node_next
    dest_node.next_val = pick_up1
    # relink current_node
    cup.next_val = curr_next
    cup = curr_next

part_2 = nodes[1].next_val.data_val*nodes[1].next_val.next_val.data_val
print(f"Solution part 2: {part_2}")
