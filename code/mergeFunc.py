from PyPDF2 import PdfFileMerger
from os import listdir


def merging_file(merge_path, merged_path):
    # convert path to the right absoulute path
    if merge_path.endswith('/'):
        input_dir = merge_path + '/'
    else:
        input_dir = merge_path + '//'

    # convert path to the right absoulute path
    if merged_path.endswith('/'):
        input_dir = merged_path + '/'
    else:
        input_dir = merged_path + '//'

    merge_list = []

    for x in listdir(input_dir):
        if not x.endswith('.pdf'):
            continue
        merge_list.append(input_dir + x)

    merger = PdfFileMerger()
    merge_list.sort(reverse=False)

    for pdf in merge_list:
        merger.append(pdf)
        print(pdf)

    merged_file_path = "{}/merged_pdf.pdf".format(merged_path)

    merger.write(merged_file_path)
    merger.close()
    print("merge completed")
