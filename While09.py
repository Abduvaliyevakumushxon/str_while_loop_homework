def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    d=0
    count=0
    while d < len(s):
        if s[d].isdigit():
            count +=int(s[d])
        d+=1
    return count
print(main("987654"))