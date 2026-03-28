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