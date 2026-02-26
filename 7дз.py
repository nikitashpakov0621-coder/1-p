"""Декораторы"""



def checker(function): 
    def wrapper(*args, **kwargs): 
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"ошибка в: {exc}")
        else:
            print(f"нет проблемы : {result}")
            return result
    return wrapper 

def calculate(expression):
    return eval(expression)


calculate("2 + 2")

calculate("2 / 0")