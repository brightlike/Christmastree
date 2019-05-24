def printtree(tree_h=20, leaves=1):
    for i in range(tree_h):
        print((' ' * (tree_h - i)) + ('*' * leaves))
        leaves += 2
    for j in range(tree_h):
        print ((' ' * tree_h) + '*')
