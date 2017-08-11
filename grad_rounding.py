def solve(grades):
    results=[]
    for item in grades:
        if item>=38 and item%5>=3:
            results.append(item+(5-item%5))
        else:
            results.append(item)
    return results
