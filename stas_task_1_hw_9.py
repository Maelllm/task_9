def edit_number():
    code: str = '+380'

    def edit_code(number):
        print(f'{code}{number}')

    return edit_code


a = edit_number()
print(a(4541531523))
