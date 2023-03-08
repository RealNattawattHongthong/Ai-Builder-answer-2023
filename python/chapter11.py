def WordSplit(strArr):
    text = strArr[0]
    words = strArr[1].split(',')

    splits = [(text[:i], text[i:]) for i in range(1, len(text))]
    
    matches = [w1 + ',' + w2 for w1, w2 in splits if w1 in words and w2 in words]
    
    if matches:
        return matches[0] 
    else:
        return "not possible"
print(WordSplit(["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]))