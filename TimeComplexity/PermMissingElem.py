# 100 %
def per_missing_element(A: list) -> int:
    """
    https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

    An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)],
    which means that exactly one element is missing.

    Your goal is to find that missing element.

    Write a function:

    class Solution { public int solution(int[] A); }

    that, given an array A, returns the value of the missing element.

    For example, given array A such that:

      A[0] = 2
      A[1] = 3
      A[2] = 1
      A[3] = 5
    the function should return 4, as it is the missing element.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
    """
    if not A:
        return 1
    min_a = min(A)
    max_a = max(A)

    if min_a != 1:
        return 1
    elif max_a != len(A) + 1:
        return len(A) + 1

    # https://www.cuemath.com/sum-of-integers-formula/
    expected_sum = int((len(A) + 1) * (min_a + max_a) / 2)  # sum of all numbers from 1 to (N + 1)
    real_sum = sum(A)
    return expected_sum - real_sum
