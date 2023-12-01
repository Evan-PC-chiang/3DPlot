# Model Result Visualization in an Interactive, Publication-quality Graph and Deploy through Reveal.js

## Introduction

As a researcher, delivering the results might be the most important thing in our life. How to visualize our result in a clear and understandable way is always a big issue in tectonic modeling. We compiled a 3-dimension fault geometry across Taiwan with 56 faults over 60K square kilometers. When plot it in a traditional way, all of the fault would just tangle togather and it's also hard to read the 3D plot in a 2D way. Here, I plot some interactive graphs for presentation purpose and plot some static graphs for paper purpose. 

We define our fault into several continuous triangular patches with radious of 5km and invert the surface deformation data for strike-slip, dip-slip and locking depth. For model simplicity, we assume the same slip rates on most of the faults. Several faults on the eastern Taiwan are allowed to aquire slip variation along strike. We also allow the detachment to change slip rates along strike and dip. For more model details, please visit [Johnson et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JB019672).

To make the best use of the interactive graphs, I also use reveal.js, a presentation software based on html and java script, to make slides thats able to embeded those interactive graphs. It's easy to manage and build by html elements and CSS. It's basically a power point in browser, means it could enbed interactive graphs just like a website. It can host by Github like as a github page, so it doesn't need any extra care about the compatibility between different computer as long as it is able to access the internet. It could export as a pdf file as well. 



https://github.com/Evan-PC-chiang/3DPlot

## Folder Structure

`Plot_maker.ipynb` is a jupyter notebook file combines 3 parts: `11Plot`, `build_figure`, `detachment_plot`,and `writeGMT`. 

Part 1: `11Plot` plots the 1 to 1 ratio figure between model prediction and data. Shows how well our model could predict.

Part 2: `build_figure` plots the interactive plot in html form. Those plots are able to rotate, zoom in, and show the informations of the fault when you hover on it.

Part 3: `detachment_plot` does the same thing with part2. Due to the different model setting in our model, this might not be the best way to show the slips on the detachment, therefore, we make a different plot for detachment in part 4.

Part 4: `writeGMT`. This script output GMT form files for GMT. 

 The functions are written in `PlotFault.py`. 

```plaintext
3DPlot/
├── Codes/
│   ├── PlotFault.py
│   ├── figure/
|   │   └── figures
│   └── Plot_maker.ipynb
|       ├── 11Plot
│       ├── build_figure
|       └── writeGMT
├── data/
│   └── #Our Model Outputs
├── pyGMT/
│   ├── GMT.ipynb # code for plotting
│   ├── cpt/
│   │   └── color scheme for GMT
│   ├── data/
│   │   └── data for plotting
│   ├── fig/
│   │   └── final figure
│   └── grd_data/
│       └── raster data for plotting
├── html/
│   └── #Plots in .html file
└── tri/
    ├── fault_mesh_files/
    │   └── #metadata for faults.
    ├── fault_parm/
    │   └── #Model outputs for parameters
    └── gmt/
        └── #Results from writeGMT.py for GMT plots
```



## Data Structure

```plaintext
└── tri/
    └── fault_mesh_files/
        ├── {fault_name}_nodes.txt
        └── {fault_name}_tri.txt
    └── fault_parm/
        ├── {fault_name}_ds.txt
        ├── {fault_name}_ss.txt
        └── {fault_name}_Ld.txt
```

### {fault_name}_nodes.txt

```
x1, y1, z1
x2, y2, z2
x3, y3, z3
```

The location in local coordinate of each point.

### {fault_name}_tri.txt

```
point_num, point_num, point_num
```

The connectivity of three point to form a triangle patch.

### fault_parm/{fault_name}_{fix}.txt

```
double
double
double
```

The slip/locking on each triangular patch.

## Project Timeline

- [x] (Sep 10) write code to aquire data from inversion model.
- [x] (Sep 14) write code for 3D interative graphs.
- [x] (Sep 20) set up the folder for data management.
- [x] (Sep 24) rewrite codes into several sub functions.
- [x] (Oct 01) set up the environment for reveals.js.
- [x] (Oct 05) test the reveal.js.
- [x] (Oct 11) finalizing the codes for interactive plots, including labels, view angles, and color bars.
- [x] (Oct 18) uplaod reveal.js project to Github to deploy the presentation.
- [x] (Oct 20) find a new way (GMT) to plot detachment contribution. 
- [x] (Oct 23) update presentation.
- [x] (Nov 20) Get pyGMT working.
- [x] (Nov 26) make static graphs for paper.
- [x] (Dec 01) Finishing up project, https://evan-pc-chiang.github.io/3D_Taiwan_model/
