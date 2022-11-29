import subprocess

from itertools import product
performance = ['0','2','4','6']
efficient = ['8','9','10','11','12','13','14','15']
hybrid = ['0','2','4','6','8','9','10','11','12','13','14','15']
smt = ['0','1','2','3','4','5','6','7']
hybrid_smt = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
mylist = [str(i) for i in range(1,len(hybrid_smt)+1)]
print(mylist)
for x,y in product(mylist,range(10)):
    filename = "ompdata_hybrid_physical_fisrt.txt"
    print(x)
    with open(filename,'a') as f:
        subprocess.run(["./ompi_physical_first", '5', x],stdout=f,universal_newlines=True)