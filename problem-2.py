import os

def find_files(suffix, path):
    """
    Find all files beneath the specified path with a given file name suffix.

    This function searches through all directories and subdirectories under the specified path to find files with the specified suffix.

    Args:
      suffix (str): The suffix of the file name to be found. For example, if searching for text files, the suffix would be '.txt'.
      path (str): The path of the file system directory where the search will start.

    Returns:
      list: A list containing paths to all files found with the specified suffix. If no such files are found, an empty list is returned.
    
    Example:
    >>> find_files(".c", "./testdir")
    ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c']
    
    Notes:
    - The specified path may contain further subdirectories, and those subdirectories may also contain further subdirectories. There are no limits to the depth of subdirectories that can be searched.
    - If the specified path does not exist or is inaccessible, the function will return an empty list.
    - If the specified suffix is an empty string or None, the function will return None.
    """
    if suffix is None or suffix == "":
        return None
    
    if path is None:
        return []
        
    if not os.path.exists(path):
        return []

    file_paths = []

    def search_files(current_path):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            if os.path.isfile(item_path) and item.endswith(suffix):
                file_paths.append(item_path)
            elif os.path.isdir(item_path):
                search_files(item_path)

    search_files(path)
    return file_paths

# Test Case 1: Normal case with existing suffix in a deeper directory structure
# Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
print(find_files(".c", "./testdir"))

# Test Case 2: Edge case with empty suffix
# Expected output: None
print(find_files("", "./testdir"))

# Test Case 3: Edge case with null path
# Expected output: []
print(find_files(".c", None))

# Test Case 4: Normal case with existing suffix in a directory containing only non-matching files
# Expected output: []
print(find_files(".c", "./testdir/subdir4"))


