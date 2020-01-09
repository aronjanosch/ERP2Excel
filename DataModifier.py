import datetime


def get_address(data):
    x = data.replace('\n', '')
    x = x.replace('<br>', '\n')
    x = x.split("\n")
    string = ''
    for i in range(len(x)-2):
        string += x[i]
        string += ' '

    return string


def change_date(date):
    d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    day_string = d.strftime('%Y-%m-%d')
    return day_string
