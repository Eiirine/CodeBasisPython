#Выведите на экран строку Do you want to eat, <name>?. Где вместо <name> должна использоваться переменная stark.
#Вывод должен получиться таким: Do you want to eat, Arya?
stark = 'Arya'

# BEGIN (write your solution here)
question = f'Do you want to eat, {stark}?'
print(question)
# END

#Выведите на экран последний символ строки, находящейся в переменной name
name = 'Na\nharis'

# BEGIN (write your solution here)
print(name[-1])
# END

#В переменной value лежит значение Hexlet. Извлеките из него и выведите на экран срез, который получит подстроку xle. Это задание можно сделать разными способами.
value = 'Hexlet'

# BEGIN (write your solution here)
print(value[2:5])
# END

#Запишите в переменную text текст, который приведен ниже. Используйте тройные кавычки.
#Lannister, Targaryen, Baratheon, Stark, Tyrell...
#they're all just spokes on a wheel.
#This one's on top, then that one's on top, and on and on it spins,
#crushing those on the ground.
# BEGIN (write your solution here)
text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
they\'re all just spokes on a wheel.
This one\'s on top, then that one\'s on top, and on and on it spins,
crushing those on the ground.'''
# END
print(text)