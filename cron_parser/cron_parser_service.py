def define_string(data, dataType):
    """
    INPUT: string = Value of parameter, datatype = Type of the parameter.
    OUTPUT: String indicating the matching time period for that parameter
    (e.g. which minutes the command will run).
    """
    values = {
        'week': [i for i in range(1, 8)],
        'month': [i for i in range(1, 13)],
        'hour': [i for i in range(0, 24)],
        'day': [i for i in range(1, 32)],
        'minute': [i for i in range(0, 60)]
    }

    months = [
        'JAN', 'FEB', 'MAR',
        'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP',
        'OCT', 'NOV', 'DEC'
    ]

    days = [
        'SUN', 'MON', 'TUE',
        'WED', 'THU', 'FRI',
        'SAT'
    ]

    if data == "*":
        return " ".join(map(str, values[dataType]))

    if data == "?":
        return "Not Specified"

    if "-" in data:
        values = days if dataType == "week" else months
        return handle_range(data, values, dataType)

    if "/" in data:
        return handle_intervals(data, values[dataType], dataType)

    if "," in data:
        if dataType in ["month", "week"]:
            val = days if dataType == "week" else months
            return handle_lists(data, values[dataType], dataType, val)
        else:
            return handle_lists(data, values[dataType], dataType)

    return data


def handle_lists(data, values, dataType, sub=None):
    """
       INPUT: string = Value of parameter, values = Array of possible value for
       parameter, datatype = Type of the parameter, sub = An optional parameter
       used when there are 2 possible input formats (e.g. JAN vs 1). We also
       verify that formats (i.e. JAN vs 1) are not mixed.
       OUTPUT: String of all the values listed in the input, if they are part
       of the range of possible values for that parameter.
    """
    string = data.split(",")
    types = None
    for i in string:
        try:
            val = int(i)
        except ValueError:
            val = i
        if not types:
            types = type(val)
        elif types != type(val):
            raise Exception(
                '{} input combination is not valid. Please use either string or number syntax.'.format(dataType))

        if type(val) == str and val not in sub:
            raise Exception('Invalid {} data provided'.format(dataType))
        if type(val) == int and val not in values:
            raise Exception('Invalid {} data provided'.format(dataType))

    return data.replace(",", " ")


def handle_range(data, values, dataType):
    """
    INPUT: string = Value of parameter, values = Array of possible values for
    parameter, datatype = Type of the parameter.
    OUTPUT: String of all values in the range given. If word form was used
    (e.g. JAN instead of 1), it returns a word-formatted range.
    """
    start, end = data.split("-")
    try:
        start, end = int(start), int(end)
    except ValueError:
        try:
            start, end = values.index(start), values.index(end)
            return " ".join(values[start:end + 1])
        except ValueError:
            raise Exception(
                '{} input combination is not valid. Please use either string or number syntax.'.format(dataType))
    return " ".join(map(str, [i for i in range(start, end + 1)]))


def handle_intervals(data, values, dataType):
    """
    INPUT: string = Value of parameter, values = Array of possible value for
    parameter.
    OUTPUT: String of all the values matching the specified interval in the
    possible range.
    """
    first, last = data.split("/")
    if first == "*":
        return " ".join(map(str, [i for i in values if i % int(last) == 0]))
    if type(first) != int or type(last) != int:
        raise Exception('Invalid input for {}'.format(dataType))
    else:
        return " ".join(map(str, [i for i in range(first, values[:-1]) if i % int(last) == 0]))


