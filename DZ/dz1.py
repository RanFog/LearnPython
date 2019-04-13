import random
secret_number = random.randint(0,100) #A ≤ N ≤ B

EXIT = "exit"
answer = -100

print ("Попробуйте отгадать загаданное число! (Для выхода наберите: ", EXIT,")")

while answer != EXIT :
    answer = input("---------------------------\nВведите число:")
    
    try:
        answer = int(answer)
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
