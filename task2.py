# task 2
from math import sqrt


def countGeometricalAvg(val1, val2):
    avg_geo = sqrt(val1 * val2)
    info = f'''
    Числа: {val1},{val2};
    Середнє геометричне: {avg_geo};
    '''
    print(info)


countGeometricalAvg(7, 12)
countGeometricalAvg(17, 32)
countGeometricalAvg(7, 7)