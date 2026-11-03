def print_perm_time_call(msc_time):
    msc_minutes = ((int(msc_time[0]) * 10 + int(msc_time[1])) * 60 + (int(msc_time[3]) * 10 + int(msc_time[4])))
    perm_minutes = msc_minutes + 120
    perm_hours = perm_minutes // 60
    new_perm_minutes = perm_minutes % 60

    perm_time = []

    if perm_hours < 10:
        perm_time.append(str(0))
        perm_time.append(str(perm_hours))
    else:
        perm_time.append(str(perm_hours))

    perm_time.append(':')

    if new_perm_minutes < 10:
        perm_time.append(str(0))
        perm_time.append(str(new_perm_minutes))
    else:
        perm_time.append(str(new_perm_minutes))

    perm_time = ''.join(perm_time)    

    print(f'Созвон будет в {perm_time}.')

msc_time = input()

print_perm_time_call(msc_time)