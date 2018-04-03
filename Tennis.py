import numpy as np
import pandas as pd
import xlsxwriter
import os
import glob
import matplotlib.pyplot as plotter

class Tennis:
    def __init__(self, path='NOT_SPECIFIED'):
        #if path is specified create a data-frame with that filename
        if not path == 'NOT_SPECIFIED':

            #if path refers to a filepath
            if os.path.isfile(path):
                try:
                    self.data = pd.read_csv(path)
                    self.path = path
                except:
                    print('could not open file')
                    exit()

            #if filename refers to a whole directory, then it reads all csv files in that directory and writes to data-frame
            elif os.path.isdir(path):
                temporary_variable = Tennis()
                for filename in glob.glob(os.path.join(path, '*.csv')):
                    temporary_variable = temporary_variable + Tennis(path = filename)
                self.data = temporary_variable.data
                self.path = path


        #if no filename mentioned create a blank data-frame
        else:
            self.data = pd.DataFrame()
            self.path= path

    #overrides the '+' symbol for Tennis objects. Returns summation_result which is a Tennis object which contains data of object_2 appended to data of object_1
    def __add__(object_1, object_2):
        summation_result = Tennis()
        summation_result.data = object_1.data.append(object_2.data, ignore_index = True)
        return summation_result

    #writes the data frame to an excel file filename.xlsx (required). Optional argument is Sheet_name (default 'Sheet1')
    def write_to_excel(self, filename, sheet_name = 'Sheet1'):
        if not filename.split('.')[1] == 'xlsx':
            print("OUTPUT FILE DOES NOT HAVE .xlsx EXTENSION ")
            exit()
        try:
            writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
            self.data.to_excel(writer, sheet_name = sheet_name)
            writer.save()
            self.path = filename

        except:
            print('\nError in opening output file. Exiting')
            exit()

    #set the data attribute
    def set_data(self, data_frame):
        self.data = data_frame

    #filter the self object to return a df containing just the rows which have column_name == [value1, value2..]. column_name, [list_of_values].
    def select_rows(self, column_name, list_of_values):
        dummy_df = pd.DataFrame()
        if column_name not in self.data.columns:
            print('No such columns. Exiting')
            exit(-1)
        else:
            for i in range (len(list_of_values)):
                dummy_df = dummy_df.append(self.data[self.data.eval(column_name) == list_of_values[i]])
        return dummy_df

        # filter the self object to return a df containing just the rows which have column_name != [value1, value2..]. column_name, [list_of_values].
    def disselect_rows(self, column_name, list_of_values):
        dummy_df = pd.DataFrame()
        if column_name not in self.data.columns:
            print('No such columns. Exiting')
            exit(-1)
        else:
            for i in range(len(list_of_values)):
                dummy_df = dummy_df.append(self.data[self.data.eval(column_name) != list_of_values[i]])
        return dummy_df









    #plots a scatter plot between factor_y (y -axis) and factor_x (x-axis)
    #def two_factor_plots(self, factor_y, factor_x):
     #   plotter.scatter()



