
# read the csv file using python

from csv import reader
with open('hello1.csv','r') as f:
    csv_reader = reader(f)
    print(csv_reader)
    for row in csv_reader:
        print(row)	

