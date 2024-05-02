#!/usr/bin/python3
"""modules"""
from collections import deque


def canUnlockAll(boxes):
    """
    Checks if all boxes have keys.
    """

    all_boxes = len(boxes)
    explored = set()
    queue = deque([0])

    while queue and len(explored) != all_boxes:
        current_box = queue.popleft()
        if current_box not in explored:
            explored.add(current_box)
            for key in boxes[current_box]:
                if 0 <= key < all_boxes and key not in explored:
                    queue.append(key)

    return len(explored) == all_boxes
