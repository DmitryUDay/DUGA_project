patch = input('Введите путь папки без последнего /: ')#

copy = input('Введите кол-во копирования: ')#

name = input('Введите название переменной: ')#

types = input('Введите формат изображения: ')#

widch = input('Введите ширину изображения: ')#

height = input('Введие высоту изображения: ')#

# sixSt = pg.image.load('img/loading/6.jpg')
# sixSt = pg.transform.scale(sixSt,(500,500))

copy = int(copy)

types = types.replace('.','')

for i in range(1,copy+1,1):
    print(f"\n{name}{i} = pg.image.load('{patch}/{i}.{types}')")
    print(f"{name}{i} = pg.transform.scale({name}{i},({widch},{height}))")