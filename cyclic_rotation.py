# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    n = len(A)
    new_arr = [0] * n

    for i in range(n):
        if i < (n - K):
            new_arr[i+K] = A[i]
        else:
            if (n > K):
                new_arr[i-(n-K)] = A[i]
            else:
                new_arr[i-(K-n)] = A[i]

    
    return new_arr
        


if __name__== "__main__":
    A = [1,2,3,4,5]
    K = 6
    print(solution(A, K))
