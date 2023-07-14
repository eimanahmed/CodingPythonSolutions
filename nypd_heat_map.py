import pandas as pd, folium, math
from folium.plugins import HeatMap

shooting_data_nyc = pd.read_csv("NYPD_Shooting_Incident_Data__Historic_.csv")
shooting_data_nyc.dropna()

avg_lat = shooting_data_nyc["Latitude"].mean()
avg_lon = shooting_data_nyc["Longitude"].mean()

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=10.5)

heat_data = []
for index, row in shooting_data_nyc.iterrows():
    individual_data_location = []
    if math.isnan(row["Latitude"]) == False:
        individual_data_location.append(row["Latitude"])
        individual_data_location.append(row["Longitude"])
        heat_data.append(individual_data_location)

print(heat_data)

HeatMap(heat_data).add_to(map)

map.save("heatmap.html")
