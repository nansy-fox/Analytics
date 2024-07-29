import matplotlib.figure
import pandas as pd
import csv
import matplotlib

fig = matplotlib.figure()
fields = []
df = []
limits = []
with open("C:/Users/molot/Desktop/Data_set_new.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        df.append(row)
        limits.append(row[3])

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

labels = ', '.join(field for field in fields)
print(labels, limits)
fig, ax = matplotlib.subplots(figsize=(0, 0))
w, t, a = ax.pie(limits, labels=labels)
