import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

data = pd.read_table(f'data/long_up.txt', delimiter=" ", names=["measurement", "model", "zone"], index_col=False)
fig = px.scatter(data, x="measurement", y="model", title="Long-term Vertical")
trace = px.line(x=[-15, 30], y=[-15, 30])
fig.add_trace(trace.data[0])
fig.update_traces(marker=dict(size=3,))
fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1)), margin=dict(l=20, r=20, t=40, b=20),)
fig.show()
fig.write_html(f"html/lt_up.html")