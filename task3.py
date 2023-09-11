# task3
def countRectangleSquareByCoordinates(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)

    square = a * b
    perimeter = 2 * (a + b)

    info = f'''
    Координати двох протилежних вершин прямокутника: ({x1},{y1}),({x2},{y2});
    Площа прямокутника: {square};
    Периметр прямокутника: {perimeter};
    '''
    print(info)


countRectangleSquareByCoordinates(3,6,8,10)
countRectangleSquareByCoordinates(4,7,2,12)
countRectangleSquareByCoordinates(4,6,8,10)