a = 1
b = a
id(a)
id(b)
a = 2
a != b
a = []
b = a
a.append('asdf')
b = a


def f():
    x = 1  # Local


def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    return inner


o = one()
o()
dir(o)
o.__closure__
o.__closure__[0]
dir(o.__closure__[0])
o.__closure__[0].cell_contents
a = o.__closure__[0].cell_contents
id(a)
a.append('asdf')
o()

id(a)
