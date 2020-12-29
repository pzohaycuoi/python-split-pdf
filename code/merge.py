from PyPDF2 import PdfFileMerger
from os import listdir


#put this here to test
print("input file to merge path here: ")
mergePath = str(input())
print("input merged file path here: ")
mergedPath = str(input())


def merging_file(mergePath, mergedPath):    
    #convert path to the right absoulute path
    if mergePath.endswith('/'):
        input_dir = mergePath + '/'
    else:
        input_dir = mergePath + '//'

    #convert path to the right absoulute path
    if mergedPath.endswith('/'):
        input_dir = mergedPath + '/'
    else:
        input_dir = mergedPath + '//'

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

    merged_file_path = "{}/merged_pdf.pdf".format(mergedPath)

    merger.write(merged_file_path)
    merger.close()
    print("merge completed")