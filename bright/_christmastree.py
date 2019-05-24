def printtree(tree_h=20):
    m,n = tree_h
    if m >= 1:
        f(m - 1, n)
        print (n - m + 1) * (' ') + (2 * m - 1) * ('*')
    for i in range(tree_h):
        print((' ' * tree_h) + '*')
