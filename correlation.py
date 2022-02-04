from fileinput import filename
from statistics import correlation
import plotly.express as px
import csv
import numpy as np

def getdata(datafile):
    icecream=[]
    coldrink=[]
    with open(datafile) as c:
        df=csv.DictReader(c)
        for row in df :
            icecream.append(float(row["Coffee"]))
            coldrink.append(float(row["sleep"]))
    return {"x":icecream,"y":coldrink}

def findcorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"])
    print("Corelation beetween temprature and cold drink sale is= ",correlation[0,1])

def main():
    filename="data2.csv"
    datasource=getdata(filename)
    findcorrelation(datasource)
main()
    
