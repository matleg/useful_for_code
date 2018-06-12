"""example from sametmax"""

def read_large_file(file_object):
    """
    Uses a generator to read a large file lazily
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


def process_file(path):
    """process large file without taking all memory"""
    try:
        file_cleaned = open("report_differences_cleaned.txt", 'w')
        with open(path) as file_handler:
            for line in read_large_file(file_handler):
                # process line
                if ".pyc" not in line and ".git" not in line:
                    file_cleaned.write(line)
        file_cleaned.close()
    except (IOError, OSError):
        print("Error opening / processing file")


process_file("C:\\Users\\mat\\Documents\\report_differences.txt")
