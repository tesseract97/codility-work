def solution(A):
    n = len(A)

    for i in range(n):
        match = False
        for j in range(n):
            if i != j:
                if A[i] == A[j]:
                    break
                else:
                    if j == n-1:
                        return A[i]
            continue
            
        



if __name__== "__main__":
    A = [2,3,4,5,6,2,3,4,5]
    print(solution(A))
