def can_match_by_rotation(A: list[list[int]], B: list[list[int]]) -> bool:
    """
    Check if matrix A can be rotated to match matrix B.

    Args:
    A (list of list of int): Square matrix of integers.
    B (list of list of int): Square matrix of integers.

    Returns:
    bool: True if A can be rotated to match B, False otherwise.
    """

    def rotate_90_clockwise(matrix):
        """Rotate the matrix 90 degrees clockwise."""
        return [list(reversed(col)) for col in zip(*matrix)]

    # Check all four possible rotations
    for _ in range(4):
        if A == B:
            return True
        A = rotate_90_clockwise(A)

    return False


# Sample Inputs
A1 = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
B1 = [[0, 1, 0], [0, 1, 0], [1, 1, 1]]
print(can_match_by_rotation(A1, B1))  # True

A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(can_match_by_rotation(A2, B2))  # False

A3 = [[1]]
B3 = [[1]]
print(can_match_by_rotation(A3, B3))  # True

A4 = [[5, 2], [2, 3]]
B4 = [[5, 2], [2, 3]]
print(can_match_by_rotation(A4, B4))  # True

A5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
B5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(can_match_by_rotation(A5, B5))  # True

A6 = [[1, 0], [0, 1]]
B6 = [[1, 1], [1, 0]]
print(can_match_by_rotation(A6, B6))  # False
