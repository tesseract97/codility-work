import math

def solution(X, Y, D):
    N = Y - X
    return math.ceil(N/D)

if __name__== "__main__":
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))
