import folium

map = folium.Map(location=[46.19,0.29], zoom_start=6)

fg = folium.FeatureGroup(name="myMap")
for coordinates in [[47.12, 0.45], [46.19, 0.29], [45.30, 0.59], [44.19, 0.62]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Marqueur", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("france_map.html")