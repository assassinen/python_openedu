__author__ = 'NovikovII'



content = [
    [
        'Апгрейд московского фаста:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FAST-prd-fast_20170523110457.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d01(10.63.10.232)',
        'fast-d01(10.63.10.232)',
        'FUS_FAST_01D',
        'DSP-FAST-prd',
        '«All streams are online»'
    ],
    [
        'Апгрейд казахского фаста:',
        'fast_gate-1.3.64_15052017190727+svn73823-DSP-KZ-prd-fast_20012017140223.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d01(10.63.10.232)',
        'fast-d01(10.63.10.232)',
        'KZ_FAST_D01_ROUTER',
        'DSP-KZ-prd',
        '«All streams are online»'
    ],
    [
        'Апгрейд украинского фаста:',
        'fast_gate-1.3.64_15052017190727+svn73823-DSP-UX-prd-fast_20012017140223.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d01(10.63.10.232)',
        'fast-d01(10.63.10.232)',
        'UX_FAST_D01_ROUTER',
        'DSP-UX-prd',
        '«All streams are online»'
    ],

    [
        'Апгрейд московского фаста:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FAST-prd_reserve-fast_20170523110457.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d02(10.63.10.233)',
        'fast-d02(10.63.10.233)',
        'FUS_FAST_03D',
        'DSP-FAST-prd_reserve',
        '«All streams are online»'
    ],
    [
        'Апгрейд казахского фаста:',
        'fast_gate-1.3.64_15052017190727+svn73823-DSP-KZ-prd_reserve-fast_20012017140223.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d02(10.63.10.233)',
        'fast-d02(10.63.10.233)',
        'KZ_FAST_DRZ_ROUTER',
        'DSP-KZ-prd_reserve',
        '«All streams are online»'
    ],
    [
        'Апгрейд украинского фаста:',
        'fast_gate-1.3.64_15052017190727+svn73823-DSP-UX-prd_reserve-fast_20012017140223.zip',
        '\\\DD_P2DEVOUT.OFFICE.MICEX.COM\Fusion\Releases\Fast\\1.3\\20170526_fast-d02(10.63.10.233)',
        'fast-d02(10.63.10.233)',
        'UX_FAST_DRZ_ROUTER',
        'DSP-UX-prd_reserve',
        '«All streams are online»'
    ],

]

out_file = "dsp_fast.txt"
with open(out_file, "w", ) as r:

    for i in content:
        title = i[0]
        assembly = i[1]
        route = i[2]
        server = i[3]
        login = i[4]
        fast_name = i[5]
        log_message = i[6]


        r.write(title + ' \n')
        r.write('1. Скопировать ' + assembly + ' из ' + route + ' в директорию /tmp на сервере ' + server + '\n')
        r.write('2. Выполнить команду "cd /; unzip /tmp/' + assembly + '"\n')
        r.write('3. Убедиться, что в /app/fusion/ver/ создана директория ' + assembly[0:-4] + ' \n')
        r.write('4. В директории ' + assembly[0:-4] + ' выполнить скрипт командой "./link.sh"\n')
        r.write('5. Убедиться, что в /app/fusion/ создана директория ' + fast_name + ' с вложенными директориями, файлами и скриптами\n')
        r.write('6. В файле /app/fusion/' + fast_name + '/fast/etc/router.ini задать пароль для пользователя ' + login + ' \n')
        #r.write('7. Запустить fast_gate "cd /app/fusion/; ./start_fstg.sh ' + fast_name + '"\n')
        r.write('7. Запустить fast_gate:' + '\n')
        r.write('   cd /app/fusion/' + '\n')
        r.write('   ./stop_fstg.sh ' + fast_name + '"\n')
        r.write('   ./start_fstg.sh ' + fast_name + '"\n')
        r.write('8. Дождаться выхода фаст-гейта в режим онлайна, проверив, что в лог-файлах, расположенных в "/app/fusion/'+ fast_name + '/fast/log/" появилась запись ' + log_message + '\n')
        r.write('\n')
        r.write('\n')
        r.write('\n')





