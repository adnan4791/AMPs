import csv
import math
from matplotlib import pyplot as plt
option = 0
filename = []
filename.append("cilk_performance_core.csv")
filename.append("cilk_efficient_core.csv")
filename.append("cilk_hybrid.csv")
filename.append("cilk_smt.csv")
filename.append("cilk_smt_pf.csv")
filename.append("cilk_hybrid_smt.csv")
filename.append("cilk_hybrid_smt_pf.csv")
nthread = [4,8,12,8,8,16,16];
file = open(filename[option],'r')
#data = list(csv.DictReader(file,delimiter=','))
data = list(csv.reader(file,delimiter=','))
file.close()
seq_exec_time = [1.9769,5.027873,1.9769,1.9769,1.9769,1.9769,1.9769]
new_data = []
all_data = []
#new_data.append(["nthreads","execution time"])
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)
option = 1
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)


option = 2
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)

option = 3
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)

option = 4
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)

option = 5
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)

option = 6
new_data=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
for i in range(0,nthread[option]*10,10):
    minval = min([row[1] for row in data[i:i+10]])
    new_data.append([math.floor(i/10+1),seq_exec_time[option]/float(minval)])
all_data.append(new_data)

plot_data = []
#print(plot_data_x)
for i in range(7):
    plot_data_x = [i for i in range(len(all_data[i]))]
    for plot_data_y in all_data[i]:
        print(plot_data_y[1])
                #plt.plot(plot_data_x,plot_data_y)

    