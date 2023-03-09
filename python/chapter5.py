from collections import Counter
import pandas as pd

def appearxtimes(lst):
    x = lst[0]
    num_counts = Counter(lst[1:])
    filtered_counts = {num: count for num, count in num_counts.items() if count == x}
    if not filtered_counts:
        return -1
    else:
        min_num = min(filtered_counts.keys())
        return min_num
lst1 = [3, 1, 2, 3, 4, 5, 2, 2, 4]
lst2 = [2, 3, 3, 3, 4, 4]
lst3 = [2, 1, 2, 3, 4, 5]
lst4 = [4, 2, 2, 2, 2, 4, 4, 4]
lst5 = [3, 1, 2, 3, 4, 5, 6, 7, 8]

print(appearxtimes(lst1))  # 2
print(appearxtimes(lst2))  # 3
print(appearxtimes(lst3))  # -1
print(appearxtimes(lst4))  # 2
print(appearxtimes(lst5))  # -1
#####
