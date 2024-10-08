def remove_duplicates(input_list):
    # Використовуємо set для видалення дублікатів
    return list(set(input_list))

def sort_mixed_list(input_list):
    # Сортуємо список: спочатку числа, потім рядки
    numbers = sorted(x for x in input_list if isinstance(x, (int, float)))
    strings = sorted(x for x in input_list if isinstance(x, str))
    return numbers + strings

# Основний список
original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Світ']

# Видаляємо дублікатів
unique_list = remove_duplicates(original_list)

# Сортуємо
sorted_list = sort_mixed_list(unique_list)

print("Список без дублікатів:", unique_list)
print("Відсортований список:", sorted_list)
