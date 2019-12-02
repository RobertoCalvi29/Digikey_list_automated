import xlsxwriter
from datetime import datetime
from progressbar import ProgressBar

from inputs import ask_for_urls, ask_for_excel_file
from scrape_digikey import find_part_infos


# Ask user for inputs
excel_file = ask_for_excel_file()
urls = ask_for_urls()

# Creating worksheet
workbook = xlsxwriter.Workbook('DigikeyList' + str(datetime.now()) + '.xlsx')
worksheet = workbook.add_worksheet()

# Templating
cell_format = workbook.add_format({'bold': True, 'underline': True})
currency_format = workbook.add_format({'num_format': '$#,##0.00'})
worksheet.write(0, 0, 'Part name', cell_format)
worksheet.write(0, 1, 'Digikey part number', cell_format)
worksheet.write(0, 2, 'Description', cell_format)
worksheet.write(0, 3, 'Unit', cell_format)
worksheet.write(0, 4, 'Price', cell_format)
worksheet.write(0, 5, 'Url', cell_format)

row = 1
if excel_file is not None:
    rows = len(excel_file['name']) + 1
    for row in range(1, rows):
        worksheet.write(row, 0, excel_file['name'][row-1])
        worksheet.write(row, 1, excel_file['digikey_part_number'][row-1])
        worksheet.write(row, 2, excel_file['description'][row-1])
        worksheet.write(row, 3, excel_file['unit'][row-1])
        worksheet.write(row, 4, excel_file['price'][row-1], currency_format)
        worksheet.write(row, 5, excel_file['url'][row-1])
    row += 1

pbar = ProgressBar()
for url in pbar(urls):
    part_infos = find_part_infos(url)
    worksheet.write(row, 0, part_infos['name'])
    worksheet.write(row, 1, part_infos['digikey_part_number'])
    worksheet.write(row, 2, part_infos['description'])
    worksheet.write(row, 3, part_infos['unit'])
    worksheet.write(row, 4, float(part_infos['price'][1:len(part_infos['price'])]), currency_format)
    worksheet.write(row, 5, part_infos['url'])

    row += 1

worksheet.write(row + 1, 0, 'Total')
worksheet.write(row + 1, 1, '=SUM(E2:E' + str(row) + ')', currency_format)

workbook.close()
