from anytree import Node, PreOrderIter, RenderTree, AsciiStyle

def get_data():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip().split()
            line = [int(l.strip()) for l in line]
            data.extend(line)
    return data

#17359 numbers
# print(get_data()[-0:])

def parse_to_tree():
    data = get_data()
    tree = get_node(data)
    return tree


def get_node(data, parent=None):
    if not data:
        return Node('node',parent=parent, meta=[])

    child_count = data.pop(0)
    metadata_len = data.pop(0)
    root = Node('node', parent=parent)
    if child_count:
        for i in range(child_count):
            get_node(data, parent=root)
    meta = []
    for i in range(metadata_len):
        meta.append(data.pop(0))
    root.meta = meta
    return root

def part_1():
    tree = parse_to_tree()
    sums = [sum(n.meta) for n in PreOrderIter(tree)]
    print(RenderTree(tree, style=AsciiStyle()))
    print(sums)
    print(sum(sums))

def part_2():
    tree = parse_to_tree()
    vals = []
    get_root_value(tree, vals)
    print(vals)
    print(sum(vals))

def get_root_value(root, vals):
    if not root.children:
        vals.append(sum(root.meta))

    for c in root.meta:
        if c == 0:
            continue
        try:
            get_root_value(root.children[c-1], vals)
        except IndexError:
            continue

part_2()