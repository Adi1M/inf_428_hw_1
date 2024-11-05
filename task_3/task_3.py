def time_diff(time_from, time_to):
    if time_from > time_to:
        return (24 + time_to) - time_from
    else:
        return time_to - time_from
