import gmplot
# google map api pricing: map lods 1000 -> 7$ (monthly 28500 free $200)

# apikey = '' # (your API key here)
# gmap = gmplot.GoogleMapPlotter(37.766956, -122.479481, 15, apikey=apikey)

Latitude = [6.9171, 6.9271, 6.9291, 6.9371]
Longitude = [79.8622, 79.8602, 79.8652, 79.8672]


# Initial map center point Latitude, Langitude the zoom level
gmapOne = gmplot.GoogleMapPlotter(7.2906, 80.6337, 7)

gmapOne.scatter(Latitude, Longitude, '#FF0000', size=40, marker=True)
gmapOne.plot(Latitude, Longitude, 'blue', edge_width=3.0)
gmapOne.draw("map.html")  # Name of the file that want to save
