def shortest(my_list):
    shortest_string = my_list[0]
    for string in my_list:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string