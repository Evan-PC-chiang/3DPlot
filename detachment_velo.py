from PlotFault import Fault, Costal, SetUp
import plotly.io as pio
pio.renderers.default = "browser"

costal_file = 'tri/ll_costal.txt'
surface_list = [Costal(costal_file).plot(), Fault('detachment').tri("tot_slip")]

SetUp(surface_list).reg("detachment_slip", 'RdBu_r', 'total slip')


