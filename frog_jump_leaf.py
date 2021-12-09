def solution1(X, A):
    new_arr = [0] * X
    for i in range(len(A)):
        if A[i] < (X + 1):
            new_arr[A[i]-1] = 1
            print(new_arr)
            if 0 not in new_arr:
                return i
    return -1

def solution(jump_pos, leaves):
    """Solution method implementation."""
    # initialize the set of leaves we need for the frog
    leaves_positions = set(range(1, jump_pos + 1))
    # iterate through the array using both the element and its index
    for i, item in enumerate(leaves):

        # eliminate items from the set, one by one, if existing
        leaves_positions.discard(item)
        
        # check if our set has emptied or not
        if not leaves_positions:
            return i
    # if we made it to this point, frog can't cross the river
    return -1

    

if __name__== "__main__":
    X = 5
    A = [1,3,1,4,2,3,5,4]
    print(solution(X, A))
