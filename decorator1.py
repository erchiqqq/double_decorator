def second_outer(*dargs, **dkwargs): #Параметры декоратора
    def outer(func): #Сама декорируемая функция
        def inner(*args, **kwargs): # Параметры функции

            attempts = dkwargs['attempts']
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f'Error: {err}, attempts left: {attempts}')
                    attempts -= 1

        return inner
    return outer

def simple_deco(func):
    def inner(*args, **kwargs):
        print('Reklama')
        return func(*args, **kwargs)
    return inner

@simple_deco
@second_outer(attempts=5)

def div(a, b):
    return a / b

print(div(6, 0))