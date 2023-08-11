import math
import Iterations.BinaryGap


def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if N <= len(alphabet):
        return alphabet[:N]
    if N % len(alphabet) == 0:
        return alphabet * int(N / len(alphabet))
    else:
        d = divisor(N)
        if len(d) == 2:
            return alphabet[0] * N
        else:
            for i in reversed(d):
                if i < len(alphabet):
                    div = int(N / i)
                    return alphabet[:i] * div


def divisor(n):
    small_divisors: list = []
    large_divisors: list = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            small_divisors.append(i)
            if i * i != n:
                large_divisors.append(int(n / i))
    large_divisors.reverse()
    return small_divisors + large_divisors


def domino(n):
    if len(n) == 2:
        return 0

    index = 1
    inc = 1
    found: bool = False
    while True:
        while True:
            if index + inc >= len(n) - 1:
                break

            if n[index] == n[index + inc]:
                # print(n[:index+1])
                # print(n[index+inc:])
                found = True
                n = n[:index + 1] + n[index + inc:]
            else:
                inc += 2
        if index + 2 >= len(n) - 1:
            break
        if not found:
            n = n[:index + 1]
            break
        else:
            found = False
            index += 2

    print(n)
    return int(len(n) / 2)


def dominos(input_dom):
    # flip pieces
    preprocessed_dom = []
    for i in input_dom:
        if i[0] > i[1]:
            preprocessed_dom.append([i[1], i[0]])
        else:
            preprocessed_dom.append(i)

    # sort pieces
    preprocessed_dom.sort(key=lambda x: x[0])

    # find lengths of chained dominos and take max length
    dom_prev = preprocessed_dom[0]
    output = 1
    max_output = 1
    for dom in preprocessed_dom[1:]:
        if dom_prev[1] == dom[0]:
            output += 1
        elif dom_prev[1] != dom[0] and output > max_output:
            max_output = output
            output = 1
        if output > max_output:
            max_output = output
        dom_prev = dom

    return max_output


def MinPerimeterRectangle(n):
    divisors = divisor(n)
    if len(divisors) == 1:
        return 4
    min_perimeter = math.inf
    while True:
        for i in divisors:
            if divisors[0] * i == n:
                print("uotruoitrut")
                if 2 * (divisors[0] + i) < min_perimeter:
                    min_perimeter = 2 * (divisors[0] + i)
        divisors.pop(0)
        if len(divisors) == 1:
            break

    return min_perimeter


def MinPerimeterRectangle2(n):
    i = 1
    d = 0
    f = []
    while i * i < n:
        if n % i == 0:
            f.append(i)
            f.append(n // i)
        i += 1
    if i * i == n:
        f.append(i)
        return 2 * (i + i)
    else:
        return 2 * (f[-1] + f[-2])


if __name__ == '__main__':
    # print(solution(5))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
    # print(solution(3))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
    # print(solution(52))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
    # print(find_divisors(50))
    # print((solution(30)))
    # print(list(range(0, 10, 2)))
    # print([i * 2 for i in range(5)])
    # print(list(reversed(range(8, -1, -2))))
    # print([i for i in range(10) if i % 2])
    #

    # print(domino([2, 4, 1, 3, 4, 6, 2, 4, 1, 6]))
    # print(domino([5, 1, 2, 6, 6, 1, 3, 1, 4, 3, 4, 3, 4, 6, 1, 2, 4, 1, 6, 2]))
    # print(dominos([[1,2],[4,5],[9,6],[2,3],[5,8]]))

    # print(divisor(24))
    print(MinPerimeterRectangle(36))
    print(Iterations.BinaryGap.binary_gap(55))
