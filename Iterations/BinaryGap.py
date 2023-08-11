def binary_gap(n: int) -> int:
    """
    BinaryGap is a problem that involves finding the longest sequence of zeros
    in a binary representation of an integer
    :param n: integer
    :return: max distance between ones
    """
    sequence: str = bin(n)[2:]
    # print(sequence)
    max_distance: int = 0
    temp_distance: int = 0
    s1: bool = False

    for i in sequence:
        if i == '1':
            s1 = True
            if temp_distance > max_distance:
                max_distance = temp_distance
            temp_distance = 0
        else:
            if s1:
                temp_distance += 1

    return max_distance
