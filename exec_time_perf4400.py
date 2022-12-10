#eksperimen dilakukan dengan setting cpupower performance
#kabel adaptor terpasang
#
import csv
import math
from matplotlib import pyplot as plt

filename = []
filename.append("cilk_performance4400.csv")
filename.append("cilk_efficient4400.csv")
filename.append("cilk_hybrid4400.csv")
filename.append("cilk_smt4400.csv")
filename.append("cilk_smt_pf4400.csv")
filename.append("cilk_hybrid_smt4400.csv")
filename.append("cilk_hybrid_smt_pf4400.csv")
nthread = [4,8,12,8,8,16,16]
seq_exec_time = [1.9769,5.027873,1.9769,1.9769,1.9769,1.9769,1.9769]
new_data_y = []
new_data_x = []
all_data = []
all_x = []
option = 0
file = open(filename[option],'r')
#data = list(csv.DictReader(file,delimiter=','))
data = list(csv.reader(file,delimiter=','))
file.close()

new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

option = 1
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)


option = 2
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

option = 3
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

option = 4
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

option = 5
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

option = 6
new_data_y=[]
file = open(filename[option],'r')
data = list(csv.reader(file,delimiter=','))
file.close()
new_data_x = [i for i in range(1,nthread[option]+1)]
all_x.append(new_data_x)
print(all_x)
for i in range(0,nthread[option]*8,8):
    minval = min([row[1] for row in data[i:i+8]])
    new_data_y.append(float(minval))
all_data.append(new_data_y)

plt.style.use('grayscale')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(all_x[0],all_data[0],"<",label='cilk_performance_core')
ax.plot(all_x[1],all_data[1],"2-.",label='cilk_efficient_core')
ax.plot(all_x[2],all_data[2],">",label='cilk_hybrid_mode')
ax.plot(all_x[3],all_data[3],"d",label='cilk_smt_mode')
ax.plot(all_x[4],all_data[4],"+--",label='cilk_smt_pf_mode')
ax.plot(all_x[5],all_data[5],"x",label='cilk_hybrid_smt_mode')
ax.plot(all_x[6],all_data[6],"-.",label='cilk_hybrid_pf_mode')
ax.legend()
ax.set_xlabel('number of threads')
ax.set_ylabel('execution time [Seconds]')
plt.show()
