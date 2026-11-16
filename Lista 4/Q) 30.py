def all_the_longest(my_list):
    if not my_list:
        return []

    longest_length = max(len(word) for word in my_list)
    return [word for word in my_list if len(word) == longest_length]