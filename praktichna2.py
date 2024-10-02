# Основний словник
main_dict = {
    "name": "Danya",
    "age": 16,
    "address": {
        "street": "Vilhova",
        "city": "Lutsk",
        "country": "Ukraine"
    },
    "is_student": True
}

# Словник з типами даних
# Генерує словник з типами данних
# отримання типів
types_dict = {
    key: {k: type(v) for k, v in (value.items() if isinstance(value, dict) else {key: value}.items())}
    for key, value in main_dict.items()
}

# Вивід результатів
print("основний словник:", main_dict)
print("словник з типами даних:", types_dict)
