# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    bin_num = bin(N)
    bin_str = str(bin_num)[2:]
    print("binary number: ", bin_str)
    binary_gap = 0
    binary_gap_tester = 0

    start = False
    for digit in bin_str:
        if digit == '1':
            if start == True:
                if binary_gap < binary_gap_tester:
                    binary_gap = binary_gap_tester
                binary_gap_tester = 0
            else:
                start = True

        if digit == '0':
            if start == True:
                binary_gap_tester +=1
    return binary_gap







if __name__== "__main__":
    print(solution(1610612737))
