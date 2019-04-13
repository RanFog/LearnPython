import random
secret_number = random.randint(0,100) #A ≤ N ≤ B
__EXIT__ = -1000;
answer = -100;
print ("Попробуйте отгадать загаданное число! (Для выхода наберите: ", __EXIT__,")")
while answer != __EXIT__ :
    print("---------------------------\nВведите число:")
    try:
        answer = int(input())
    except Exception as ex:
        print("Надо вводить числа!")
        continue
    if answer == secret_number : 
        print ("Вы угадали!") 
        break
    elif answer < secret_number : 
        print ("Слишком мало...")
    elif answer > secret_number : 
        print ("Слишком много...")
