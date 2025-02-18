
# Text File Utility Documentation

## 1. `get_file_object(filepath)`
Opens a file and returns its file object.

### Parameters:
  - `filepath`: Path to the text file to be opened.

### Returns:
  - `(status, [fileobject or error])`: Returns a tuple where:
    - `status`: `True` if the file is opened successfully, `False` otherwise.
    - `fileobject`: The file object if the file is successfully opened.
    - `error`: The error message if the file could not be opened.

---

## 2. `read_chunk(fileobj, start, size, result, index)`
Reads a specific chunk of the file and stores it in the result list.

### Parameters:
  - `fileobj`: The file object to read from.
  - `start`: The start position in the file to read from.
  - `size`: The size of the chunk to read.
  - `result`: A list to store the read chunks.
  - `index`: The index where the chunk should be stored in the result list.

---

## 3. `read(fileobj, fast=False, threads=4, debug=False)`
Reads the file. Can read in chunks using multiple threads for faster reading.

### Parameters:
  - `fileobj`: The file object to read from.
  - `fast`: If `True`, the file is read in chunks using multiple threads. Defaults to `False`.
  - `threads`: The number of threads to use for reading. Defaults to 4.
  - `debug`: If `True`, debug information is printed. Defaults to `False`.

### Returns:
  - The combined result of the file read (either in chunks or the full content).

---

## 4. `read_to_list(fileobj, fast=False, threads=4, debug=False)`
Reads the file and returns the result as a list of chunks.

### Parameters:
  - `fileobj`: The file object to read from.
  - `fast`: If `True`, the file is read in chunks using multiple threads. Defaults to `False`.
  - `threads`: The number of threads to use for reading. Defaults to 4.
  - `debug`: If `True`, debug information is printed. Defaults to `False`.

### Returns:
  - A list of chunks read from the file.

---

## 5. `count_lines(fileobj)`
Counts the number of lines in the file.

### Parameters:
  - `fileobj`: The file object to count lines from.

### Returns:
  - The number of lines in the file.

---

## 6. `find_word(fileobj, word)`
Finds all the occurrences of a word in the file.

### Parameters:
  - `fileobj`: The file object to search in.
  - `word`: The word to search for.

### Returns:
  - A list of line numbers where the word is found.

---

## 7. `get_file_info(filepath)`
Retrieves basic information about a file, including its size, number of lines, and the first few lines.

### Parameters:
  - `filepath`: Path to the file.

### Returns:
  - A dictionary containing file information:
    - `size`: The size of the file.
    - `lines`: The number of lines in the file.
    - `first_lines`: The first 3 lines of the file.

---

## 8. `copy_file(src_filepath, dest_filepath)`
Copies the content of one file to another.

### Parameters:
  - `src_filepath`: Path to the source file.
  - `dest_filepath`: Path to the destination file.

---

## 9. `get_file_lines(filepath)`
Reads a file and returns its content as a list of lines.

### Parameters:
  - `filepath`: Path to the file.

### Returns:
  - A list of lines from the file.

---

## 10. `write_lines(filepath, lines, append=False)`
Writes a list of lines to a file.

### Parameters:
  - `filepath`: Path to the file.
  - `lines`: List of strings (lines) to write.
  - `append`: If `True`, it appends the lines to the file. If `False`, it overwrites the file.

---

## 11. `merge_files(filepaths, output_filepath)`
Merges multiple files into one file.

### Parameters:
  - `filepaths`: List of paths to the files to be merged.
  - `output_filepath`: Path to the output merged file.

---

## 12. `filter_lines(fileobj, condition)`
Filters the lines of the file based on a given condition (e.g., contains a specific word).

### Parameters:
  - `fileobj`: The file object to read from.
  - `condition`: A function that takes a line and returns `True` or `False` based on the condition.

### Returns:
  - A list of lines that meet the condition.

---

## 13. `write_file(filepath, content)`
Writes content to a file, overwriting any existing content.

### Parameters:
  - `filepath`: Path to the file.
  - `content`: The content to write to the file.
