def methods_counting(method_list):
    def wrapper():
        a = method_list()
        count: int = a.index(a[-1]) + 1
        return f' {a} \n {count}'

    return wrapper


@methods_counting
def magic_list():
    from pydoc import locate

    object_name = input('Please enter your object \n')
    method_name = locate(object_name)  # Определяем объект
    full_methods_list_temp: list = list(dir(method_name))
    full_methods_list: list = []
    for i in full_methods_list_temp:
        if '__' in i:
            full_methods_list.append(i)
    return full_methods_list


print(magic_list())
