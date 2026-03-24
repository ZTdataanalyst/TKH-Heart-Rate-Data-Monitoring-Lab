def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    clean_list = []
    removed_values = []

    for item in data:
        item = item.strip()          # remove \n and spaces
        if item.isdigit():           # good numeric value
            clean_list.append(item)
        else:                        # bad value: "NO DATA", "", etc.
            removed_values.append(item)

    return (clean_list, removed_values)
        
result = (clean_heartrate_data)
 
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

def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """

    # open file using file I/O and read it into the `data` list
    with open(file) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line)
    
    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)
    
    for item in removed_values:
        print(f"Removed invalid value: {item}")

    for item in cleaned_list:
        print(f"Cleaned value: {item}")

    # calculate the average, median, and range of this file using the functions you've wrote


    # print out your data quality measure to the console
    avg = average(cleaned_list)
    med = median (cleaned_list)
    rng = range(cleaned_list)

    # print out your descriptive statistics to the console
    print("average =:", avg)
    print("median =:", med)
    print("range =:", rng)



if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
