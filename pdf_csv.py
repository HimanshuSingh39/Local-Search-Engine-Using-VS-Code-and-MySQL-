import fitz
import csv

def pdf_to_csv(input_path, output_path):
    doc = fitz.open(input_path)
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        headers_written = False  
        for page in doc:
            tables = page.find_tables()
            if tables:
                for idx, table in enumerate(tables):
                    table_data = table.extract()
                    if not headers_written:
                        csv_writer.writerows(table_data)
                        headers_written = True
                    else:
                        csv_writer.writerows(table_data[1:])
pdf_to_csv(r"C:\Users\1009s\Downloads\Flask_App_Demo-main\DCC ASSIGNMENT 4 FILE 1.pdf", 'csv1.csv')
pdf_to_csv(r"C:\Users\1009s\Downloads\Flask_App_Demo-main\DCC ASSIGNMENT 4 FILE 2.pdf", 'csv2.csv')