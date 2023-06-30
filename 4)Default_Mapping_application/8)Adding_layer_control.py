
import folium

import pandas 

data = pandas.read_csv("Volcanoes.csv")
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
fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    IFrame = folium.IFrame(html=html % str(el),width = 200,height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=folium.Popup(IFrame),
    fill_color=color_producer(el),color = 'grey',fill_opacity=0.7))
    
fgp = folium.FeatureGroup(name="Population")

#inorder for this code to work i need to add read() before 
# comma then this code will read the data. or else it will report cannot render objects with any missing geometries.
    
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    
map.add_child(fgv)
map.add_child(fgp)
#these are being added as new add child as they are not being read as seprate layer controls.
#this only shows everything as one layer control like population and volcanoes so you have to seprate the both and
# create them as feature groups and add child to them then they will be displayed in the layer control as options.
map.add_child(folium.LayerControl())
map.save("Map_layer_control.html")
