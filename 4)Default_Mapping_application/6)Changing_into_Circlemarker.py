from branca.element import IFrame
import folium
from folium.map import FeatureGroup, Icon
import pandas 

data =pandas.read_csv("Volcanoes.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])

html = """<h4> Volcanic information :</h4>
Height:  %s m
""" 

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000>= elevation < 3000:
        return 'orange'
    else:
        return 'red' 
    
    
    
map=folium.Map(location=[38.9,-97.9], zoom_start=6, titles="Stamen Terrian")
fg=folium.FeatureGroup(name="mymap")
#to change the look of marker you just have to change the marker into circlemarker from folium.map .
#the circle has two sides inner and outer so fill in will be from color_producer and outer is set as grey.

for lt,ln,el in zip(lat,lon,elev):
    IFrame = folium.IFrame(html=html % str(el),width = 200,height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=folium.Popup(IFrame),
    fill_color=color_producer(el),color = 'grey',fill_opacity=0.7))
    
map.add_child(fg)
map.save("Map_circle_markers.html")
