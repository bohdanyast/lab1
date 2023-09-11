# task 6
def isCellBlack(x, y):
    correctness = 'неправильне'
    # клітка (1,1) - чорна
    # задана клітка може бути чорною, тоді коли x = y, або коли змінні однакової парності
    equal_pairings = x % 2 == 0 and y % 2 == 0
    if x == y or equal_pairings:
        correctness = 'правильне'

    info = f'''
    Клітка ({x},{y}) чорна - {correctness} висловлення
    '''
    print(info)


isCellBlack(4, 6)
isCellBlack(5, 6)
isCellBlack(8, 6)
