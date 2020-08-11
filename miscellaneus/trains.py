"""
On a train terminal there are schedules:
    start: arrives at terminal
    end: leaves the terminal
based on a schedule, (set of starts and ends) determine what is the maximum
number of trains at the station at the same time.
"""


def get_max_trains(schedule):
    max_count = 0
    count = 0
    for timestamp in get_sorted_timestamps(schedule):  # n + n + nlogn
        count += 1 if timestamp.is_start else -1
        max_count = max(max_count, count)
    return max_count  #nlogn


def get_sorted_timestamps(schedule):
    timestamps = []
    for start, end in schedule:
        timestamps.extend([Timestamp(start, True), Timestamp(end, False)])  # n
    return sorted(timestamps)  # nlogn


class Timestamp:
    def __init__(self, time, is_start):
        self.time = time
        self.is_start = is_start

    def __lt__(self, other):
        if self.time < other.time:
            return True
        elif self.time > other.time:
            return False
        else:
            return True if self.is_start else False

    def __repr__(self):
        is_start = 'start' if self.is_start else 'end'
        return f'{self.time} {is_start}'

