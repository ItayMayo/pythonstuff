import csv
import json


def readCsv(path):
    csvDataList = []

    try:
        with open(path, newline='') as csvfile:
            parsedCsvFile = csv.DictReader(csvfile)

            for row in parsedCsvFile:
                csvDataList.append(row)
    except FileNotFoundError:
        print('The requested file does not exist, check file path. File path: ' + path)

        return []

    return csvDataList


def storeListInJson(list, path):
    if (list is None or len(list) == 0):
        print('List is empty.')

        return

    try:
        with open(path, "a") as file:
            json.dump(list, fp=file, indent=4)
            file.close

    except Exception:
        print('An error occured while dumping list into json file. File path: ' + path)

        return


# parsedData = readCsv("filename.csv")
# storeListInJson(parsedData, "filename.json")
