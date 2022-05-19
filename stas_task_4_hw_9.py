wault = {}


def memory_decorator(function):
    global wault

    def wrapper(*args):
        if wault.get(args):
            print('From wault')
            return wault[args]
        else:
            print('Calculation')
            wault[args] = function(*args)
            return wault[args]

    return wrapper


@memory_decorator
def hash_list(*args):
    len_value = len(args)
    return len_value


print(hash_list(1, 2))
print(hash_list(1, 2, 3, 'sss'))
print(hash_list(1, 2, 4, 5))
print(hash_list(1, 2))
