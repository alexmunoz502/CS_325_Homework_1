import file_handler
import algorithms

# CONSTANTS
FILE_PATH = "data.txt"
INSERT_OUT_PATH = "insert.out"
MERGE_OUT_PATH = "merge.out"


data_list = file_handler.read_data_from_file(FILE_PATH)
for number_list in data_list:
    algorithms.insertion_sort(number_list)

file_handler.write_data_to_file(data_list, INSERT_OUT_PATH)


# TODO: Add merge sort algorithm