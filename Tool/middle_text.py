while True:
    try:
        pos = int(input('Введите число: '))
        if pos == 0:
            break
        print(f'Middle = {pos}')
    except:
        print('ЭТО НЕ ЧИСЛО!')