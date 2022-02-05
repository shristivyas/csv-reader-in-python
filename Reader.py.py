import csv
  
# csv file name
file =str(input("Enter fileanme : "))
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(file,encoding="utf8") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    x=csvreader.line_num
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\n rows are:\n')
for i in (rows[:x]):
    # parsing each column of a row
    for col in i:
        print("%1s"%col,end="  ")
    print('\n\n\n\n')