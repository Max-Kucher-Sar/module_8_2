def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += numbers[num]
        except TypeError:
            incorrect_data += 1
        finally:
            return result, incorrect_data

def calculate_average(numbers):
    total_numbers = personal_sum(numbers)
    try:
        average = sum(total_numbers) / len(total_numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    finally:
        return average

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать



