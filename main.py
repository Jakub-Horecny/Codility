# This is a sample Python script.
import math
import sys


def fibonacci(n: int) -> int:
    """
    fibonacci sequence
    :param n:
    :return: value of fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        seq1: int = 0
        seq2: int = 1
        for i in range(n - 2):
            temp = seq2
            seq2 = seq2 + seq1
            seq1 = temp
        return seq2 + seq1



def max_counters(A: list, N: int) -> list:
    """
    count number of unique integers in list, if integer > n - > all counters are set to the maximum value of any counter.
    :param A:
    :param N:
    :return:
    """
    counters: list = [0] * N
    max_value = 0
    for item in A:
        if item > N:
            counters = [max_value] * N
        else:
            counters[item - 1] = counters[item - 1] + 1
            max_value = max(counters[item - 1], max_value)

    return counters





# prefix sums
def passing_cars(a: list) -> int:
    east = 0
    passing_car = 0
    for i in a:
        if i == 0:
            east += 1
        else:
            passing_car += east

        if passing_car > 1_000_000_000:
            return -1
    return passing_car


# sorting
def MaxProductOfThree(A):
    a = sorted(A)
    return max(a[0] * a[1] * a[-1], a[-3] * a[-2] * a[-1])


# nájde počet všetkých dleitelov
def count_div(a: int, b: int, k: int) -> int:
    """
    For example, for A = 6, B = 11 and K = 2, your function should return 3,
    because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
    :rtype: object
    """
    # r: int = 0
    # for i in range(a, b):
    #     if i % k == 0:
    #         r += 1
    # return r
    f = ((a + k - 1) // k) * k  # first
    if f > b:
        return 0

    return ((b - f) // k) + 1


def Brackets(s: str):
    if len(s) % 2 == 1: return 0
    st = []  # stack
    pu = ['[', '{', '(']  # element to push on stack
    po = {']': '[', '}': '{', ')': '('}

    for e in s:
        if e in pu:
            st.append(e)  # push
        if e in po.keys():
            if (len(st) == 0):
                return 0
            if (st[-1] == po[e]):
                st.pop()
            else:
                return 0

    if len(st) == 0:
        return 1
    else:
        return 0


def ChocolatesByNumbers(n: int, m: int):
    temp = 0
    i = 0
    while True:
        i += 1
        temp = temp + m
        if temp == n:
            return i


def MinAbsSum(A):
    N = len(A)

    # Initialize variables to keep track of current and total sums
    current_sum = 0
    total_sum = sum(A)

    # Initialize the minimum absolute difference to the total sum
    min_abs_diff = total_sum

    for num in A[:-1]:
        current_sum += num
        abs_diff = abs(total_sum - 2 * current_sum)
        min_abs_diff = min(min_abs_diff, abs_diff)

    # Handle the case where the last number is multiplied by -1
    abs_diff = abs(total_sum - 2 * current_sum - A[-1])
    min_abs_diff = min(min_abs_diff, abs_diff)

    return min_abs_diff


# stacks nad Queues
def nesting(s: str) -> int:
    if len(s) == 0:
        return 1
    stack = []
    for letter in s:
        if letter == ')' and not stack:
            return 0
        if letter == '(':
            stack.append(letter)
        else:
            stack.pop()

    if not stack:
        return 1
    else:
        return 0


def max_slice_sum(a: list) -> int:
    a.sort()
    return max(a[0] * a[1], a[-1] * a[-2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(cyclic_rotation([5, -1000], 1))
    # print(odd_occurrences_in_array([3,3,6,6,6,6,9]))
    # print(per_missing_element([12, 11, 10, 1, 2, 3, 5, 6, 7, 8, 9, 4, 14]))
    # print(frog_jmp(5, 85, 10))
    # print(tape_equilibrium([3, 1, 2, 4, 3, 13, 20]))
    # print(frog_river_one([1, 3, 1, 4, 2, 3, 5, 4], 5))
    # print(max_counters([3, 4, 4, 6, 1, 4, 4, 5, 6], 5))

    #print(missing_integer([-5, 0, 1, 3, 6, 4, 1, 2]))
    # print(missing_integer([2]))
    # print(perm_check([1,2]))
    # print(passing_cars([0, 1, 0, 1, 1]))
    # print(count_div(6, 8, 2))
    # print(MaxProductOfThree([4, 7, 3, 2, 1, -3, -5]))
    # print(Brackets('{[()()]}'))
    # print(Brackets('([)()]'))
    # print(Brackets('))(('))
    # print(MinAbsSum([1, 5, 2, -2]))
    # print(nesting('(()()()(()(((()())'))
    print(max_counters([3, 4, 4, 6, 1, 4, 4, 5, 6], 5))
