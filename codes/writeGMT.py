import numpy as np


file_name = "CRF"
suffix = "Ld"

simplices = np.loadtxt(f'tri/fault_mesh_files/{file_name}_tri.txt', dtype="int", delimiter=",") - 1
xyz = np.loadtxt(f'tri/fault_mesh_files/{file_name}_nodes.txt', dtype="float", delimiter=",")
ld = np.loadtxt(f'tri/fault_parm/{file_name}_{suffix}.txt', dtype="float", delimiter=",")

with open(f'tri/gmt/{file_name}_{suffix}_gmt_tri.txt', 'w') as f:
    for i in range(len(simplices)):
        ind = simplices[i, :]
        string = str(simplices[i, :])[1:-1]
        f.write(f'> Polygon {string.replace(" ", "-")} -Z{ld[i]}\n')
        f.write(f'{str(xyz[ind[0]][0:2])[2:-2].strip()}\n')
        f.write(f'{str(xyz[ind[1]])[2:-2].strip()}\n')
        f.write(f'{str(xyz[ind[2]])[2:-2].strip()}\n')
        f.write(f'{str(xyz[ind[0]])[2:-2].strip()}\n')
