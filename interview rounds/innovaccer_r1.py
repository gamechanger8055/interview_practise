'''
meetings = [
["10:00 AM", "01:00 PM"],
["08:00 PM", "01:00 AM"],
["08:00 AM", "11:00 PM"],
["06:00 AM", "05:50 AM"],
["06:00 AM", "00:00 AM"],
["00:00 AM", "01:00 AM"],
["03:00 AM", "04:00 AM"],
["04:00 AM", "11:59 PM"],
]

free_slots = [[1, '12:00 AM', '10:00 AM'], [1, '01:00 PM', '08:00 PM'],
[2, '01:00 AM', '08:00 AM'], [2, '11:00 PM', '11:59 PM'], [3, '12:00 AM', '06:00 AM'],
[4, '05:50 AM', '06:00 AM'], [5, '01:00 AM', '03:00 AM']]

assumptions- no meeting can be longer than 24 hours.
no free slot be longer than 24 hours.
'''


def parse_time(time_str):
    hr = int(time_str[:2])
    mn = int(time_str[3:5])
    ampm = time_str[6:]
    if ampm == 'AM':
        return hr * 60 + mn
    return (hr + 12) * 60 + mn


def parse_to_time(times):
    time_st = "AM"
    if times > 720:
        times -= 720
        time_st = "PM"
    hr = times // 60
    mn = times % 60
    return f'{hr}:{mn} {time_st}'


print(parse_time("11:59 PM"))


def findFreeSlots(meetings):
    free_slots = []
    day_start = 0
    day_end = 1439
    day_count = 1
    if parse_time(meetings[0][0])>day_start:
        free_slots.append((day_count,parse_to_time(day_start),meetings[0][0]))
    for i in range(len(meetings)-1):
        start_next=meetings[i+1][0]
        end=meetings[i][1]
        start=meetings[i][0]
        if parse_time(start_next)>parse_time(end):
            if parse_time(end)<parse_time(start):
                day_count+=1
            print(1)
            free_slots.append((day_count, end,start_next))
        elif parse_time(end)<day_end:
            print(3)
            free_slots.append((day_count,end,parse_to_time(day_end)))
        elif parse_time(start_next)>day_start:
            print(2)
            day_count+=1
            free_slots.append((day_count, parse_to_time(day_start), start_next))

        #if parse_time(start_next)
        print(free_slots)


    if parse_time(meetings[-1][1]) < day_end:
        free_slots.append((day_count,meetings[-1][1], parse_to_time(day_end)))
    return free_slots


meetings = [
    ["10:00 AM", "01:00 PM"],
    ["08:00 PM", "01:00 AM"],
    ["08:00 AM", "11:00 PM"],
    ["06:00 AM", "05:50 AM"],
    ["06:00 AM", "00:00 AM"],
    ["00:00 AM", "01:00 AM"],
    ["03:00 AM", "04:00 AM"],
    ["04:00 AM", "11:59 PM"],
]

print(findFreeSlots(meetings))


