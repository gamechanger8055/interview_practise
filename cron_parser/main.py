import sys
from cron_parser_service import define_string
def describe_cron(input):
    """
    INPUT: cron_str = The input string containing the entire cron string from
    the user.
    OUTPUT: A formatted string containing the minute, hour, day, month,
    weekday and command that will run.
    """
    try:
        minute, hour, day, month, week, cmd = input.split(" ")
    except:
        raise Exception("Not enough parameters passed.")
    return '\n'.join([
        "minute        {}".format(define_string(minute, 'minute')),
        "hour          {}".format(define_string(hour, 'hour')),
        "day of month  {}".format(define_string(day, 'day')),
        "month         {}".format(define_string(month, 'month')),
        "day of week   {}".format(define_string(week, 'week')),
        "command       {}".format(cmd)
    ])


def main():
    print(describe_cron(sys.argv[1]))


if __name__ == "__main__":
    main()
