import subprocess
from itertools import product

for x,y in product(['8','4','2','1'],range(10)) :
    filename = "serial_performance_core"
    with open(filename,'a') as f:
        subprocess.run(["./pi_on_performance",x],stdout=f,universal_newline=true)
