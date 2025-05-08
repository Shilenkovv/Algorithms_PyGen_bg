def is_function(pairs: list) -> bool:
    """Проверяет выражают ли пары чисел функциональную зависимость.

    Args:
        pairs (list): Список различных кортежей, каждый из которых состоит из двух целых чисел.

    Returns:
        bool
    """

    pairs_new = list(map(lambda x: x[0], pairs))
    return len(set(pairs_new)) == len(pairs_new)
