def solution(A):
    n = len(A)
    perfect_set = set(range(1, n+1))

    for i, item in enumerate(A):
        perfect_set.discard(item)

        if not perfect_set:
            if i == n-1:
                return 1
            else:
                return 0
    return 0
    


if __name__== "__main__":
    A = [1,2,1]
    print(solution(A))
