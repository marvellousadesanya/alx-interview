#!/usr/bin/python3

"""Unlock all boxes"""
def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist represents
            a box and contains integers that represent the keys that are in
            that box.

    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    n = len(boxes)
    keys = {0}
    visited = set()
    while keys:
        box = keys.pop()
        visited.add(box)
        for key in boxes[box]:
            if key < n and key not in visited:
                keys.add(key)
    return len(visited) == n
