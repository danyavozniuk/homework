a = 10
b = 3.14
c = "Hello"
d = [1, 2, 3]
e = {'key': 'value'}
f = (1, 2)
g = True

# створення першого списку
values = [a, b, c, d, e, f, g]

# створення другого списку
types = [type(value) for value in values]

# обчислення частсти данних
from collections import Counter
type_counts = Counter(types)

# найчастіший тип данних
most_common_type = type_counts.most_common(1)[0][0]

# пезультат
print(f"Найчастіший тип даних: {most_common_type}")
