wault = dict()


def memory_decorator(function):
    def wrapper(*args):
        for i in args:
            if i in list(wault.keys()):
                return wault[i]
            else:
                value = function(i)
                wault[i] = value

    return wrapper

@memory_decorator
def hash_list(*args):
    value_list = []
    args_list = [i for i in args]
    for i in args:
        if type(i) == int:
            value = i * 3
        elif type(i) == str:
            value = i.upper()
        elif type(i) == bool:
             value = True
        else:
             value = None
        value_list.append(value)
    wault_2 = {k: v for k, v in list(zip(args_list, value_list))}
    return wault_2


print(hash_list(1, 2, 3, 'str'))
