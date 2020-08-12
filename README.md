# airbnb-py-spark

This is mirror project of [airbnb-sc-spark](https://github.com/rkanniah/usermanagement-sc-backend), which reads & processes a csv file and then write into a PostgreSql database using Spark written in Python 3.7.x. The listing.csv file for the city of Paris, found in [Inside Airbnb](http://insideairbnb.com/get-the-data.html) website.

This publicly available file is provided by them under [Creative Commons CC0 1.0 Universal (CC0 1.0) "Public Domain Dedication"](https://creativecommons.org/publicdomain/zero/1.0/) license.

File table.sql contains the sql script for table creation that will be used for writing data into the PostgreSql database.

The build_run.sh is a utility script to install the package in ./venv which is the virtual environment directory and also to run the test. The final execution relies on the properties.json.

NOTE: The listings.csv file is huge.

Reference:
-------------
- [Guide to setup the virtual environment for Windows](https://www.c-sharpcorner.com/article/steps-to-set-up-a-virtual-environment-for-python-development/)
- [Guide to create a Open Source project](https://jacobtomlinson.dev/posts/2020/creating-an-open-source-python-project-from-scratch/)
- [Guide to use database with Spark](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html)
- [SO community guidance on jdbc driver](https://stackoverflow.com/questions/46925864/how-to-add-jdbc-drivers-to-classpath-when-using-pyspark)
- [Python guide on unit testing](https://docs.python.org/3/library/unittest.html)