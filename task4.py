# task4
def isEven(number):
    flag = 'непарне'
    if number % 2 == 0 and number > 0:
        flag = 'парне'
    elif number <= 0:
        flag = 'не має парності'
    info = f'''
    Число {number} - {flag};
    '''
    print(info)


isEven(5)
isEven(0)
isEven(8)
