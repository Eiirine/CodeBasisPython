#Напишите функцию is_pensioner(), которая принимает возраст в качестве единственного аргумента и проверяет, является ли этот возраст пенсионным.
#Пенсионным считается возраст 60 лет и больше.
def is_pensioner(age):
    return age >= 60

#Напишите функцию is_mister(), которая принимает строку и проверяет, является ли она словом 'Mister'.
def is_mister(title):
    return title == 'Mister'

#Реализуйте функцию is_international_phone(), которая принимает на вход строку - номер телефона и проверяет его формат.
#Если телефон начинается с +, значит это международный формат.
def is_international_phone(number):
    first_symbol = number[0]
    return first_symbol == '+'

#Реализуйте функцию is_leap_year(), которая принимает год в форме числа и определяет является ли он високосным или нет.
#Год будет високосным, если он кратен (то есть делится без остатка) 400 или он одновременно кратен 4 и не кратен 100.
def is_leap_year(year):
    return (year % 400 == 0 or year % 4 == 0 and year % 100 != 0)

#В этом уроке вам нужно будет реализовать две функции is_palindrome() и is_not_palindrome(), принимающие строку на вход
def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]

def is_not_palindrome(word):
    return not is_palindrome(word)

#Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается 'yes' иначе 'no'
def string_or_not(text):
    return isinstance(text, str) and 'yes' or 'no'