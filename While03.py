def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    z=0
    while a< len(s):
        if not s[a].isalpha() and not s[a].isdigit():
            z+=1
        a+=1
    return z
print(main("#hashtag@$"))