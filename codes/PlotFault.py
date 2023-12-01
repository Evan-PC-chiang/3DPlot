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
        self.simplices = np.loadtxt(f'../tri/fault_mesh_files/{file_name}_tri.txt', dtype="int", delimiter=",") - 1
        self.xyz = np.loadtxt(f'../tri/fault_mesh_files/{file_name}_nodes.txt', dtype="float", delimiter=",")

        self.x = self.xyz[:, 0]
        self.y = self.xyz[:, 1]
        self.z = self.xyz[:, 2]

    def depth(self):
        """
        This function colored the fault plane with depth.
        :return: Mesh3D file in plotly.
        """
        surface = go.Mesh3d(x=self.x, y=self.y, z=self.z, i=self.simplices[:, 0], j=self.simplices[:, 1],
                            k=self.simplices[:, 2], intensity=self.z, coloraxis="coloraxis",
                            customdata=self.z,
                            hovertemplate=
                            f'Fault name: {self.file_name}' +
                            '<br>Depth:  %{customdata:.2f} Km<extra></extra>',
                            showlegend=False)
        return surface

    def tri(self, suffix):
        """
        This function plots the data of your suffix.
        :param suffix: "Ld" for locking, "SS" for strike slip, "DS" for Dip slip.
        :return: Mesh3D file in plotly.
        """
        if suffix == 'ld':
            text = '<br>Locking Ratio: %{customdata:.2f}<extra></extra>'
            ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        elif suffix == 'ss':
            text = '<br>Strike Slip:  %{customdata:.2f} mm/yr<extra></extra>'
            ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        elif suffix == 'ds':
            text = '<br>Dip Slip:  %{customdata:.2f} mm/yr<extra></extra>'
            ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        elif suffix == 'dir':
            text = '<br>Slip direction:  %{customdata:.2f}<extra></extra>'
            ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        else:
            text = '<br>Total Slip:  %{customdata:.2f} mm/yr<extra></extra>'
            ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        surface = go.Mesh3d(x=self.x, y=self.y, z=self.z, i=self.simplices[:, 0], j=self.simplices[:, 1],
                            k=self.simplices[:, 2], intensity=ld, intensitymode='cell', coloraxis="coloraxis",
                            customdata=ld,
                            hovertemplate=
                            f'Fault name: {self.file_name}' +
                            text,
                            showlegend=False)
        return surface

    def gmt_plot(self, suffix):
        ld = np.loadtxt(f'../tri/fault_parm/{self.file_name}_{suffix}.txt', dtype="float", delimiter=",")
        with open(f'../tri/gmt/{self.file_name}_{suffix}_gmt_tri.txt', 'w') as f:
            for i in range(len(self.simplices)):
                ind = self.simplices[i, :]
                string = str(self.simplices[i, :])[1:-1]
                f.write(f'> Polygon {string.replace(" ", "-")} -Z{round(ld[i].mean(),2)}\n')
                f.write(f'{str(self.xyz[ind[0]][0:2])[1:-1].strip()}\n')
                f.write(f'{str(self.xyz[ind[1]][0:2])[1:-1].strip()}\n')
                f.write(f'{str(self.xyz[ind[2]][0:2])[1:-1].strip()}\n')
                f.write(f'{str(self.xyz[ind[0]][0:2])[1:-1].strip()}\n')


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
                            ),
                            hoverinfo='skip')
        return line


class SetUp:
    """
    Set up the layout for plot.
    """
    def __init__(self, surface_list):
        self.surface_list = surface_list

    def reg(self, output_name):
        """
        This function makes every plot display the same content. I've set up the names and title of the figure.
        :param output_name: The name you want for HTML file.
        :return: A HTML file that is able to embed in html by <iframe>
        """
        if output_name == 'locking':
            colorscale = 'oranges'
            title = 'Locking <br> Ratio'
            minc = 0
            maxc = 1
            vals = [0, 0.25, 0.5, 0.75, 1]
            text = ['Creeping', '0.25', '0.5', '0.75', 'Locking']
        elif output_name == 'strike_slip':
            colorscale = 'Rdbu_r'
            title = 'Strike Slip <br> mm/yr'
            minc = -60
            maxc = 60
            vals = [-60, -50, -25, 0, 25, 50, 60]
            text = ['Left', '-50', '-25', '0', '25', '50', 'Right']
        elif output_name == 'dip_slip':
            colorscale = 'Rdbu_r'
            title = 'Dip Slip <br> mm/yr'
            minc = -60
            maxc = 60
            vals = [-60, -50, -25, 0, 25, 50, 60]
            text = ['Normal', '-50', '-25', '0', '25', '50', 'Reverse']
        elif output_name == 'detachment_tot':  # tot slip
            colorscale = 'GnBu'
            title = 'Total Slip <br> mm/yr'
            minc = 0
            maxc = 90
            vals = [0, 30, 60, 90]
            text = ['0', '30', '60', '90']
        else:  # dir
            colorscale = 'YlOrRd_r'
            title = 'Depth <br> Km'
            minc = -30
            maxc = 0
            vals = [-30, -15, 0]
            text = ['-30', '-15', '0']
        fig = go.Figure(data=self.surface_list)
        fig.update_layout(
            scene=dict(
                xaxis_title="X Axis",
                yaxis_title="Y Axis",
                zaxis_title="Z Axis",
                aspectmode="manual",
                aspectratio=dict(x=1, y=1, z=0.08),
                xaxis=dict(range=[-200, 300], showspikes=False),
                yaxis=dict(range=[-300, 200], showspikes=False),
                zaxis=dict(showspikes=False, showgrid=False)
            ),
            scene_camera=dict(eye=dict(x=0., y=-0.4, z=0.9)),
            width=580,
            height=580,
            coloraxis=dict(colorscale=f"{colorscale}",
                           colorbar_title=f"{title}",
                           cmin=minc, cmax=maxc,
                           colorbar=dict(orientation='h', y=-0.2,
                                         tickmode="array",
                                         tickvals=vals,
                                         ticktext=text,)),
        )
        fig.write_html(f"../html/{output_name}.html")

        return fig.show()
