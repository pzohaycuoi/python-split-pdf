from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def split_at_every(source_file, output_file_path, file_number_int, file_step_int, sorting):

    input_pdf = PdfFileReader(open(source_file, "rb"))
    pdf_len = input_pdf.numPages
    page_numbers = list(range(0, pdf_len, file_step_int))

    for ind, val in enumerate(page_numbers):

        if(ind+1 != len(page_numbers)):
            output_1 = PdfFileWriter()

            for page in range(page_numbers[ind], page_numbers[ind+1]):

                if sorting[0] == True:
                    file_number_int += (1 / file_step_int)

                if sorting[1] == True:
                    file_number_int -= (1 / file_step_int)

                page_data = input_pdf.getPage(page)
                output_1.addPage(page_data)
                output_1_filename = '{}_{}.pdf'.format(
                    output_file_path, int(file_number_int))
                print(output_1_filename)

            output_stream1 = open(output_1_filename, "wb")
            output_1.write(output_stream1)
            output_stream1.close()
        else:
            output_final = PdfFileWriter()
            output_final_filename = "Last_Pages"

            for page in range(page_numbers[ind], pdf_len):
                page_data = input_pdf.getPage(page)
                output_final.addPage(page_data)
                output_final_filename = '{}_lastpage_{}.pdf'.format(output_file_path, page + 1)
                print(output_final_filename)

            outputStream2 = open(output_final_filename, "wb")
            output_final.write(outputStream2)
            outputStream2.close()
