def print_(team1_num, team2_num):
    print('В команде Мастера кода участников: %s' % team1_num)
    print('Вкоманде Волшебники данных участников: %s' % team2_num)
    print('И того сегодня в командах: %s и %s' % (team1_num, team2_num))


def print_practice(score_1, score_2, team1_time, team2_time):
    tasks_total = score_1 + score_2
    time_avg = round((team1_time + team2_time) / tasks_total, 2)
    # ------ .format()
    print('Команда {} рештла задач: {}'.format('Мастера кода', score_1))
    print('Команда {1} решила задач: {0}'.format(score_2, 'Волшебники данных'))
    print('Команда {team1} решила задач: {}!'.format(team1_time, team1='Мастера кода'))
    print('Команда {team2} решила задач: {time}!'.format(team2='Волшебники данных', time=team2_time))

    if score_1 > score_2 or score_1 == score_2 and team1_time > teame2_time:
        result = 'Мастера кода'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < teame2_time:
        result = 'Волшебники данных'
    else:
        result = 'Ничья'
    # ------ f'{}'
    print(f'Результаты битвы: победа команды {result}')
    print(f'Сегодня было решено {tasks_total} задачи, в среднем на одну задачу потрачено {time_avg} секунды')


print_(5, 6)
# print_format(40, 42)
# format_time(1552.512, 2153.31451)
print_practice(40, 42, 1552.512, 2153.31451)
