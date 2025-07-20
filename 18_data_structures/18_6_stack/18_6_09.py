from typing import List


def simplify(path: str) -> str:
    stack: List[str] = []
    sym_set = set([',', ',', '_', '.'])

    i = 1
    while i < len(path):
        while i < len(path) and path[i] == '/':
            i += 1
        start = i
        while i < len(path) and (path[i] in sym_set or path[i].isalpha()):
            i += 1
        end = i
        if end - start == 2 and path[start:end] == '..':
            if stack:
                stack.pop()
        elif start != end and path[start:end] != '.':
            stack.append(path[start:end])
    return '/' + '/'.join(stack)


# print(simplify('/a/b/'))  # /a/b

# print(simplify('/a///b'))  # /a/b

# print(simplify('/a/b/c/../d'))  # /a/b/d

# print(simplify('/bee/'))  # /bee

# print(simplify('/../'))  # /

# print(simplify('/.../project_g//docs/../tmp/../data'))  # /.../project_g/data

# print(simplify('/.beegeek'))  # /.beegeek

# print(simplify('/.....beegeek'))  # /.....beegeek
