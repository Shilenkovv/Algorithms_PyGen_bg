from typing import List, Tuple


def journey_ends(flights: List[Tuple[str, str]]) -> Tuple[str, str]:
    set_from: set[str] = set()
    set_to: set[str] = set()

    for dep, arr in flights:
        set_from.add(dep)
        set_to.add(arr)

    return ((set_from - set_to).pop(), (set_to - set_from).pop())


flights = [('Vladikavkaz', 'Istanbul'), ('Moscow', 'Vladikavkaz'), ('Kazan', 'Moscow')]
print(journey_ends(flights))
