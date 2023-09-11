# task 11
def isSimple(num):
    how_many = 0
    for i in range(1, num+1):
        if num % i == 0:
            how_many += 1

    info = f'''
    {num} просте: {how_many == 2}
    '''
    print(info)


isSimple(31)
isSimple(322)
isSimple(32)
