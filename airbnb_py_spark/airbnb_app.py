# These two lines should be written first before importing SparkSession
import findspark
findspark.init()

import json
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType, IntegerType, NullType
from pyspark.sql import SparkSession
from pyspark import SparkConf


def main():
    """
    The programs reads the listing.csv file and writes the result
    back to the PostgreSql database. The config file path for the
    program is supplied as argument.
    """
    import sys

    properties_filepath = sys.argv[1]
    print("properties_filepath argument: ", properties_filepath)

    #load the supplied properties.json file
    props = config_properties(properties_filepath)

    #Specify the jdbc database driver library to load
    conf = SparkConf()
    conf.set("spark.jars", props["database_driver_path"])

    #Get a Spark session and load the csv file
    mySpark = SparkSession.builder.config(
        conf=conf).appName("AirBnB").getOrCreate()
    csvFile = mySpark.read.csv(
        props["input_filePath"], header=True)

    #Get a database ready format
    dbDF = transformCsvToDbDataFile(csvFile)

    #write the data to the database table
    dbDF.write.mode(props["write_mode"])\
        .format("jdbc")\
        .option("driver", props["database_driver_class_name"])\
        .option("url", props["database_url"])\
        .option("dbtable", props["database_table"])\
        .option("user", props["database_user"])\
        .option("password", props["database_password"])\
        .save()

    mySpark.stop()

def config_properties(properties_filepath):
    """
    Read the properties file and return as dictionary.
    """
    f = open(properties_filepath, "r")
    config_properties = json.load(f)
    f.close()
    return config_properties

def transformCsvToDbDataFile(csvFile):
    """
    Prepare a suitable format to be saved into Postgres database.
    General rules are
    1. Look for minimum nights >= 5 & maximum nights <= 30
    2. Look amenities such as Wifi, TV, and Internet
    3. Replace the $ signs in price & weekly_price with empty string
    4. Convert minimum nights and maximum nights to Integer
    5. Convert price & weekly_price to Double
    6. When weekly_price is null then set it as 0
    """

    return csvFile.select("id", "listing_url", "amenities", "minimum_nights",
                          "maximum_nights", "price", "weekly_price", "city", "country")\
        .filter(csvFile["amenities"].contains("Internet"))\
        .filter(csvFile["amenities"].contains("Wifi"))\
        .filter(csvFile["amenities"].contains("TV"))\
        .filter(csvFile["price"].contains("$"))\
        .withColumn("id", csvFile["id"].cast(IntegerType()))\
        .withColumn("minimum_nights", csvFile["minimum_nights"].cast(IntegerType()))\
        .withColumn("maximum_nights", csvFile["maximum_nights"].cast(IntegerType()))\
        .withColumn("price", F.regexp_replace("price", "\\$", "").cast(DoubleType()))\
        .withColumn("weekly_price", F.when(F.isnull(csvFile["weekly_price"]), 0.0)
                    .otherwise(F.regexp_replace("weekly_price", "\\$", "").cast(DoubleType())))\
        .where(csvFile.colRegex("minimum_nights") >= 5)\
        .where(csvFile.colRegex("maximum_nights") <= 30)
