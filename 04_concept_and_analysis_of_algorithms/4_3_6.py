def is_perfect_possible(key: list[str], answers: list[str]) -> bool:
    """
    Determines whether it is possible for a perfect score or a completely
    incorrect score to be achieved given an answer key and a set of responses.

    Args:
        key (list[str]): The correct answer key. Each element is either a string
                         representing a valid answer or '*' which acts as a wildcard
                         that matches any response.
        answers (list[str]): A list of responses provided for the questions in the key.

    Returns:
        bool: True if either all responses match the key (perfect score) or all
              responses are incorrect (completely incorrect score). False otherwise.
    """
    g = b = 0
    for k, a in zip(key, answers):
        if k == '*':
            g += 1
            b += 1
        elif k != a:
            b += 1
        else:
            g += 1
    return g == len(key) or b == len(key)
