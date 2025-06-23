def draw_graph(function):
    print('y ^')

    for y in range(9, 0, -1):
        for x in range(1, 10):
            if x == 1:
                print(y, '|', end='')
            if function(x) == y:
                print('  *', end='')
            else:
                print('   ', end='')
        print()

    print('  +--------------------------- > x')
    print('     1  2  3  4  5  6  7  8  9')
