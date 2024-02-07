import csv
import json

"""
    > Author: Kgomotso Kgola 
    > Date: 20 November 2023
    > Version: 1.0.0
    > Description: This is a file converter program that simply convert a csv file to a json file
                 - The program only converts from csv to json, no any other extentions.
                 - The program only offers a foundation or blueprint you are free to use it any other way you see fit
        
"""

# Enter the name of the file you with to convert from
inputFileName = input("Enter csv file: ")
# find where the extension name start
x = inputFileName.find('.')    
# create an output name for the json file
outputFile = "Generated"+inputFileName[:x]+".json"

#create a list that will contain the dictionaries in a json file 
lst = []

# When a file is not in the directory or the user enters a wron spelling of the file name or the extension the error is catched 
try:
    # opens a csv file in a read mode and special characters are expected
    with open(inputFileName, 'r', encoding='utf-8', newline="") as csvFile:
        # create an enumerator to track the row number being read
        csvFileReader = enumerate(csv.reader(csvFile))
        ## create a list of keys which are simply column headers from the csv file
        keys = []
        # loops through a the csv file
        for i, row in csvFileReader: 
            # if it's first row or the coulumn headers
            if i == 0:
                for x in range(len(row)):
                    keys.append(row[x])
            # skips through a column header
            elif i > 0:
                dictionary = {} 
                for x in range(len(row)):
                    # adds entries to a dictionary
                    dictionary.setdefault(keys[x],row[x])
                lst.append(dictionary)

except FileNotFoundError:
    print("Please ensure that you entered the correct File name and the right extention name.")
                
with open(outputFile, 'w', encoding='utf-8', newline="") as jsonFile:
    json.dump(lst, jsonFile, ensure_ascii=False, indent = 2)

print("Done")