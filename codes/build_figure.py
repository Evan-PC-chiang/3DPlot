from PlotFault import Fault, Costal, SetUp
import plotly.graph_objects as go
import pandas as pd


costal_file = 'tri/ll_costal.txt'
line = Costal(costal_file).plot()

filenames = pd.read_table('tri/namelist.txt')
surface_list = [line]

for i in filenames.namelist:
    surface_list.append(Fault(i).tri("ld"))
    #surface_list.append(Fault(i).depth())
    #Fault(i).gmt_plot('Ld')


fig = go.Figure(data=surface_list)

SetUp(surface_list).reg("locking")
