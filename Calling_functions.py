#В коде программы определены две переменные, содержащие имена компаний. Посчитайте их общую длину в символах и выведите ее на экран.
company1 = 'Apple'
company2 = 'Samsung'

# BEGIN (write your solution here)
length1 = len(company1)
length2 = len(company2)
print(length1 + length2)
# END

#Напишите программу, которая выведет на экран результат работы функции hex() с переменной number в качестве параметра.
number = 255
# BEGIN (write your solution here)
hex_number = hex(255)
print(hex_number)
# END

#Округлите число, записанное в переменную number, до двух знаков после запятой и выведите результат на экран.
number = 10.1234
# BEGIN (write your solution here)
result = round(number, 2)
print(result)
# END

#Выведите на экран первую и последнюю буквы предложения, записанного в переменную text, в следующем формате:
#First: N
#Last: t
text = 'Never forget what you are, for surely the world will not'
# BEGIN (write your solution here)
print(f'First: {text[0]}')
print(f'Last: {text[len(text) - 1]}')
# END

#Посчитайте программно (а не в голове) минимальное число среди 3, 10, 22, -3, 0 — и выведите его на экран.
#Воспользуйтесь функцией min(), которая работает аналогично max().
# BEGIN (write your solution here)
print(min(3, 10, 22, -3, 0))
# END

#Так как функция random() возвращает числа в диапазоне от 0 до 1, то чтобы получить числа от 0 до 10,
#нам нужно выполнить умножение на 10. Затем получившиеся число округляется и так мы получаем то, что нужно.
# imports are studied on Hexlet
from random import random
# BEGIN (write your solution here)
print(round(random() * 10))
# END

#Выведите на экран тип значения переменной motto.
motto = 'Family, Duty, Honor'
# BEGIN (write your solution here)
print(type(motto))
# END
