result = []

def divider(a, b):
    if a < b:
        raise ValueError("a меньше b")
    if b > 100:
        raise IndexError("b больше 100")
    return a / b

data = {10: 2, 2: 5, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Ошибка для {key}: {e}")

print(result)