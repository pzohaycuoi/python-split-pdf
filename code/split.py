from PyPDF2 import PdfFileReader, PdfFileWriter
import os   

def split_at_every(infile , step):

    input_pdf = PdfFileReader(open(infile, "rb"))
    pdf_len = input_pdf.numPages
    fname = os.path.splitext(os.path.basename(infile))[0]
    tchNo = 736 #so thu chao hang cuoi cung la 423
    page_numbers = list(range(0,pdf_len,step))

    for ind,val in enumerate(page_numbers):

        if(ind+1 != len(page_numbers)):
            output_1 = PdfFileWriter()

            for page in range(page_numbers[ind], page_numbers[ind+1]):
                tchNo += 0.25 # 1 file pdf 4 trang 1-(0.25*4) = 0
                page_data = input_pdf.getPage(page)
                output_1.addPage(page_data)
                output_1_filename = '{}_{}.pdf'.format(int(tchNo), 20) #parse float sang int
                print(output_1_filename)

            outputStream1 = open(output_1_filename, "wb")
            output_1.write(outputStream1)
            outputStream1.close()
        else:
            output_final = PdfFileWriter()
            output_final_filename = "Last_Pages"

            for page in range(page_numbers[ind], pdf_len):
                page_data = input_pdf.getPage(page)
                output_final.addPage(page_data)
                output_final_filename = '{}_page_{}.pdf'.format(fname, page + 1) #file cuoi rename thu cong
                print(output_final_filename)

            outputStream2 = open(output_final_filename, "wb")
            output_final.write(outputStream2)
            outputStream2.close()

split_at_every("C:\Git-hub\python-split-pdf\Merged\merged_pdf.pdf", 4)