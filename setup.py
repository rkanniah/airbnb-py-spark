from setuptools import setup, find_packages

setup(
    name="airbnb",
    version="0.0.1",
    description="Python Spark csv file processor",
    url="https://github.com/rkanniah/airbnb-py-spark",
    test_suite = "tests",
    packages=["airbnb_py_spark"],
    entry_points={"console_scripts": ["airbnb=airbnb_py_spark.airbnb_app:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    tests_require=["pytest"],
    install_requires=[
        "findspark",
        "pyspark"
    ],
    python_requires=">=3.7",
)