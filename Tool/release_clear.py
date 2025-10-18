def clear(): 
    clear_files = ['data_user\data_file_game\height.txt','data_user\data_file_game\widch.txt','data_user/name.txt','data_user\moch.txt','data_user\date.txt']
    for i in range(0,5):
        t = open(clear_files[0], 'w')
        t.write('')
        t.close()
        clear_files.pop(0)


    #WRITER#
    tt = open('data_user\display_config.txt', 'w')
    tt.write('False')
    tt.close()
    tt = open('data_user\display.txt', 'w')
    tt.write('FS')
    tt.close()
    tt = open('data_user\language.txt', 'w')
    tt.write('RU')
    tt.close()
    tt = open('data_user\subtitle.txt', 'w')
    tt.write('RU')
    tt.close()
    tt = open('data_user\succes.txt', 'w')
    tt.write('false')
    tt.close()
    tt = open('data_user/view_warning.txt', 'w')
    tt.write('1')
    tt.close()
    tt = open('data_user/volume_menu.txt', 'w')
    tt.write('0.6')
    tt.close()
    return 'Дата данные восстановлены в положение Defoult'

print('Запустить отчистку файлов для дата релиза?')
while True:
    i = input('Д/н>>> ')
    if i == 'Д' or i == 'д':
        clear()
        print(clear())
        exit()
    else:
        exit()