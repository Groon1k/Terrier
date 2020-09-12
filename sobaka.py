import datetime


def split(lst, pathh):
    lst_1 = []
    for i in lst:
        if i.find('-') != -1:
            lst_1.extend([str(j) for j in(list(range(int(i[:i.find('-')]), int(i[i.find('-') + 1:]) + 1)))])
        else:
            lst_1.append(i)
    return [str(pathh + 'АРМ ' + i + 'L') for i in lst_1]


def time(st_time, difference):
    h, m = int(st_time[:st_time.find(':')]), int(st_time[st_time.find(':') + 1:])
    hm = h*60 + m + difference
    h_end, m_end = hm // 60, hm % 60
    return str(datetime.time(h_end, m_end))[:5]


def files(lst, lst2, iterator, name_user, num_date, num_time, time_difference):
    if iterator > len(lst) - 1:
        raise SystemExit('Заибавси(')
    with open(lst[iterator] + '.txt', 'w') as f:
        f.write(lst2[0][:len(lst2[0]) - 1] + name_user + '\n')
        f.write(lst2[1][:len(lst2[1]) - 1] + num_date + num_time + '\n')
        f.write(lst2[2])
        f.write(lst2[3])
        f.write(lst2[4])
    num_time = time(num_time, time_difference)
    return files(lst, lst2, iterator + 1, name_user, num_date, num_time, time_difference)


path = input(r'enter the path to your file: ') + '\\'
lst_nums_arms = input('you can set the range: ').split()
lst_final = split(lst_nums_arms, path)
user = input('name plzzzz: ')
date = input('date: ') + '  '
start_time = input('start time: ')
time_diff = int(input('time difference between installations: '))
lines = []
with open(path + 'test.txt') as file:
    for j in file:
        lines.append(j)
print(lines)
files(lst_final, lines, 0, user, date, start_time, time_diff)