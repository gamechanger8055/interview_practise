def next_palindrome_optimized(n):
    s=str(n)
    length=len(s)
    first_half=s[:(length+1)//2]
    next_half=str(int(first_half)+1)
    possiblity1=int(first_half+first_half[::-1][length%2:])
    possiblity2=int(next_half+next_half[::-1][length%2:])
    if possiblity1>n:
        return possiblity1
    return possiblity2


# Example usage
n = 94187978322
n1=3221
result = next_palindrome_optimized(n)
print(f"The smallest palindrome greater than {n1} is {result}")

#def smallestNumberPalindromeGreaterThanN(n):
