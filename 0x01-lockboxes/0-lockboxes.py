def canUnlockAll(boxes):
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

