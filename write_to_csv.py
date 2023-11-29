import csv

# Latitude and Longitude data
latitude = [6.9171, 6.9271, 6.9291, 6.9371]
longitude = [79.8622, 79.8602, 79.8652, 79.8672]

# Combine latitude and longitude into a list of tuples
data = list(zip(latitude, longitude))

# Specify the CSV file path
csv_file_path = 'coordinates.csv'

# Write data to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header
    csv_writer.writerow(['Latitude', 'Longitude'])

    # Write the data
    csv_writer.writerows(data)

print(f'Data has been written to {csv_file_path}')
