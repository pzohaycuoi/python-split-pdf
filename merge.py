from PyPDF2 import PdfFileMerger
from os import listdir

input_dir = "C:\Git-hub\python-split-pdf\Base-file\\"

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

merger.write("C:\Git-hub\python-split-pdf\Merged\merged_pdf.pdf")
merger.close()