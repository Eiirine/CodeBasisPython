# Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. Для этого нужно идти от верхней границы к нижней.
# То есть счётчик должен быть инициализирован максимальным значением, а в теле цикла его нужно уменьшать до нижней границы.
def print_numbers(last_number):
    while last_number > 0:
        print(last_number)
        last_number = last_number - 1
    print('finished!')


# Реализуйте функцию multiply_numbers_from_range(), которая принимает два числа, границы диапазона, и перемножает числа в нем, включая границы диапазона.
def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1
    while i <= finish:
        multiply = multiply * i
        i = i + 1
    return multiply


# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из переданного диапазона в строку.
def join_numbers_from_range(start, finish):
    result = str(start)
    i = start + 1
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result

#Реализуйте функцию print_reversed_word_by_symbol(), которая печатает переданное слово посимвольно, как в примере из теории, но делает это в обратном порядке.
def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i = i - 1

#Функция из теории учитывает регистр букв. То есть A и a с её точки зрения разные символы. Реализуйте вариант этой же функции, так чтобы регистр букв был не важен
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].lower() == char.lower():
            count = count + 1
        index = index + 1
    return count

#Реализуйте функцию my_substr(), которая извлекает из переданной строки подстроку указанной длины. Она принимает на вход два аргумента:
#строку и длину, и возвращает подстроку, начиная с первого символа
def my_substr(string, number):
    i = 0
    substr = ''
    while i < number:
        substr = substr + string[i]
        i = i + 1
    return substr

#Реализуйте функцию-предикат is_arguments_for_substr_correct(), которая принимает три аргумента:
#строку;
#индекс, с которого начинать извлечение;
#длину извлекаемой подстроки.
#Функция возвращает False, если хотя бы одно из условий истинно:
#Отрицательная длина извлекаемой подстроки.
#Отрицательный заданный индекс.
#Заданный индекс выходит за границу всей строки.
#Длина подстроки в сумме с заданным индексом выходит за границу всей строки.
#В ином случае функция возвращает True.
def is_arguments_for_substr_correct(string, index, length):
    if index < 0:
        return False
    elif length < 0:
        return False
    elif index > len(string) - 1:
        return False
    elif index + length > len(string):
        return False
    return True

#Реализуйте функцию filter_string(), принимающую на вход строку и символ, и возвращающую новую строку, в которой удален переданный символ во всех его позициях.
#Старайтесь не использовать встроенные методы работы со строкой в своем решении.
def filter_string(text, character):
    index = 0
    filtered_text = ''
    while index < len(text):
        if text[index] != character:
            filtered_text += text[index]
            index += 1
        else:
            index += 1
    return filtered_text

#Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, содержит ли переданная строка указанную букву. Функция принимает два параметра:
#Строка
#Буква для поиска
def is_contains_char(word, character):
    index = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1
    return False

#В одном из предыдущих уроков мы уже написали функцию filter_string(). Напомним, она принимает на вход строку и символ и возвращает новую строку,
#в которой удалён переданный символ во всех его позициях. На этот раз реализуйте эту функцию с помощью цикла for.
#Дополнительное условие: регистр исключаемого символа не имеет значения.
def filter_string(text, character):
    filtered = ''
    for current_character in text:
        if current_character.lower() != character.lower():
            filtered += current_character
    return filtered

#Реализуйте функцию print_table_of_squares(from, to), которая печатает на экран квадраты чисел.
#Она первое from и последнее to число печатает строку square of <число> is <результат>
def print_table_of_squares(first, last):
    for i in range(first, last + 1):
        square = i * i
        print(f"square of {i} is {square}")