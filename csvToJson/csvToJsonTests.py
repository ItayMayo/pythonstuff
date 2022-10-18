from json import JSONDecodeError
from csvToJson.csvToJson import *
import unittest
import sys
import io

class TestCsvToJson(unittest.TestCase):
    def test1_readCsv_returnsEntriesArray_testcsv(self):
        # Arrange
        filepath = "csvToJson/testcsv.csv"

        # Act
        result = readCsv(filepath)

        # Assert
        self.assertNotEqual(result, [])

    def test2_readCsv_invalidfile_test2csv(self):
        # Arrange
        filepath = "csvToJson/test2.csv"

        # Act
        result = readCsv(filepath)

        # Assert
        self.assertEqual(result, [])

    def test3_readCsv_invalidfilepath(self):
        # Arrange
        filepath = "sdgsjghouwhto234jhorth3409gj42prfhPH#*)H$%H*40#()(u432984yh208)#($*)#U%_(!#$*(U!%*)Y&(^"

        # Act
        result = readCsv(filepath)

        # Assert
        self.assertEqual(result, [])

    def test4_readCsv_returnsListOfDictionaries_testcsv(self):
        # Arrange
        filepath = "csvToJson/testcsv.csv"

        # Act
        result = readCsv(filepath)

        # Assert
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)

    def test5_storeListInJson_handlesDecodeException_testcsv(self):
        # Arrange
        filepath = "csvToJson/testcsv.csv"
        outpath = ""
        csvList = readCsv(filepath)

        # Act
        try:
            storeListInJson(csvList, outpath)

        # Assert
        except Exception:
            self.fail("storeListInJson raised an exception.")

    def test6_storeListInJson_emptyList(self):
        # Arrange
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        outpath = "csvToJson/test.json"
        emptyList = None

        # Act
        storeListInJson(emptyList, outpath)

        # Assert
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "List is empty.\n")