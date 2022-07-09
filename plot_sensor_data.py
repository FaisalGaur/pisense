
import pandas as pd
import glob
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

path = r'D:\sense_data'
all_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files))

# Create figure
fig = make_subplots(rows=2, cols=3,  subplot_titles=('Temperature',  'Pressure', 'Humidity',
                                                     'Accelerometer', 'Compass', 'Orientation'))

columns = []
col_list = list(df)

# Loop df columns and plot columns to the figure
for i in range(6, 9):
    col_name = col_list[i]
    fig.add_trace(go.Scatter(x=df['datetime'], y=df[col_name], mode='lines', name=col_name), row=2, col=1)

for i in range(3, 6):
    col_name = col_list[i]
    fig.add_trace(go.Scatter(x=df['datetime'], y=df[col_name], mode='lines', name=col_name), row=2, col=2)

for i in range(9, 12):
    col_name = col_list[i]
    fig.add_trace(go.Scatter(x=df['datetime'], y=df[col_name], mode='markers', name=col_name), row=2, col=3)

fig.add_trace(go.Scatter(x=df['datetime'], y=df['temp'], mode='markers', name='temperature'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['datetime'], y=df['pres'], mode='markers', name='pressure'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['datetime'], y=df['hum'], mode='markers', name='humidity'), row=1, col=3)

fig.show()
