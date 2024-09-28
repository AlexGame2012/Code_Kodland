import random
import time
hran1 = "+-/*!&$#?=@"
hran2 = "abcdefghijklnopqrstuvwxyz"
hran3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hran4 = "1234567890"
hran5 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
hran6 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
user_login = input('Ваш логин: ')
time.sleep(1)
print('Добро пожаловать в Geniration Parol,', user_login, '!')
time.sleep(1)
while True:
    q = int(input("Скажите длину пароля которую вы хотите:"))
    time.sleep(1)
    v = input("Скажите, текст будет из: А. Заглавные русские буквы. Б. Маленькие русские буквы. В. Заглавные английские буквы. Г. Маленькие английские буквы. Д. Символы. Е. Цифры (Введите заглавную русскую букву из списка.)")
    parol = ""
    for i in range(q):
        if v == "А":
            s = random.choice(hran6)
        elif v == "Б":
            s = random.choice(hran5)
        elif v == "В":
            s = random.choice(hran3)
        elif v == "Г":
            s = random.choice(hran2)
        elif v == "Д":
            s = random.choice(hran1)
        elif v == "Е":
            s = random.choice(hran4)
        else:
            print("Вы ввели не правильно букву и сломали программу!")
            break    
        parol += s
    print("Генерируется ваш пароль!") 
    time.sleep(1)
    print("Загрузка...")
    time.sleep(10)   
    print("Вот ваш сгенерированный пароль")    
    print(parol)
    time.sleep(5) 
    print(" ")
    print(" ")
    print(" ")
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
