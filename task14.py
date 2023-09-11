# task 14
while True:
    trials = 5
    print(f"trials: {trials}")
    for i in range(trials):
        num = int(input())
        trials -= 1

        if num == 5:
            print('Well Done!')
            break

        if trials == 0:
            print('Try again!\n')
            break
        print(f"trials: {trials}")