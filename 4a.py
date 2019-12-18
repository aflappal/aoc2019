start = 206938
end = 679128

def check(num):
    s = str(num)
    if s != "".join(sorted(s)):
        return False
    return len(str(s)) > len(set(str(s)))

print(sum(check(num) for num in range(start, end+1)))
