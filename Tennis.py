import numpy as np
import pandas as pd
import xlsxwriter

class Tennis:
    def __init__(self, filename ='NOT_SPECIFIED'):
        #if filename is specified create a data-frame with that filename
        if not filename == 'NOT_SPECIFIED':
            try:
                self.data = pd.read_csv(filename)
                self.filename = filename
            except:
                print('could not open file')
                exit()
        #if no filename mentioned create a blank dataframe
        else:
            self.data = pd.DataFrame()
            self.filename = filename

    #overrides the '+' symbol for Tennis objects. Returns summation_result which is a Tennis object which contains data of object_2 appended to data of object_1
    def __add__(object_1, object_2):
        summation_result = Tennis()
        summation_result.data = object_1.data.append(object_2.data, ignore_index = True)
        return summation_result

    #writes the data frame to an excel file filename.xlsx (required). Optional argument is Sheet_name (default 'Sheet1')
    def write_to_excel(self, filename, sheet_name = 'Sheet1'):
        try:
            writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
            self.data.to_excel(writer, sheet_name = sheet_name)
            writer.save()
            self.filename = filename

        except:
            print('\nError in opening output file. Exiting')
            exit()



