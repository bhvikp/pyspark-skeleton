"""
    Main class script.
"""

__author__ = ['Bhavik Patel']
__version__ = "1.0.0"

from my_app.utils.spark_utils import get_spark_session
from my_app.utils.common import say_hello


class App:
    def __init__(self):
        self.spark = get_spark_session("hello-spark")

    def run(self):
        df = self.spark.range(100)
        print(df.collect())

        say_hello("Spark")
