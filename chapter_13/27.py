# Задание 27

# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надёжным, или False в противном случае.

# Пароль является надёжным, если:

# его длина не менее 8 символов; 
# он содержит как минимум одну заглавную букву (верхний регистр); 
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# Примечание. Приведённый ниже код:

# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
                  
# должен выводить:

# True
# False

'''
# объявление функции
def is_password_good(password):
    pass

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
'''

def is_password_good(password):
    len_validate = False
    upper_validate = False
    lower_validate = False
    digit_validate = False

    if len(password) >= 8:
        len_validate = True
    
    for symbol in range(len(password)):
        if password[symbol].isupper():
            upper_validate = True
        if password[symbol].islower():
            lower_validate = True
        if password[symbol].isdigit():
            digit_validate = True

    if len_validate and upper_validate and lower_validate and digit_validate:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))