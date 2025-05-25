def shortest_distance(x: int, y: int, z: int) -> int:
    dist = sorted([x, y, z])
    return min(x + y + z, 2 * (dist[0] + dist[1]))
