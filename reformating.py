def reformat_excel_file(excel_file):
    sheet = excel_file['Sheet1']

    names = list()
    units = list()
    prices = list()
    descriptions = list()
    digikey_part_numbers = list()
    urls = list()

    for elem in range(0, len(sheet) - 2):
        names.append(sheet['Part name'][elem])
        units.append(sheet['Unit'][elem])
        prices.append(sheet['Price'][elem])
        descriptions.append(sheet['Description'][elem])
        digikey_part_numbers.append(sheet['Digikey part number'][elem])
        urls.append(sheet['Url'][elem])

    part_info = {'name': names, 'unit': units, 'price': prices,
                 'description': descriptions, 'digikey_part_number': digikey_part_numbers, 'url': urls}

    return part_info
