# some succinct code for opening a CSV file

with open('filename.csv','r') as f:
    data_csv = f.read()
data_csv = [line.split(',') for line in data_csv.split('\n')]

# this will give you a 2D list of rows/cells

# to turn this into a list of dictionaries
data = []
for i in range(1, len(data_csv)):
    line_dict = {}
    for j in range(0, len(data_csv)):
        line_dict[data_csv[0][j]] = data_csv[i][j]
    data.append(line_dict)

# or #
keys = data_csv[0]
data = []
for i,row in list(enumerate(data_csv))[1::]:
    line_dict = {}
    for j,cell in enumerate(row):
        line_dict[keys[j]] = cell
    data.append(line_dict)

