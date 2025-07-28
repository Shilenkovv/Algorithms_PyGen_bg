from typing import List


def is_correct(html: str) -> bool:
    stack: List[str] = []
    i = 0

    while i != len(html):
        if html[i] == '<':
            i += 1
            cur_tag = '<'
            while cur_tag[-1] != '>':
                cur_tag += html[i]
                i += 1
            if '/' not in cur_tag:
                stack.append(cur_tag)
            else:
                if stack and stack[-1][1:-1] == cur_tag[2:-1]:
                    stack.pop()
                else:
                    return False
        else:
            i += 1
    return not stack


html = """<html>
             <head>
                <title>Привет, мир!</title>
             </head>"""
print(is_correct(html))
