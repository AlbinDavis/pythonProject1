
def repeatedString(s, n):
    if 'a' not in s:
        return 0
    else:
        d = n // len(s)
        r = n % len(s)
        c = s.count("a")
        if r == 0:
            return d * c
        else:
            return d * c + s[:r].count('a')
s = input()

n = int(input())

result = repeatedString(s, n)
