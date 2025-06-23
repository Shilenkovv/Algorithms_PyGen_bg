def count_animals(heads: int, legs: int) -> tuple:
    """
    Determines the count of ducks and rabbits based on the total number of heads
    and legs, assuming ducks have 2 legs and rabbits have 4 legs.

    Args:
        heads (int): The total number of heads (sum of ducks and rabbits), where 0 <= heads <= 10^3.
        legs (int): The total number of legs (sum of legs of ducks and rabbits), where 0 <= legs <= 10^3.

    Returns:
        tuple: A tuple `(ducks, rabbits)` representing the count of ducks and rabbits
               if a valid solution exists. If no valid solution is possible, returns `None`.
    """
    ducks = 2 * heads - legs / 2
    rabbits = heads - ducks
    if any([not ducks.is_integer(), not rabbits.is_integer(), rabbits < 0, ducks < 0]):
        return None
    return (int(ducks), int(rabbits))
