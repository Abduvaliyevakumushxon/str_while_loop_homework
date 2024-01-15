def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    d=0
    count=0
    while d<len(s):
        if s[d].isdigit() and int(s[d])%2==0:
            count +=1
        d+=1
    return count
print(main("56786543250"))