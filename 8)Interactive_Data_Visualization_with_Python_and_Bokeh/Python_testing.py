from bokeh.plotting import figure, output_file, show
import pandas
df=pandas.read_csv("adbe.csv",parse_dates=["Date"])
p=figure(plot_width=500, plot_height=250,x_axis_type="datetime",sizing_mode="sizing_both")
#responsive doesn't seem to be working so i used sizing mode=sizing both
p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)
output_file("Timeseries.html")
show(p)
