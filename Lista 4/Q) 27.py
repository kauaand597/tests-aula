def distinct_numbers (my_list):
    distinct = []
    for num in my_list:
        if num not in distinct:
            distinct.append(num)
    return distinct[::-1]
