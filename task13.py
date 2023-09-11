# task 13.1
def form1():
    field_name = input('Your name: ')
    field_surname = input('Your surname: ')
    field_phone = input('Your phone: ')
    txt = "Не залишайте жодні поля порожніми"

    if field_surname and field_phone and field_name:
        txt = 'Спасибі'
    print(txt)

form1()


# task 13.2
def form2():
    field_name = input('Your name: ')
    field_surname = input('Your surname: ')
    field_phone = input('Your phone: ')
    txt = "Не залишайте жодні поля порожніми"

    if field_surname or field_phone or field_name:
        txt = 'Спасибі'
    print(txt)

form2()


# task 13.3
def form3():
    field_name = input('Your name: ')
    field_surname = input('Your surname: ')
    field_phone = input('Your phone: ')
    txt = "Не залишайте жодні поля порожніми"

    if field_surname or field_name:
        txt = 'Спасибі'
    print(txt)

form3()