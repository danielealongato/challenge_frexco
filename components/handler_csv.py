import csv
import re
import os
from datetime import datetime

today = datetime.today().strftime('%d_%m_%Y %H_%M')
name_file = 'files\produtos_frexco_de_' + today + '.csv'

class HandlerFile:

    def inserting_data(self, data):
        with open(name_file, 'w') as file_csv:
            writer = csv.writer(file_csv, delimiter=',')
            writer.writerow(data)