import numpy as np
import plotly.graph_objects as go


class Fault:
    def __init__(self, file_name):
        """
        This Class loads in the fault information for plotting a Mesh3D fault trace.
        Use Fault("file_name").depth() to plot fault depth.
        Use Fault("file_name").tri("suffix") to plot data you like to plot. (Same as trisurf(matlab))
        :param file_name: String, for fault name.
        """
        self.file_name = str(file_name)
        self.simplices = np.loadtxt(f'tri/fault_mesh_files/{file_name}_tri.txt', dtype="int", delimiter=",") - 1
        xyz = np.loadtxt(f'tri/fault_mesh_files/{file_name}_nodes.txt', dtype="float", delimiter=",")

        self.x = xyz[:, 0]
        self.y = xyz[:, 1]
        self.z = xyz[:, 2]

    def depth(self):
        """
        This function colored the fault plane with depth.
        :return: Mesh3D file in plotly.
        """
        surface = go.Mesh3d(x=self.x, y=self.y, z=self.z, i=self.simplices[:, 0], j=self.simplices[:, 1],
                            k=self.simplices[:, 2], intensity=self.z, coloraxis="coloraxis")
        return surface

    def tri(self, suffix):
        """
        This function plots the data of your suffix.
        :param suffix: "Ld" for locking, "SS" for strike slip, "DS" for Dip slip.
        :return: Mesh3D file in plotly.
        """
        ld = np.loadtxt(f'tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        surface = go.Mesh3d(x=self.x, y=self.y, z=self.z, i=self.simplices[:, 0], j=self.simplices[:, 1],
                            k=self.simplices[:, 2], intensity=ld, intensitymode='cell', coloraxis="coloraxis")
        return surface


class Costal:
    def __init__(self, costal_file):
        """
        This function helps you plot coastal line in plot.
        Function: Costal("costal_file").plot()
        :param costal_file: STR
        """
        self.costal_file = costal_file

    def plot(self):
        """
        Plot the costal line.
        :return: line in plotly.
        """
        costal = np.loadtxt(f'{self.costal_file}', dtype="float", delimiter=",")
        line = go.Scatter3d(x=costal[:, 0], y=costal[:, 1], z=costal[:, 2], line=dict(
            color='black',
            width=1,
        ),
                            marker=dict(
                                size=1,
                            ))
        return line


class SetUp:
    """
    Set up the layout for plot.
    """
    def __init__(self, surface_list):
        self.surface_list = surface_list

    def reg(self, output_name, colorscale, title):
        """
        This function makes every plot display the same content.
        :param output_name: The name you want for HTML file.
        :param colorscale: the colorscale form plotly I use "oranges" for locking, "GnBu_r" for depth, "RdBu" for slip
        rates.
        :param title: The title on colorbar. I use "Ratio" for locking, "mm/yr" for slip rates.
        :return: A HTML file that is able to embed in html by <iframe>
        """
        fig = go.Figure(data=self.surface_list)
        fig.update_layout(
            scene=dict(
                xaxis_title="X Axis",
                yaxis_title="Y Axis",
                zaxis_title="Z Axis",
                aspectmode="data",
                xaxis=dict(range=[-200, 300]),
                yaxis=dict(range=[-300, 200])
            ),
            scene_camera=dict(eye=dict(x=0., y=-1.2, z=2.5)),
            width=580,
            height=580,
            coloraxis=dict(colorscale=f"{colorscale}",
                           colorbar_title=f"{title}", )
        )

        return fig.write_html(f"html/{output_name}.html")
