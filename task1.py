# task 1
def countSquareAndPerimetreOfRectangle(side_a, side_b):
    square = side_a * side_b
    perimetre = 2 * (side_a + side_b)
    info = f'''
    Сторони: {side_a},{side_b};
    Площа прямокутника: {square};
    Периметр прямокутника: {perimetre};
    '''
    print(info)


countSquareAndPerimetreOfRectangle(4,5)
countSquareAndPerimetreOfRectangle(9,7)
countSquareAndPerimetreOfRectangle(5,12)