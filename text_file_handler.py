from threading import Thread
import os

def get_file_object(filepath):
    """
    This function helps to open a text file and return its file object.
    :param filepath: path to the text file to be opened.
    :return (status, [fileobject or error])
    """
    try:
        return (True, open(filepath, 'r'))
    except Exception as e:
        return (False, e)

def read_chunk(fileobj, start, size, result, index):
    """
    Function to read a specific chunk of the file.
    :param fileobj: The file object to read from.
    :param start: The start position in the file to read.
    :param size: The size of the chunk to read.
    :param result: A list to store the read chunks.
    :param index: Index to store the chunk in the result list.
    """
    fileobj.seek(start)
    data = fileobj.read(size)
    result[index] = data

def read(fileobj, fast=False, threads=4, debug=False):
    if fast:
        fileobj.seek(0, os.SEEK_END)
        size = fileobj.tell()
        if debug:
            print(f"File size: {size} bytes")

        # Calculate the chunk sizes
        shares = []
        initShare = int(size / threads)
        expShare = size // threads
        for i in range(threads - 1):
            shares.append(initShare)
        shares.append(initShare + expShare)

        if debug:
            print(f"Shares: {shares}")

        # Prepare the list to store results
        result = [None] * threads

        # Create and start threads
        threads_list = []
        start_pos = 0
        for i in range(threads):
            t = Thread(target=read_chunk, args=(fileobj, start_pos, shares[i], result, i))
            threads_list.append(t)
            start_pos += shares[i]
            t.start()

        # Wait for all threads to finish
        for t in threads_list:
            t.join()

        # Combine the results
        combined_result = ''.join(result)

        if debug:
            print(
                f"Combined result (preview):\n{combined_result[:200]}...")  # Printing a preview of the combined result

        return combined_result
    else:
        fileobj.seek(0)
        data = fileobj.read()
        if debug:
            print(f"Complete file data:\n{data[:200]}...")  # Printing a preview of the file content
        return data

def read_to_list(fileobj, fast=False, threads=4, debug=False):
    """
    Reads the file and returns the result as a list of chunks.
    :param fileobj: The file object to read from.
    :param fast: Whether to read the file in chunks using multiple threads.
    :param threads: The number of threads to use for reading.
    :param debug: Whether to print debug information.
    :return: A list of chunks read from the file.
    """
    if fast:
        fileobj.seek(0, os.SEEK_END)
        size = fileobj.tell()
        if debug:
            print(f"File size: {size} bytes")

        # Calculate the chunk sizes
        shares = []
        initShare = int(size / threads)
        expShare = size // threads
        for i in range(threads - 1):
            shares.append(initShare)
        shares.append(initShare + expShare)

        if debug:
            print(f"Shares: {shares}")

        # Prepare the list to store results
        result = [None] * threads

        # Create and start threads
        threads_list = []
        start_pos = 0
        for i in range(threads):
            t = Thread(target=read_chunk, args=(fileobj, start_pos, shares[i], result, i))
            threads_list.append(t)
            start_pos += shares[i]
            t.start()

        # Wait for all threads to finish
        for t in threads_list:
            t.join()

        # Return the result as a list of chunks
        if debug:
            print(
                f"Chunks (first 3 previews):\n{[chunk[:200] for chunk in result[:3]]}")  # Preview of the first 3 chunks

        return result
    else:
        fileobj.seek(0)
        data = fileobj.read()
        if debug:
            print(f"Complete file data:\n{data[:200]}...")  # Printing a preview of the file content
        return [data]

def count_lines(fileobj):
    """
    Counts the number of lines in the file.
    :param fileobj: The file object to count lines from.
    :return: The number of lines in the file.
    """
    lines = 0
    for line in fileobj:
        lines += 1
    return lines

def find_word(fileobj, word):
    """
    Finds all the occurrences of a word in the file.
    :param fileobj: The file object to search in.
    :param word: The word to search for.
    :return: A list of line numbers where the word is found.
    """
    lines_found = []
    line_number = 1
    for line in fileobj:
        if word in line:
            lines_found.append(line_number)
        line_number += 1
    return lines_found


def get_file_info(filepath):
    """
    Retrieves basic information about a file, including its size, number of lines, and the first few lines.
    :param filepath: Path to the file.
    :return: A dictionary containing file information.
    """
    try:
        file_info = {}
        with open(filepath, 'r') as fileobj:
            # Get file size
            file_info['size'] = os.path.getsize(filepath)

            # Get line count
            file_info['lines'] = count_lines(fileobj)

            # Get first few lines
            fileobj.seek(0)
            file_info['first_lines'] = [fileobj.readline().strip() for _ in range(3)]

        return file_info
    except Exception as e:
        return {"error": str(e)}

def copy_file(src_filepath, dest_filepath):
    """
    Copies the content of one file to another.
    :param src_filepath: Path to the source file.
    :param dest_filepath: Path to the destination file.
    """
    try:
        with open(src_filepath, 'r') as src_file:
            with open(dest_filepath, 'w') as dest_file:
                dest_file.write(src_file.read())
        print(f"File copied from {src_filepath} to {dest_filepath}")
    except Exception as e:
        print(f"Error copying file: {str(e)}")

def get_file_lines(filepath):
    """
    Reads a file and returns its content as a list of lines.
    :param filepath: Path to the file.
    :return: A list of lines from the file.
    """
    try:
        with open(filepath, 'r') as fileobj:
            return fileobj.readlines()
    except Exception as e:
        return [f"Error reading file: {str(e)}"]


def write_lines(filepath, lines, append=False):
    """
    Writes a list of lines to a file.
    :param filepath: Path to the file.
    :param lines: List of strings (lines) to write.
    :param append: If True, it appends the lines to the file. If False, it overwrites the file.
    """
    mode = 'a' if append else 'w'
    try:
        with open(filepath, mode) as fileobj:
            fileobj.writelines(lines)
        print(f"Written {len(lines)} lines to {filepath}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

def merge_files(filepaths, output_filepath):
    """
    Merges multiple files into one file.
    :param filepaths: List of paths to the files to be merged.
    :param output_filepath: Path to the output merged file.
    """
    try:
        with open(output_filepath, 'w') as output_file:
            for filepath in filepaths:
                with open(filepath, 'r') as input_file:
                    output_file.write(input_file.read())
        print(f"Files merged into {output_filepath}")
    except Exception as e:
        print(f"Error merging files: {str(e)}")

def filter_lines(fileobj, condition):
    """
    Filters the lines of the file based on a given condition (e.g., contains a specific word).
    :param fileobj: The file object to read from.
    :param condition: A function that takes a line and returns True or False based on the condition.
    :return: A list of lines that meet the condition.
    """
    filtered_lines = []
    for line in fileobj:
        if condition(line):
            filtered_lines.append(line)
    return filtered_lines

def write_file(filepath, content):
    """
    Writes content to a file, overwriting any existing content.
    :param filepath: Path to the file.
    :param content: The content to write to the file.
    """
    try:
        with open(filepath, 'w') as fileobj:
            fileobj.write(content)
        print(f"File written: {filepath}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
