import numpy as np
import pandas as pd
import os

os.chdir('../')
suffix = "Ld"

filenames = pd.read_table('tri/namelist.txt')


for i in filenames.namelist:
    file_name = i
    simplices = np.loadtxt(f'tri/fault_mesh_files/{file_name}_tri.txt', dtype="int", delimiter=",") - 1
    xyz = np.loadtxt(f'tri/fault_parm/{file_name}_nodes_loc.txt', dtype="float").round(3)
    ld = np.loadtxt(f'tri/fault_parm/{file_name}_{suffix}.txt', dtype="float", delimiter=",")

    with open(f'tri/gmt/{suffix}_gmt_tri.txt', 'w') as f:
        for i in range(len(simplices)):
            ind = simplices[i, :]
            string = str(simplices[i, :])[1:-1]
            f.write(f'> Polygon {file_name} {string.replace(" ", "-")} -Z{ld[i]}\n')
            f.write(f'{str(xyz[ind[0]][0:3])[1:-1].strip()}\n')
            f.write(f'{str(xyz[ind[1]][0:3])[1:-1].strip()}\n')
            f.write(f'{str(xyz[ind[2]][0:3])[1:-1].strip()}\n')
            f.write(f'{str(xyz[ind[0]][0:3])[1:-1].strip()}\n')
