"""Splits column 4, which should be:

Re-annotated raw file name (username_date_PI_Country_cell/sample type_injectionID)

Into multiple columns:
- username_date_PI_Country_cell/sample type
- injectionID

that can be combined to generate a unique ID, but that can also be
used to identify replicate analysis of the same sample"""


import csv
import re


def main():
    column = 2
                    
    with open('cleanedTable.csv', 'rb') as csvin:
        with open('cleanedTable_id.csv', 'w') as csvout:
            reader = csv.reader(csvin)

            headers = next(reader)
            headers.append('Sample ID')
            headers.append('Replicate nr')
            headers.remove('AnnotatedFileName')
            writer = csv.writer(csvout, lineterminator='\n')
            
            all = []
            all.append(headers)
            
            for row in reader:
                a = re.split("_(\d*)$", row[column])
                row.append(a[0])
                row.append(a[1])
                del row[column]
                all.append(row)

            writer.writerows(all)

    
if __name__ == '__main__':
    main()
