import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.cluster import AgglomerativeClustering


def importTextFile( fileName: str):
    fileObject = open(fileName, "r") # opens file in "r"ead mode
    datapoints = fileObject.read().splitlines()
    fileObject.close()
    return datapoints


def datapointFormat(datapoints: list):
    xArr = []
    yArr = []
    for point in datapoints:
        x, y = point.split(" ")
        xArr.append(float(x))
        yArr.append(float(y))

    return xArr, yArr



datapoints = importTextFile("A.txt")
xArr, yArr = datapointFormat(datapoints)
# plt.scatter(xArr, yArr, label = 'True Position' )
# plt.show()

plt.show()