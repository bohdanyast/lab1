# task 8
def printGrowingList(a, b):
    nums = 0
    arr = []
    for i in range(a, b+1):
        arr.append(i)
        nums += 1

    info = f'''
    Nums: {arr}
    How many: {nums}
    '''
    print(info)


printGrowingList(3,9)
printGrowingList(3,19)

printGrowingList(3,29)
