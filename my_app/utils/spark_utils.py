"""
    This is common spark utils script.
"""

__author__ = ['Bhavik Patel']
__version__ = "1.0.0"

from pyspark.sql import SparkSession


def get_spark_session(app_name):
    """
    Function to get spark session

    :param app_name: spark app name
    :return: spark session
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

    return spark
