# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    #sorting array
    n = len(A)
    A.sort()
    for i in range(n):
        if (i < n-1):
            if A[i +1] - A[i] > 1:
                return A[i] + 1
        else:
            return A[i] + 1




if __name__== "__main__":
    A = [2,3,4,1,5]
    print(solution(A))
