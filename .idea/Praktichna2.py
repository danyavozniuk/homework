# створення основного словника
main_dict = {
    "name": "Danya",
    "age": 16,
    "address": {
        "street": "Vilhova",
        "city": "Lutsk",
        "country": "Ukraine",
    },
    "is_student": True
}

# створення словника з типами данних
types_dict = {
    "name": type(main_dict["name"]),
    "age": type(main_dict["age"]),
    "address": {key: type(value) for key, value in main_dict["address"].items()},
    "is_student": type(main_dict["is_student"])
}

# вивід результатів
print("основний словник:")
print(main_dict)

print("\словник з типами даних:")
print(types_dict)
