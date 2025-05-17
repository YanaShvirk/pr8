sum = 0

while True:
    user_input = input("Введите число или 'stop'/'end' для завершения: ")
    
    if user_input.lower() in ['stop', 'end']:
        break
    elif user_input.isdigit():  # Проверяем, является ли ввод числом
        sum += int(user_input)  # Если число, добавляем к сумме
    else:
        print("Пожалуйста, введите число или 'stop'/'end'.")  # Если не число и не команда
    
print(f"Сумма введенных чисел: {sum}")
