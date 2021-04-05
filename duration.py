duration = int(input("Please, enter duration in seconds : \t"))
periods_in_sec = [31536000, 2592000, 86400, 3600, 60, 1]
periods_name = ['year', 'month', 'day', 'hour', 'minute', 'second']
total_answer = ""
for idx in range(len(periods_in_sec)):
    units_count = duration // periods_in_sec[idx]
    if units_count > 0:
        suffix = ''
        if units_count > 1:
            suffix = 's'
        total_answer += " {0} {1} ".format(str(units_count), periods_name[idx] + suffix)
        duration = duration % periods_in_sec[idx]
print(total_answer)
