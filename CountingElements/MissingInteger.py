def missing_integer(A: list) -> int:
    if len(A) == 1:
        return 1

    A = sorted(set(A))
    if A[len(A) - 1] < 1:
        return 1
    else:
        temp = A[0]
        for i in A[1:]:
            if i > 1:
                if temp + 1 != i:
                    return temp + 1
            temp = i
        return A[len(A) - 1] + 1