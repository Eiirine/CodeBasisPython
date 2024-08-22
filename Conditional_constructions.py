#Реализуйте функцию guess_number(), которая принимает число и проверяет, равно ли число заданному (пусть это будет 42).
#Если равно, то функция должна вернуть строку 'You win!', в противном случае нужно вернуть строку 'Try again!'.
def guess_number(guess):
    if guess == 42:
        return 'You win!'
    return 'Try again!'

#Реализуйте функцию normalize_url(), которая выполняет нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.
def normalize_url(url):
    if url[:8] == 'https://':
        return url
    elif url[:7] == 'http://':
        return 'https://' + url[7:]
    else:
        return 'https://' + url

#На электронной карте Вестероса, которую реализовал Сэм, союзники Старков отображены зелёным кружком, враги — красным, а нейтральные семьи — серым.
#Напишите для Сэма функцию who_is_this_house_to_starks(), которая принимает на вход фамилию семьи и возвращает одно из трёх значений: 'friend', 'enemy', 'neutral'.
def who_is_this_house_to_starks(family):
    if family == 'Karstark' or family == 'Tully':
        return 'friend'
    elif family == 'Lannister' or family == 'Frey':
        return 'enemy'
    else:
         return 'neutral'

#Реализуйте функцию flip_flop(), которая принимает на вход строку и, если эта строка равна 'flip', возвращает строку 'flop'. В противном случае функция должна вернуть 'flip'.
def flip_flop(text):
    return 'flip' if text == 'flop' else 'flop'

# Реализуйте функцию get_number_explanation(), которая принимает на вход число и возвращает объяснение этого числа.
#Если для числа нет объяснения, то возвращается just a number. Объяснения есть только для следующих чисел:
# 666 - devil number
# 42 - answer for everything
# 7 - prime number

def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'