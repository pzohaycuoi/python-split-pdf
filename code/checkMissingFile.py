from os import listdir

def checking_missing_file(file_path, smallest_file_number, largest_file_number):
    dirPath = listdir(file_path)

    correct_file_list = []

    for i in range(largest_file_number - smallest_file_number):
        correct_file_list.append("{}.pdf".format(i))
        i += 1

    check = tuple(set(correct_file_list) - set(dirPath))
    sort_check = sorted(check)

    print(sort_check)