def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for item in data:
        total += int(item)
    avg_data = total / len(data)
    return round(avg_data, 2)

def median(data: list) -> float:
    """
    Calculate the median of the list of integers. Assumes data is clean.
    """
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2

    if len(sorted_data) % 2 == 0:
        median_data = (int(sorted_data[mid - 1]) + int(sorted_data[mid])) / 2 
    else:
        median_data = int(sorted_data[mid])
    return round(median_data, 2)

def range(data: list) -> float:
    """
    Calculate the range of the list of integers. Assumes data is clean.
    """
    numeric_data = [float(x) for x in data]
    sorted_data = sorted(numeric_data)
    range_data = sorted_data[-1] - sorted_data[0]
    return round(range_data, 2)


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass