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

top10_recovered = pd.DataFrame(data.groupby("Country")["Recovered"].sum().nlargest(10).sort_values(ascending=False))
fig2 = px.scatter(top10_recovered,x=top10_recovered.index, y="Recovered", size= "Recovered", size_max= 120,color=top10_recovered.index, title="Top 10 Countries by Recovered Cases")
fig2.write_html("Fig2_html", auto_open = True)

top10_deaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
fig3 = px.scatter(top10_deaths,x = top10_deaths.index,y="Deaths",size="Deaths", size_max=120,color=top10_deaths.index,title="Top 10 Countries by Deaths")
fig3.write_html("Fig3_html", auto_open = True)

top10_active = pd.DataFrame(data.groupby("Country")["Active"].sum().nlargest(10).sort_values(ascending=False))
fig4 = px.scatter(top10_active, x=top10_deaths.index,y= "Active",size="Active",size_max=120,color=top10_active.index,title="Top 10 Countries by Active Cases" )
fig4.write_html("Fig3_html",auto_open = True)

top10_death = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
fig5 = px.bar(top10_death,x = "Deaths", y = top10_death.index, height=600,color = "Deaths" , orientation="h",color_continuous_scale=["deepskyblue","red"], title="Top 10 Death Cases Counties")
fig5.write_html("Fig5.html", auto_open = True)


























