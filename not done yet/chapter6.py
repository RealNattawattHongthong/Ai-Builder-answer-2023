def StringExpression(expression: str) -> str:
    # Replace the words "plus" and "minus" with the symbols "+" and "-"
    expression = expression.replace("plus", "+").replace("minus", "-")
    # Initialize the running total to zero
    total = 0
    # Initialize a list to hold the terms of the expression
    terms = []
    # Iterate over the characters of the input string
    for char in expression:
        # If the character is a digit, add it to the current term
        if char.isdigit():
            terms[-1] += char
        # If the character is a plus or minus symbol, start a new term
        else:
            terms.append(char)
    # Evaluate the expression by summing the terms
    for term in terms:
        if term == "+":
            total += int(terms[terms.index(term) + 1])
        elif term == "-":
            total -= int(terms[terms.index(term) + 1])
        else:
            total += int(term)
    # If the result is negative, add the word "negative" before the digits
    result = str(total)
    if result.startswith("-"):
        result = "negative" + result[1:]
    # Replace the digits with their word counterparts
    result = result.replace("0", "zero").replace("1", "one").replace("2", "two").replace("3", "three") \
             .replace("4", "four").replace("5", "five").replace("6", "six").replace("7", "seven") \
             .replace("8", "eight").replace("9", "nine")
    return result
print(StringExpression("foursixminustwotwoplusonezero"))