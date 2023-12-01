import numpy as np

file_name = "detachment"
suffix = "depth"

simplices = np.loadtxt(f'../tri/fault_mesh_files/{file_name}_tri.txt', dtype="int", delimiter=",") - 1
xyz = np.loadtxt(f'../tri/fault_parm/{file_name}_nodes_loc.txt', dtype="float").round(3)

with open(f'../tri/gmt/{file_name}_{suffix}_gmt_tri.txt', 'w') as f:
    for i in range(len(simplices)):
        ind = simplices[i, :]
        string = str(simplices[i, :])[1:-1]
        f.write(f'> Polygon {string.replace(" ", "-")} -Z{-1*np.max([*xyz[ind[0]][2:3],*xyz[ind[1]][2:3], *xyz[ind[2]][2:3]])}\n')
        f.write(f'{str(xyz[ind[0]][0:2])[1:-1].strip()}\n')
        f.write(f'{str(xyz[ind[1]][0:2])[1:-1].strip()}\n')
        f.write(f'{str(xyz[ind[2]][0:2])[1:-1].strip()}\n')
        f.write(f'{str(xyz[ind[0]][0:2])[1:-1].strip()}\n')