'''задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

def check_input(num_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(num_input))
            check_input = True
        except:
            print("Некорректный ввод!!!")
    return number_input

def prime_fact(n):
    list_fact = []
    n1 = 2
    while n1<=n:
        while n%n1==0:
           list_fact.append(n1)
           n = n/n1
        n1+=1
    return list_fact

num = check_input("Введите число N: ")
if num>1:
    if len(prime_fact(num))>1:
        print("Простые множители числа ", num, " - это: ", prime_fact(num))
    else: print("Простое число", num, "делится само на себя:", prime_fact(num))
else: print("Введите число > 1")