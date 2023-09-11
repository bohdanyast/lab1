# task 7
def canHorseMovetoCell(x1, y1, x2, y2):
    diff_x_y = abs(x2-x1) == 1 and abs(y2-y1) == 2
    can = 'не може'
    if diff_x_y:
        can = 'може'

    info = f'''
    Ферзь |{can}| стати на клітку {x2,y2} з клітки {x1,y1}
    '''
    print(info)


canHorseMovetoCell(1,1,2,3)
canHorseMovetoCell(2,1,2,3)
canHorseMovetoCell(3,1,4,3)

