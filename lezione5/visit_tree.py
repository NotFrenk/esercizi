#petodo ricorsivo

def visit_tree(tree:dict[int, list[int]], n: int):
    print(n)
    left_child,righy_child = tree[n]
    if left_child != None:
        visit_tree(tree, left_child)
    if righy_child != None:
        visit_tree(tree, righy_child)

tree={1:[2,3], 2:[4,5], 3:[None,None], 4:[None, None], 5:[None, None]}
visit_tree(tree, 1)

#metodo .pop
def visiting_tree_iterative(tree:dict[int,list[int]], root:int):
    stack:list[int] = [root]
    while stack: #while len(stack) !=0
        curr_node=stack.pop()

        if curr_node:
            print(curr_node)
            left_child, right_child =tree[curr_node]

            if right_child:
                stack.append(right_child)
            if left_child:
                stack.append(left_child)