import sys


def parse_cron_field(field, min_value, max_value):
    if field == "*":
        return list(range(min_value, max_value + 1))

    parts = field.split(',')
    values = set()
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            values.update(range(start, end + 1))
        elif '/' in part:
            step_range, step = part.split('/')
            step = int(step)
            if step_range == "*":
                values.update(range(min_value, max_value + 1, step))
            else:
                start, end = map(int, step_range.split('-'))
                values.update(range(start, end + 1, step))
        else:
            values.add(int(part))
    return sorted(values)


def expand_cron(cron_string):
    parts = cron_string.split()
    if len(parts) != 6:
        raise ValueError("Invalid cron string format")

    minute_field, hour_field, dom_field, month_field, dow_field, command = parts

    minutes = parse_cron_field(minute_field, 0, 59)
    hours = parse_cron_field(hour_field, 0, 23)
    dom = parse_cron_field(dom_field, 1, 31)
    months = parse_cron_field(month_field, 1, 12)
    dow = parse_cron_field(dow_field, 0, 6)

    return {
        "minute": minutes,
        "hour": hours,
        "day of month": dom,
        "month": months,
        "day of week": dow,
        "command": command
    }


def print_cron_expansion(expansion):
    for field, times in expansion.items():
        if isinstance(times, list):
            times = ' '.join(map(str, times))
        print(f"{field:<14} {times}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py '<cron_string>'")
        sys.exit(1)

    cron_string = sys.argv[1]
    try:
        expansion = expand_cron(cron_string)
        print_cron_expansion(expansion)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
