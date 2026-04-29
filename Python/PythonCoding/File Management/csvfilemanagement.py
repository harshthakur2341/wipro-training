import csv
import os

'''empid, ename
101,AAA
102,BBB'''

def write_csv(filename):




def read_csv(filename):
    with open(filename,"r",newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print()



def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


filename="myfile.csv"
