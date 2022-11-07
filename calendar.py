from datetime import datetime, timedelta


def calendar(year, month):
    next_month = datetime(year, month, 28) + timedelta(days=4)
    max_days = (next_month - timedelta(days=next_month.day)).day
    title = f"{datetime(year, month, 1).strftime('%B')} {year}"
    header = f"{' ' * int(int(20 - len(title)) / 2)}{title}\n" + 'Su Mo Tu We Th Fr Sa\n'
    pattern = {6: '   ', 0: '   ', 1: '   ', 2: '   ', 3: '   ', 4: '   ', 5: '   '}
    rows = []
    for day in range(1, max_days + 1):
        date_weekday = datetime(year, month, day).weekday()
        if (date_weekday - datetime(year, month, day).day >= -1) == True and date_weekday < 5:
            pattern[date_weekday] = f' {day} ' if day < 10 else f' {day} '
        elif date_weekday == 5 or day == max_days:
            pattern[date_weekday] = f' {day}' if day < 10 else f'{day}'
            rows.append(''.join(pattern.values()))
            for i in range(7):
                pattern[i] = '  '
        else:
            pattern[date_weekday] = f' {day} ' if day < 10 else f'{day} '
    return header + ''.join(f'{row}\n' if count != len(rows) else f'{row}' for count, row in enumerate(rows, start=1))
