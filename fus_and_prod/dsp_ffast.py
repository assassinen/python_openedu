__author__ = 'NovikovII'


content = [
    [
        'Апгрейд быстрого фаст-гейта:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FFAST-prd-fast_20170523110457.zip',
        '\\\dd_p2devout.office.micex.com\Fusion\Releases\Fast\\1.3\\20170526_ffast-d01(10.63.10.230)',
        'ffast-d01(10.63.10.230)',
        'FUS_FASTF_01D',
        'DSP-FFAST-prd',
        '«All streams are online» | «All erepl streams are online».'
    ],
    [
        'Апгрейд фаст-гейта с полным ордер-логом:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FFAST-prd_ordlog-fast_20170523110457.zip',
        '\\\dd_p2devout.office.micex.com\Fusion\Releases\Fast\\1.3\\20170526_ffast-d01(10.63.10.230)',
        'ffast-d01(10.63.10.230)',
        'FUS_FASTFORDLOG_D01',
        'DSP-FFAST-prd_ordlog',
        '«All streams are online»'
    ],

    [
        'Апгрейд быстрого фаст-гейта:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FFAST-prd_reserve-fast_20170523110457.zip',
        '\\\dd_p2devout.office.micex.com\Fusion\Releases\Fast\\1.3\\20170526_ffast-d02(10.63.10.231)',
        'ffast-d02(10.63.10.231)',
        'FUS_FASTF_03D',
        'DSP-FFAST-prd_reserve',
        '«All streams are online» | «All erepl streams are online».'
    ],
    [
        'Апгрейд фаст-гейта с полным ордер-логом:',
        'fast_gate-1.3.4_20170523113001+svn74001-DSP-FFAST-prd_ordlog_reserve-fast_20170523110457.zip',
        '\\\dd_p2devout.office.micex.com\Fusion\Releases\Fast\\1.3\\20170526_ffast-d02(10.63.10.231) ',
        'ffast-d02(10.63.10.231)',
        'FUS_FASTFORDLOG_D02',
        'DSP-FFAST-prd_ordlog_reserve',
        '«All streams are online»'
    ]
]

out_file = "dsp-ffast.txt"
with open(out_file, "w", ) as r:

    for i in content:
        title = i[0]
        assembly = i[1]
        route = i[2]
        server = i[3]
        login = i[4]
        fast_name = i[5]
        log_message = i[6]


        # r.write('Настройка скриптов запуска:\n')
        # r.write('1. Скопировать файлы из ' + route + ' в директорию /app/fusion сервере ' + server + '\n')
        # r.write('2. В crontab изменить строку: \n')
        # r.write('   0 7 * * * cd /app/fusion; ./start_fstg.sh ' +  fast_name + '\n')
        # r.write('   на \n')
        # r.write('   0 7 * * * cd /app/fusion; ./start_fstg_ordlog.sh ' +  fast_name + '\n')
        # r.write('\n')

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
        if title != 'Апгрейд быстрого фаст-гейта:':
            r.write('8. Дождаться выхода фаст-гейта в режим онлайна, проверив, что в лог-файлах, расположенных в "/app/fusion/'+ fast_name + '/fast/log/" появилась запись: ' + log_message + '\n')
        else:
            r.write('8. Дождаться выхода фаст-гейта в режим онлайна, проверив, что в лог-файлах, расположенных в "/app/fusion/' + fast_name + '/fast/log/" появилась пара записей: '
                    + log_message.split('|')[0] + ' и ' + log_message.split('|')[1] + '\n')

        r.write('Команда для проверки:' + '\n')
        r.write('grep "All " /app/fusion/' + fast_name + '/fast/log/fastgate*.log' + '\n')
        r.write('\n')
        r.write('\n')
        r.write('\n')
    r.write('\n')
    r.write('\n')
    r.write('\n')





