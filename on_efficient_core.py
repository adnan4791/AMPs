import os
import subprocess

os.environ['CILK_NWORKERS'] = '8'
nworkers = os.getenv('CILK_NWORKERS')

for x in range(10) :
    filename = "data_efficient_core.txt"
    with open(filename,'a') as f:
        subprocess.run(["./benchmark",'2'],stdout=f,universal_newlines=True)

