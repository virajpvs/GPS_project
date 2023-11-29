import gmplot
import csv
# google map api pricing: map lods 1000 -> 7$ (monthly 28500 free $200)

# apikey = '' # (your API key here)
# gmap = gmplot.GoogleMapPlotter(37.766956, -122.479481, 15, apikey=apikey)

# Specify the CSV file path
csv_file_path = 'coordinates.csv'

# Lists to store Latitude and Longitude data
Latitude = []
Longitude = []

# Read data from CSV file
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Read the header
    header = next(csv_reader)

    # Read data row by row
    for row in csv_reader:
        # Assuming the first column is Latitude and the second column is Longitude
        lat, lon = map(float, row)
        Latitude.append(lat)
        Longitude.append(lon)

# Print the read data
print('Latitude:', Latitude)
print('Longitude:', Longitude)

# Initial map center point Latitude, Langitude the zoom level
gmapOne = gmplot.GoogleMapPlotter(7.2906, 80.6337, 7)

gmapOne.scatter(Latitude, Longitude, '#FF0000', size=40, marker=True)
gmapOne.plot(Latitude, Longitude, 'blue', edge_width=3.0)
gmapOne.draw("map.html")  # Name of the file that want to save
