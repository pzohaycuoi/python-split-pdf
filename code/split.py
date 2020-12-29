from PyPDF2 import PdfFileReader, PdfFileWriter
import os   

def split_at_every(infile , step, file_number):

    input_pdf = PdfFileReader(open(infile, "rb"))
    pdf_len = input_pdf.numPages
    page_numbers = list(range(0,pdf_len,step))

    for ind,val in enumerate(page_numbers):

        if(ind+1 != len(page_numbers)):
            output_1 = PdfFileWriter()

            for page in range(page_numbers[ind], page_numbers[ind+1]):
                file_number += (1 / step) #hmmmm dont know how to wisely explain this one...
                page_data = input_pdf.getPage(page)
                output_1.addPage(page_data)
                output_1_filename = '{}.pdf'.format(int(file_number)) #named file ascending order and parse float to int
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
                output_final_filename = '{}_page_{}.pdf'.format("Last", page + 1) #last file with number of the page
                print(output_final_filename)

            outputStream2 = open(output_final_filename, "wb")
            output_final.write(outputStream2)
            outputStream2.close()

