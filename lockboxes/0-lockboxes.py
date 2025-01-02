#!/usr/bin/python3
'''This method determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''this method iterates over boxes
    which is a list of lists
    to see if the box in list
    contains the number
    of the indexes in boxes

    Args:
        boxes (list): list of lists

    Returns:
        bool: determines if it can open all boxes
    '''
    keys = [0]
    opened = set([0])

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
