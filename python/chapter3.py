def findmidprefix(s):
    prefixes = [s[:i] for i in range(1, len(s)+1)]
    n = len(prefixes)
    mid_prefix_index = n // 2
    return prefixes[mid_prefix_index]

s = "Hello World!"
result = findmidprefix(s)
print(result)