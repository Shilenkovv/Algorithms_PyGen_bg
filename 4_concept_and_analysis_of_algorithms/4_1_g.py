def snake(n: int) -> None:
    """Print a snake pattern of stars.

    Args:
        n (int): Amount of rows and columns in the snake pattern, where 1 <= n <= 100.
    """
    rows = 0
    crawling_right = True
    while rows < n:
        if (rows + 1) % 2 != 0:
            print('*' * n)
        else:
            if crawling_right:
                print(' ' * (n - 1) + '*')
            else:
                print('*' + ' ' * (n - 1))
            crawling_right = not crawling_right
        rows += 1


snake(5)
