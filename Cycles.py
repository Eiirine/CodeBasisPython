#Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. Для этого нужно идти от верхней границы к нижней.
# То есть счётчик должен быть инициализирован максимальным значением, а в теле цикла его нужно уменьшать до нижней границы.
def print_numbers(last_number):
    while last_number > 0:
        print(last_number)
        last_number = last_number - 1
    print('finished!')

#Реализуйте функцию multiply_numbers_from_range(), которая принимает два числа, границы диапазона, и перемножает числа в нем, включая границы диапазона.
def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1
    while i <= finish:
        multiply = multiply * i
        i = i + 1
    return multiply

#Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из переданного диапазона в строку.
def join_numbers_from_range(start, finish):
    result = str(start)
    i = start + 1
    while i <= finish:
        result = result + str(i)
        i = i +1
    return result

#