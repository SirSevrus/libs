import csv

def read_csv(filepath: str, yield_data: bool = False):
    """
    Reads a CSV file and returns its contents.

    Parameters:
    -----------
    filepath : str
        The path to the CSV file.
    yield_data : bool, optional
        If True, returns a generator yielding rows one by one.
        If False (default), returns a list of all rows.

    Returns:
    --------
    generator or tuple:
        - If `yield_data=True`, returns a generator that yields rows one by one.
        - If `yield_data=False`, returns a tuple (bool, list), where:
          - The boolean value is always True if no errors occur.
          - The list contains all rows from the CSV file.

    Raises:
    -------
    FileNotFoundError:
        If the file does not exist.
    RuntimeError:
        If an unexpected error occurs while reading the file.

    Example Usage:
    --------------
    # Reading all data at once
    success, data = read_csv("test.csv")
    if success:
        print("CSV Data:", data)

    # Reading line by line using a generator
    csv_gen = read_csv("test.csv", yield_data=True)
    for row in csv_gen:
        print(row)
    """
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            if yield_data:
                for row in csv.reader(file):
                    yield row  # Yield rows one by one
            else:
                return True, list(csv.reader(file))  # Returning all data at once
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filepath}' doesn't exist!")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")
