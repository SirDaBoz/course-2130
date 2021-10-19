def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    if number % 20 > 0:
        return (number//20 + 1) * 20
    return number//20 * 20


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    lst = string.split(' ')
    for i, item in enumerate(lst):
        lst[i] = lst[i][::-1]
    return ' '.join(lst)


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    lst = []
    for key in dictionary:
        lst.append(str(key) + ': ' + str(dictionary[key]))
    return '; '.join(lst)


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if len(sub_string) == 0:
        return True
    sub_string = sub_string[::-1]
    for i in range(len(string)-len(sub_string)):
        if string[i:i+len(sub_string)] == sub_string:
            return True
    return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    res = []
    for s in strings:
        lst = s.split(' ')
        if len(lst) == 4 and lst[:3] == lst[-1].split('*'):
            res.append(s)
    return res