import csv
import random
import re

def ReadData():
    print("Reading Data")
    FinalData = []
    ReturnData = []
    with open("Data.csv",mode='rt') as f:
        data = csv.reader(f)
        for row in data:
            if(str(row).find(",") != -1):
                l = str(row).split(',')
                a = re.findall("\d+\.\d",l[0])
                b = re.findall("\d+\.\d",l[1])
                k = [float(a[0]),float(b[0])]
                FinalData.append(k)
    print(FinalData)
    return(FinalData)

def WriteData(Feature_Length):
    with open("Data.csv",mode='w') as file:
        writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow([str(Feature_Length)])
        for i in range(Feature_Length):
            writer.writerow([str(random.random()*10),str(random.random()*10)])
    print("Data write succesful")

def main():
    k = input("Enter w to write data or r to read data:")
    if(k == "w"):
        WriteData(int(input("Enter feature length : ")))
    if(k == "r"):
        ReadData()
if __name__ == "__main__":
    main()    
