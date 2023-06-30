#this will create a map with this code and only map and nothing else.using folium.
#but you have to add the coordinates of the location and save it by giving it a name.

import folium

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Mymap")

#if you want to add multiple markers you have to use 'for' if you want to use only few statements rather than multiple statements.
for coordinates in [[38.2,-99.1],[37.2,-97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html") 


