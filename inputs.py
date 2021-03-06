import os
import pandas as pd
from query_yes_no import query_yes_no
from reformating import reformat_excel_file


def ask_for_excel_file():
    yes_no = query_yes_no('Do you want to continue on an existing file? [yes/no]')
    if yes_no is True:
        excel_file_name = input('Enter the files name:')
        path = os.getcwd()
        excel_files_names = [f for f in os.listdir(path) if f.endswith('.xlsx')]
        if excel_file_name in excel_files_names:
            try:
                excel_file = pd.read_excel(r'' + path + '/' + excel_file_name, sheet_name=None)
                if excel_file is not None:
                    try:
                        parts_dict = reformat_excel_file(excel_file)
                        return parts_dict
                    except Exception as e:
                        raise ('Problem occurred while reformatting your xlsx file. \n'
                               'make sure the file was initially generated by this program.')
            except Exception as e:
                raise ('Error while reading your excel file' + e)
        else:
            os.error('No files of named' + excel_file_name + ' on that path' + path)
    else:
        excel_file = None
    return excel_file


def ask_for_urls():
    repeat = True
    urls = list()
    while repeat is True:
        urls.append(
            input('Enter a Digikey part url: '))  # TODO: make a function that is more robust then a simple input
        answer = query_yes_no('Do you want to enter another url? [yes/no]')
        if answer is True:
            continue
        else:
            repeat = False
    return urls
