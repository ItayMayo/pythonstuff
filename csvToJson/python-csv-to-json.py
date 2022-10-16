import csv
import json


def readCsv(path):
    csvDataList = []

    with open(path, newline='') as csvfile:
        parsedCsvFile = csv.DictReader(csvfile)
        for row in parsedCsvFile:
            csvDataList.append(row)

    return csvDataList


def storeListInJson(list, path):
    with open(path, "a") as file:
        json.dump(list, fp=file, indent=4)
        file.close


parsedData = readCsv("filename.csv")
storeListInJson(parsedData, "filename.json")
