#Justpy is created using quaser framework.
from os import listdir
from ssl import Options
import justpy as jp
from pandas.core.dtypes.common import classes
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data=pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Day']=data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()


#you can check styles of quaser in google.
#inverted: false makes x to y and y to x.

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
#now the chart_def is a string but with justpy the python will convert into dictionary.


def app():
    wp=jp.QuasarPage()
    #text-h1 makes the text large and text-center moves the text to center.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis",classes="text-h4 text-left")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Day"
    #now the data won't be simple in the real life so we use zip object to convert them.
    hc.options.xAxis.categories = list(day_average.index)  
    hc.options.series[0].data = list(day_average['Rating'])
    #for simple things you can change values in the chart_def
    #but u can't change the data because the dictionary can't hold the values.
   
    
    return wp

jp.justpy(app)