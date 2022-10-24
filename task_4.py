'''задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.'''

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print("Ввод не корректен!")
    return number_input

def get_nod(x, y):
    while x*y !=0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return (x + y)

def get_nok(a,b):
    return int(a*b/get_nod(a,b))

num_a =  check_input("Введите число a: ")
num_b =  check_input("Введите число b: ")
print(f"НОД равен:", get_nod(num_a, num_b))
print(f"НОК равно:", get_nok(num_a, num_b))