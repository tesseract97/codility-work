def solution(A):
    # sum up the tape
    n = len(A)

    partA = 0
    partB = sum(A)

    last_diff = 0
    current_diff = 0
    for i in range(n):

        partA = partA + A[i]
        partB = partB - A[i]

        if i == 0:
            current_diff = abs(partA - partB)
        else:
            current_diff = abs(partA - partB)
            if current_diff > last_diff:
                return last_diff
        last_diff = current_diff

if __name__== "__main__":
    A = [3,10,19,15,2]
    print(solution(A))


    