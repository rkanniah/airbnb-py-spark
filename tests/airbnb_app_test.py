import unittest
import airbnb_py_spark.airbnb_app as F
import os

from pyspark.sql import SparkSession


class TestCsvFileTransformation(unittest.TestCase):

    def setUp(self):
        self.mySpark = SparkSession.builder.appName(
            "AirBnB_Test").getOrCreate()

    def test_transformCsvToDbDataFile_returns_two_records(self):

        csvFile = self.mySpark.read.csv(
            "./tests/test_listing.csv", header=True)

        dbDF = F.transformCsvToDbDataFile(csvFile)
        dbDF.show(10)

        self.assertTrue(dbDF.count() == 2)

    def tearDown(self):
        self.mySpark.stop()


if __name__ == '__main__':
    unittest.main()
