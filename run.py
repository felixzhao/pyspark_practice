"""run.py"""
from os import environ
from pyspark import SparkContext

logFile = environ['SPARK_HOME'] + "/README.md"
sc = SparkContext("local", "Simple APP")
logData = sc.textFile(logFile).cache()

def func1(num):
    return num * 2

print(func1(2))
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a:%i, lines with b: %i" % (numAs, numBs))