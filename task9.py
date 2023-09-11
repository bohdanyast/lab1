# task 9
def getReversedInteger(number):
    const = number
    reversed = ''
    while number > 0:
        digit = number % 10
        reversed += str(digit)
        number //= 10

    info = f'''
    {const} ===> {reversed}
    '''
    print(info)


getReversedInteger(165465465464)
getReversedInteger(19)
getReversedInteger(123)
