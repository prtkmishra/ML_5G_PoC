""" Plot Data from input file """

import matplotlib.pyplot as plt
import csv
import seaborn as sns
x       = []
y       = []
input   = ""
class PlotData:

    """ initialize """
    def __init__(self, input):
        self.input = input
    
    def graph(self):
        """ plotting function """
        with open(self.input,'r') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            for row in data:
                x.append(float(row[0]))
                y.append(float(row[1])) 

        # print(x)
        # print(y)
        # sns.set(style="darkgrid")
        # sns.relplot(x=x,y=y)
        plt.scatter(x,y, s=20)
        plt.xlabel('Population')
        plt.ylabel('Profit')
        plt.title('Housing profit')
        plt.legend()
        plt.show()