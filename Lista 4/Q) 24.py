"era so a definicao da funcao, nao precisa de input, ele serviu s p/ara testar a funcao"


def sum_of_positives(my_list):
    total = 0
    for num in my_list:
        if num > 0:
            total += num
    return total

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("O resultado é", result)