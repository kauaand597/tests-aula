def factorials(n: int):
    result = {}
    for i in range(n + 1):
        if i == 0 or i == 1:
            result[i] = 1
        else:
            result[i] = result[i - 1] * i
    return result