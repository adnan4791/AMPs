import os
import subprocess

os.environ['CILK_NWORKERS'] = '4'
nworkers = os.getenv('CILK_NWORKERS')

for x in range(10) :
    filename = "data_performance_core.txt"
    with open(filename,'a') as f:
        subprocess.run(["./benchmark",'1'],stdout=f,universal_newlines=True)

