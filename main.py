import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

#plotly is same as matplotlib but with higher graphic standards

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


data = pd.read_csv("covid_data.csv") 

data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

data.columns = ("State","Country","Last Update","Lat","Long","Confirmed","Recovered", "Deaths", "Active")# renames columns

data["State"].fillna(value = " ", inplace = True)# fillna fills empty values automaticaly

top10_confirmed = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))

fig1 = px.scatter(top10_confirmed,x = top10_confirmed.index, y = "Confirmed", size = "Confirmed", size_max = 120, color = top10_confirmed.index, title = "Top 10 Countries by Confirmed cases")
fig1.write_html("Fig1.html", auto_open = True)#opens file in browser
