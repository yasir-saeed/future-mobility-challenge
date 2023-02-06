import folium
import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv("obd-ii_data.csv")

# Create a map centered on the mean latitude and longitude of the data
mean_lat = df["Latitude (deg)"].mean()
mean_lon = df["Longitude (deg)"].mean()
map = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

# Plot each lat-lon pair as a point on the map
for lat, lon in zip(df["Latitude (deg)"], df["Longitude (deg)"]):
    folium.CircleMarker(location=[lat, lon], radius=5).add_to(map)

# Show the map
map.save("map.html")