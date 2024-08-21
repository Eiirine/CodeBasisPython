#Реализуйте функцию с именем print_motto(), которая выведет на экран фразу Winter is coming.
def print_motto():
    print('Winter is coming')

#Реализуйте функцию say_hurray_three_times(), которая возвращает строку 'hurray! hurray! hurray!'.
# BEGIN (write your solution here)
def say_hurray_three_times():
    return 'hurray! hurray! hurray!'

hurray = say_hurray_three_times()
print(hurray)
# END

#Допишите функцию truncate(), которая обрезает переданную строку до указанного количества символов,
#добавляет в конце многоточие и возвращает получившуюся строку.
def truncate(text, length):
    # BEGIN (write your solution here)
    return text[0:length] + '...'
    # END

#Реализуйте функцию get_hidden_card(), который принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки и
#возвращает его скрытую версию, которая может использоваться на сайте для отображения.
# Если исходная карта имела номер 2034399002125581, то скрытая версия выглядит так ****5581.
# Другими словами, функция заменяет первые 12 символов, на звездочки. Количество звездочек регулируется вторым,
#необязательным, параметром. Значение по умолчанию — 4.
def get_hidden_card(card, index=4):
    length = len(card)
    return f'{('*' * index) + str(card[length - 4:length])}'

#Реализуйте функцию trim_and_repeat(), которая принимает три параметра: строку, offset — число символов, на которое нужно
#обрезать строку слева и repetitions — количество обрезанных строк, которые нужно вывести. Функция обрезает строку и повторяет ее
#столько раз, чтобы общее количество обрезанных строк равнялось repetitions. Функция должна записать результат в одну строку
#и вернуть его. Число символов для среза по умолчанию равно 0, а повторений — 1.
def trim_and_repeat(text, offset=0, repetitions=1):
    return f'{text[offset:] * repetitions}'

#Реализуйте функцию word_multiply(). Она должна принимать два параметра:
#Строку
#Число, которое обозначает, сколько раз нужно повторить строку

def word_multiply(text: str, repetitions: int) -> str:
    return text * repetitions
