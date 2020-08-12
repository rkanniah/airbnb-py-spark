#!/bin/sh

################################################
# A shell script to clean the previous install
# package and runs the program to read the csv
# file and writes back to the database.
################################################

#Assuming that we have a venv directory found in the
#directory where build_run.sh script is executed.
rm ./venv/Lib/site-packages/airbnb-0.0.1-py3.7.egg
rm ./venv/Scripts/airbnb-script.py
rm ./venv/Scripts/airbnb.exe
echo 'Done removing installed airbnb files'

#Run to install in the venv directory
python setup.py install
echo 'Done installing airbnb files'

#Run test
python setup.py test
echo 'Done running test for airbnb files'

clear

echo 'Running app by calling arbnb'
echo 'with parameter file properties.json'
airbnb properties.json
