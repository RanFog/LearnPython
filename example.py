#Комментарий

"""
Многострочный комментарий
"""
#Вывод
print("Hello, world!")

#Сдвиг вместо скобок
for i in range(4):
    print(i)
    print(type(i))

#определение типа переменной
num = 1.0
print(type(num))
num = int(num)
print(type(num))

#Погрешность
print(0.1+0.1+0.1)

#Встроенный хелп
help(print)
help(type)

#Побитовые операции
x = 4 
y = 3
x | y #Или
x ^ y #Исключающее или
x & y #И
x >> y#Побитовый сдвиг
~x    #Инверсия

#Логический тип
y = True
x = False

num = bool(num) #Конвертация в логический тип
