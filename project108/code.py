import pandas as pd
import plotly.figure_factory as pff

df=pd.read_csv("data(p108).csv")
fig=pff.create_distplot([df["AvgRating"].tolist()], ["ratings"], show_hist=False)
fig.show()