from typing import List
def sat305(e: List[int], edges=[[0, 217], [40, 11], [17, 29], [11, 12], [31, 51]]):
    return e in edges
def sol305(edges=[[0, 217], [40, 11], [17, 29], [11, 12], [31, 51]]):
    """Find any edge in edges."""
    return edges[0]
# assert sat305(sol305())
