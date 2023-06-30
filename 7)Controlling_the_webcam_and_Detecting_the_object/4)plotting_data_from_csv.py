from bokeh.core.property.color import Color
from bokeh.models.annotations import Title
from motion_detector import df 
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool,ColumnDataSource

#the columndatasource allows us to fetch the data from the column to display it on the plot.
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
#these two columns are made to display the datetime in correct format 
# and the variables are added into the hovertool tooltips.
cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100, width=500, sizing_mode='scale_width',title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker=[0,1]

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
#we should remove punctuations in the tooltips as bokeh is adding it by default.
p.add_tools(hover)
#ygrid is changed into yaxis for the code to work properly.
#responsive= True is changed to sizing_mode='scale_width' it is no longer supported.

q=p.quad(left="Start",right="End",bottom=0,top=1,fill_color="Green",source=cds)
#by adding the source you don't need to add df in the list.

output_file("Graph1.html")
show(p)