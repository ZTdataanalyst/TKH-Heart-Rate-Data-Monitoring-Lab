from data_cleaning import clean_heartrate_data
from statistics import average, median, range

# Using clean_heartrate_data from the data_cleaning module (imported above).
# Using average, median, and range from the statistics module (imported above).
# All of these functions are defined in their respective modules & can call them directly in this file.
def run(file: str):
    """
    Process heart rate data from a file by cleaning and
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
    
    # print out the removed values and cleaned values to the console
    for item in removed_values:
        print(f"Removed invalid value: {item}")

    for item in cleaned_list:
        print(f"Cleaned value: {item}")

    # calculate the average, median, and range of this file using the functions you've wrote


    # print out your data quality measure to the console
    avg = average(cleaned_list)
    med = median(cleaned_list)
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
