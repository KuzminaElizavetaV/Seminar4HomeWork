'''задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:*
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

from random import randint

def input_num(number):
    ch_num = False
    while not ch_num:
        try:
            num_input = int(input(number))
            ch_num = True
            if num_input <= 0:
                print("Внимание: значение должно быть > 0")
                ch_num = False
        except:
            print('Некорректный ввод, введите число')
    return num_input

def get_koef_list(k):
    koef_list = []
    for i in range(k):
        koef_list.append(randint(0, 100))
    koef_list.append(randint(1, 100))
    return koef_list

def get_polynomial(k):
    str_pol = ''
    kf = get_koef_list(k)
    print(f'Список коэффициентов: {kf}')
    pol = []
    for i in range(k, 1, -1):
        if kf[i] != 0:
            pol.append(str(f'{kf[i]}*x^{i}'))
    if kf[1] != 0:
        pol.append(str(f'{kf[1]}*x'))
    if kf[0] != 0:
        pol.append(str(kf[0]))
    str_pol = " + ".join(pol)
    str_pol = str_pol.replace(" 1*x", " x")
    str_pol = str_pol + " = 0"
    return str_pol

k = input_num("Натуральная степень k = ")
polynomial = get_polynomial(k)
print(polynomial)
with open("Polynomial.txt", "w") as data:
    data.write(polynomial)

