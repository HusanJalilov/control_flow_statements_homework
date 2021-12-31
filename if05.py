def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a<0 and b<0 and c<0:
        return 3
    if a<0 and b<0:
        return 2
    if a<0 and c<0:
        return 2
    if b<0 and c<0:
        return 2
    if a<0:
        return 1
    if b<0:
        return 1
    if c<0:
        return 1