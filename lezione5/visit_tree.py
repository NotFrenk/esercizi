#petodo ricorsivo
"""
def visit_tree(tree:dict[int, list[int]], n: int):
    print(n)
    left_child,righy_child = tree[n]
    if left_child != None:
        visit_tree(tree, left_child)
    if righy_child != None:
        visit_tree(tree, righy_child)

tree={1:[2,3], 2:[4,5], 3:[None,None], 4:[None, None], 5:[None, None]}
visit_tree(tree, 1)
"""
#media per ciascun livello
def visiting_tree_iterative(tree:dict[int,list[int]], root:int):
    result={}
    node_numbers_per_level={}
    stack:list[int] = [root]
    while stack: #while len(stack) !=0
        curr_node, curr_level=stack.pop(0)
        resoult[curr_level] = resoult.get(curr_level,0) + curr_node
        node_numbers_per_level[curr_level] = node_numbers_per_level.get(curr_level,0) +1
        if curr_node:
            print(curr_node)
            left_child, right_child =tree[curr_node]
            if left_child:
                stack.append((left_child, curr_level +1))
            if right_child:
                stack.append((right_child, curr_level +1))
    
    for level in resoult:
        result[level] /=node_numbers_per_level[level]

    return result

tree={1:[2,3], 2:[4,5], 3:[None,None], 4:[None, None], 5:[None, None]}
visiting_tree_iterative(tree, 1)


