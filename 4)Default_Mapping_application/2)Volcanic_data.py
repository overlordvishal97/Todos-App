import folium
import pandas

#this 'data' can read both text file (or) Csv file.
data = pandas.read_csv("Volcanoes.csv") 
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Mymap")

#if you want to add multiple markers you have to use 'for' if you want to use only few statements rather than multiple statements.
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt, ln] ,popup=str(el)+" m", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html") 

#this code will display the locations of the volcanoes in the file as data on the map.
#now you just have to change the marker to show more info like dynamic information.
#if you get an error as get_name then convert the 'el' which is a float into a string as popup will only take a string.
