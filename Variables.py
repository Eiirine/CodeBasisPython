#Создайте переменную с именем motto и содержимым What Is Dead May Never Die!. Распечатайте содержимое переменной.
motto = 'What Is Dead May Never Die!'
print(motto)

#В упражнении определена переменная, внутри которой содержится строка.
#Переопределите значение этой переменной и присвойте ей строку, в которой расположите символы первоначальной строки в обратном порядке.
name = 'Brienna'
# BEGIN (write your solution here)
name = 'anneirB'
# END
print(name)

#Создайте переменную, описывающую количество своих братьев, и присвойте ей значение 2.
my_brothers_count = 2
print(my_brothers_count)

#Найдите в программе необъявленную переменную и объявите ее, присвоив ей значение 'Dragon'. После выполнения программы результат на экране должен выглядеть так:
#Targaryen
# and
#Dragon
family = 'Targaryen'
# BEGIN (write your solution here)
pet = 'Dragon'
# END
print(family)
print(' and ')
print(pet)

#Напишите программу, которая берет исходное количество евро, записанное в переменную euros_count, переводит евро в доллары и выводит на экран.
#Затем полученное значение переводит в юани и выводит на новой строчке.
euros_count = 100
# BEGIN (write your solution here)
yuans_per_dollar = 6.91
dollars_count = euros_count * 1.25
yuans_count = dollars_count * yuans_per_dollar
print(dollars_count)
print(yuans_count)
# END

#Напишите программу, которая будет генерировать заголовок и тело письма, используя уже готовые переменные, и выводить получившиеся строки на экран.
#Для заголовка используйте переменные first_name и greeting, запятую и восклицательный знак. Выведите это на экран в правильном порядке.
#Для тела письма используйте переменные info и intro, при этом второе предложение должно быть на новой строке.
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."
first_name = 'Joffrey'
greeting = 'Hello'
# BEGIN (write your solution here)
print(greeting + ', ' + first_name + '!')
print(intro + '\n' + info)
# END

#Создайте две переменные с именами «первое число» и «второе число» на английском языке используя snake_case.
#Запишите в первую переменную число 20, во вторую — -100. Выведите на экран произведение чисел, записанных в получившиеся переменные.
first_number = 20
second_number = -100
print(first_number * second_number)

#Избавьтесь от магических чисел, создав новые переменные, а затем выведите текст на экран.
king = "Rooms in King Balon's Castles:"
# BEGIN (write your solution here)
castle_room_count = 102
print(king); print(castle_room_count)
# END

#Создайте константу DRAGONS_BORN_COUNT и запишите в неё число 3 — это количество драконов, родившихся у Дайенерис.
DRAGONS_BORN_COUNT = 3