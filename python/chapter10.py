import pandas as pd

def GroupTotals(strArr):
    keys = []
    values = []
    for s in strArr:
        k, v = s.split(':')
        keys.append(k)
        values.append(int(v))

    data = {'key': keys, 'value': values}
    df = pd.DataFrame(data)

    sums = df.groupby('key')['value'].sum()

    result = ''
    for k in sorted(sums.keys()):
        if sums[k] > 0:
            result += k + ':' + str(sums[k]) + ','

    return result[:-1]
print(GroupTotals(["B:-1", "A:1", "B:3", "A:5", "C:0"]))