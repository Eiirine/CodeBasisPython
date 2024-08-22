#Приведите строку text к нижнему регистру и напечатайте её на экран. Пример метода, выполняющего эту задачу приведен в теории.
text = 'a MIND needs Books as a Sword needS a WHETSTONE.'
# BEGIN (write your solution here)
print(text.lower())
# END

#Обновите переменную first_name, записав в неё то же самое значение, но обработанное методом .strip().
#Распечатайте то, что получилось, на экран.
first_name = '  Grigor   \n'
# BEGIN (write your solution here)
print(first_name.strip())
# END

#Найдите символы N и, (запятая) внутри текста в переменной text. Выведите на экран их индексы.
text = 'Never forget what you are, for surely the world will not'
# BEGIN (write your solution here)
print('Index Of N: ' + str(text.find('N')) + '\n' + 'Index Of ,: ' + str(text.find(',')))
# END

#С помощью среза строк получите часть предложения, записанного в переменную text, c 5 по 15 символы включительно.
#Полученную подстроку обработайте методом .strip() и выведите на экран длину итоговой подстроки.
#Выполните эти операции подряд в цепочке без создания промежуточных переменных.
text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# BEGIN (write your solution here)
print(str(len(text[4:15].strip())))
# END