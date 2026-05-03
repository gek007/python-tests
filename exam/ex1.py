# write function:
# Counting Minutes

# Have the function CountingMinutes(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

# Examples

# Input: "12:30pm-12:00am"
# Output: 690

# Input: "1:23am-1:08am"
# Output: 1425


def CountingMinutes(s: str) -> int:
    def to_minutes(time_str: str) -> int:
        period = time_str[-2:]
        hour, minute = map(int, time_str[:-2].split(":"))
        if period == "am":
            hour = 0 if hour == 12 else hour
        else:
            hour = 12 if hour == 12 else hour + 12
        return hour * 60 + minute

    start, end = s.split("-")
    start_min = to_minutes(start)
    end_min = to_minutes(end)

    diff = end_min - start_min
    # If the difference is greater than 0, it means the end time is later on the same day,
    # so return the difference as is. If not, it means the end time is on the next day,
    # so add 1440 minutes (24 hours) to the difference to get the correct duration.
    return diff if diff > 0 else diff + 1440


print(CountingMinutes("9:00am-10:00am"))  # 60
print(CountingMinutes("1:00pm-11:00am"))  # 1320
print(CountingMinutes("12:30pm-12:00am"))  # 690
print(CountingMinutes("1:23am-1:08am"))  # 1425
print(CountingMinutes("10:30pm-08:00am"))
