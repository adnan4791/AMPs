import os
import subprocess

os.environ['CILK_NWORKERS'] = '16'
nworkers = os.getenv('CILK_NWORKERS')

for x in range(10) :
    filename = "data_hybrid_smt_core.txt"
    with open(filename,'a') as f:
        subprocess.run(["./benchmark",'5'],stdout=f,universal_newlines=True)

