# task 7
def canQueenMovetoCell(x1, y1, x2, y2):
    diff_x_y = x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    can = 'не може'
    if diff_x_y:
        can = 'може'

    info = f'''
    Ферзь |{can}| стати на клітку {x2,y2} з клітки {x1,y1}
    '''
    print(info)


canQueenMovetoCell(3,4,4,5)
canQueenMovetoCell(2,1,1,3)
canQueenMovetoCell(4,6,4,7)

