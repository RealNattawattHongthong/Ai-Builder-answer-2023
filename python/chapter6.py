def StringExpression(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
                'plus': '+', 'minus': '-'}
    for word, val in num_dict.items():
        s = s.replace(word, val)
    result = eval(s)
    if result < 0:
        return 'negative' + str(abs(result))
    else:
        return str(result)
result = StringExpression('oneplusone')
print(result)
####