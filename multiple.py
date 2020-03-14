def is_multiple(n, m):
    '''
    Checks whether a given multipleCandidate is a multiple of the given number.
    Parameters:
        n - A number
        m - Another number which needs to be testified to see if the first param can be a multiple of this one.
    Returns:
        True - If n is a multiple of m, i.e, reminder of n/m is 0 
        False - If n is NOT a multiple of m, i.e, reminder of n/m is NOT 0 
    '''
    
    reminder = n % m
    return reminder == 0

def test():
    '''
    Tests is_multiple function.
    '''
    n = 27
    m = 3

    result = is_multiple(n, m) 

    if result:
        print(f"{n} is a multiple of {m}.")
    else:
        print(f"{n} is NOT a multiple of {m}.")
          
test()