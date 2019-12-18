start = 206938
end = 679128

def check(num):
    s = str(num)
    if s != "".join(sorted(s)):
        return False
    return any(str(i) * 2 in s and str(i) * 3 not in s for i in range(1, 10))

print(sum(check(num) for num in range(start, end+1)))
