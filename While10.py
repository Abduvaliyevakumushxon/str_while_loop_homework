def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    d=0
    count=0
    while d<len(s):
        if s[d].isdigit() and int(s[d])%2==1:
            count+=int(s[d])
        d+=1
    return count
print(main("589765"))