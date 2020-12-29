from os import listdir

def checking_missing_file(filePath, smallest_file_number, largest_file_number):
    dirPath = listdir(filePath)

    correct_file_list = []

    for i in range(largest_file_number - smallest_file_number):
        correct_file_list.append("{}.pdf".format(i))
        i += 1

    check = tuple(set(correct_file_list) - set(dirPath))
    sortCheck = sorted(check)

    print(sortCheck)