import time
user_login = input('Ваш логин: ')
time.sleep(1)
print('Добро пожаловать в New word,', user_login, '!')
time.sleep(1)
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "ЩИЩ": "Одобрение или восторг",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться"
            }
while True:  
    print("Современные популярные слова: ", meme_dict.keys())
    time.sleep(1)
    word = input("Введите непонятное слово (большими буквами!): ")
    time.sleep(1)
    value = meme_dict[word]
    if word in meme_dict.keys():
        print("Значение слова: ", value)
    else:
        print("Слово не нашлось!")
    time.sleep(1)    
    q1 = input('Хотите продолжить работу программы?')
    time.sleep(1)
    if q1 == "да" or q1 == "Да":
        print('Программа продолжает работу!')
        time.sleep(1)
    elif q1 == "Нет" or q1 == "нет":
        print('Программа приостановлена!')
        break
    else:
        print("Вы ввели что то не то!")
        time.sleep(1)
