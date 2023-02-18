import datetime


def date_diff_in_Seconds(dt2, dt1):
    datetime.timedelta = dt2 - dt1
    print(datetime.timedelta)
    return datetime.timedelta.days * 24 * 3600 + datetime.timedelta.seconds


# Specified date
date1 = datetime.datetime(2023, 2, 18, 14, 50, 1)
# Current date
date2 = datetime.datetime.now()
print("seconds", (date_diff_in_Seconds(date2, date1)))
