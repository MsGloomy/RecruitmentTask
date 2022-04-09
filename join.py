import csv
import sys
import pandas as pd

def join(join_type, column_name, file1, file2):
    file = open(file1)
    csvreader = csv.reader(file)
    header = next(csvreader)
    #check whether column_name is in header
    if column_name not in header:
        print("Given uncorrect column_name!")
        exit()

    index1 = int(find(column_name, header))

    #check whether index is a valid value
    if( index1 < 0 || index > len(headers)):
        print("Wrong index of column_name.")
        exit()

    A = []
    for row in csvreader:
        A.append(row)
    file.close()

    file = open(file2)
    csvreader = csv.reader(file)
    header2 = next(csvreader)
    #check whether column_name is in header
    if column_name not in header2:
        print("Given uncorrect column_name!")
        exit()

    index2 = int(find(column_name, header2))
    #check whether index is a valid value
    if( index2 < 0 || index2 > len(headers2)):
        print("Wrong index of column_name.")
        exit()

    B = []
    for row in csvreader:
        B.append(row)
    file.close()

    #decide what join_type will be used
    if join_type.lower() == "inner":
        data = inner_join(column_name, A, B, index1, index2)
    elif join_type.lower() == "left":
        data left_join(column_name, A, B, index1, index2)
    elif join_type.lower() == "right":
        data = right_join(column_name, A, B, index1, index2)
    else:
        return "Wrong value for join_type!"

    new_headers = headers + headers2
    new_data = pd.DataFrame(data, new_headers)
    print(new_data)

def inner_join( column_name, A, B, index1, index2):
    combined=[]
    for x in A:
        for y in B:
            if x[index1] == y[index2]:
                combined.append(x + y)
    return combined


def right_join( column_name, A, B ,index1, index2):
    combined=[]
    for y in B:
        for x in A:
            if x[index1] == y[index2]:
                combined.append(x + y)
            else:
                combined.append(['' for i in range(len(x))] + y)
                break
    return combined

def left_join( column_name, A, B, index1, index2 ):
    combined=[]
    for x in A:
        for y in B:
            if x[index1] == y[index2]:
                combined.append(x + y)
            else:
                combined.append(x + ['' for i in range(len(y))])
                break
    return combined

def find(column_name, header):
    for i in range(len(header)):
        if column_name == header[i]:
            return i
    #error value is -1
    return -1

if __name__ == "__main__":
    join_types = ["inner", "left", "right"]
    n_arg = len(sys.argv) - 1

    if( n_arg == 4 ):
        if sys.argv[1].lower() in join_types:
            join_type = sys.argv[1].lower()
        column_name = sys.argv[2]
        file1 = sys.argv[3]
        file2 = sys.argv[4]
        join(join_type, column_name, file1, file2)

    else:
        if( n_arg == 3 ):
            if( sys.argv[1] in join_types ):
                print("Given uncorrect arguments!")
                exit()
            else:
                join_type = "inner"
                column_name = sys.argv[1]
                file1 = sys.argv[2]
                file2 = sys.argv[3]
                join(join_type, column_name, file1, file2)
