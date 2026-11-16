def longest_series_of_neighbours(my_list):
    if not my_list:
        return 0

    longest = 1
    current_series = 1
    for previous, current in zip(my_list, my_list[1:]):
        if abs(current - previous) == 1:
            current_series += 1
            longest = max(longest, current_series)
        else:
            current_series = 1
    return longest