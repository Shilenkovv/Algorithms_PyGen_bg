def prefix_search(strings: list[str], prefix: str):
    left, right = 0, len(strings) - 1
    while left <= right:
        middle = (left + right) // 2
        if strings[middle].startswith(prefix):
            while middle > 0 and strings[middle - 1].startswith(prefix):
                middle -= 1
            return strings[middle]
        if strings[middle][: len(prefix)] < prefix:
            left = middle + 1
        else:
            right = middle - 1
    return


# assert prefix_search(['bee'], 'bee') == 'bee'
# assert prefix_search(['01', '100', '12', '13'], '1') == '100'
