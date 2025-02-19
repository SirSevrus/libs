def sort_data(data, index):
    """
    Sorts a list of lists based on the specified index.

    Parameters:
    -----------
    data : list of lists
        The data to be sorted.
    index : int
        The index of the inner list to sort by.

    Returns:
    --------
    list of lists:
        The sorted data, excluding entries that do not contain the given index.

    Example:
    --------
    data = [[101, "Alice", 90], [103, "Bob"], [102, "Charlie", 85]]
    sorted_data = sort_data(data, 0)  # Sort by first column (index 0)
    print(sorted_data)  # Output: [[101, "Alice", 90], [102, "Charlie", 85]]
    """
    # Filter out entries that do not have the given index
    valid_data = [row for row in data if len(row) > index]

    # Sort the filtered data based on the given index
    sorted_data = sorted(valid_data, key=lambda x: x[index])

    return sorted_data