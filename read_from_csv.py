import csv

# Specify the CSV file path
csv_file_path = 'coordinates.csv'

# Lists to store latitude and longitude data
latitude = []
longitude = []

# Read data from CSV file
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Read the header
    header = next(csv_reader)

    # Read data row by row
    for row in csv_reader:
        # Assuming the first column is latitude and the second column is longitude
        lat, lon = map(float, row)
        latitude.append(lat)
        longitude.append(lon)

# Print the read data
print('Latitude:', latitude)
print('Longitude:', longitude)
