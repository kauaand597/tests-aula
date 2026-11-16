def even_numbers(my_list):
    evens = []
    for num in my_list:
        if num % 2 == 0:
            evens.append(num)
    return evens
'''
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("nova", new_list)
'''