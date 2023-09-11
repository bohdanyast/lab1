# task 10
def funWithArr(arr):
    old_arr = list(arr)  # зберегти копію масиву
    avg = sum(arr) / len(arr)
    for i in range(len(arr)):
        if arr[i] > avg:
            arr[i] -= 18

    info = f'''
    {old_arr} ===> {arr}
    avg: {avg}
    '''
    print(info)


funWithArr([118, 218, 18, 518, 34])
funWithArr([18, 218, 18, 118, 34])
funWithArr([118, 18, 18, 218, 34])
