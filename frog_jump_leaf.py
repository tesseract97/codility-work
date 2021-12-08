def solution(X, A):
    new_arr = [0] * X
    for i in range(len(A)):
        if A[i] < (X + 1):
            new_arr[A[i]-1] = 1
            print(new_arr)
            if 0 not in new_arr:
                return i
    return -1

    

if __name__== "__main__":
    X = 5
    A = [1,3,1,4,2,3,5,4]
    print(solution(X, A))
