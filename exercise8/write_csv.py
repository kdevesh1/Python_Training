#  creatre and Writing csv file in Python


from csv import writer 
with open('hello1.csv','w') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Devesh','India']) 
    csv_writer.writerow(['David','usa']) 
    
