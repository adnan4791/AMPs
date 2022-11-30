import subprocess

from itertools import product
performance = ['0','2','4','6'] #1
efficient = ['8','9','10','11','12','13','14','15'] #2
hybrid = ['0','2','4','6','8','9','10','11','12','13','14','15'] #3
smt = ['0','1','2','3','4','5','6','7'] #4
smt_pf = ['0','2','4','6','1','3','5','7'] #5
hybrid_smt = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'] #6
hybrid_smt_pf = ['0','2','4','6','8','9','10','11','12','13','14','15','1','3','5','7'] #7
mylist = [str(i) for i in range(1,len(hybrid_smt)+1)]
print(mylist)
for x,y in product(mylist,range(10)):
    filename = "omp_hybrid_smt.csv"
    print(x)
    with open(filename,'a') as f:
        subprocess.run(["./ompi", '6', x],stdout=f,universal_newlines=True)