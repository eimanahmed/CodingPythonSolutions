import pandas as pd, folium, math
from folium.plugins import HeatMap

shootings_nyc = pd.read_csv("NYPD_Shooting_Incident_Data__Historic_.csv")
shootings_nyc.dropna()

m = folium.Map(location=[shootings_nyc['Latitude'].mean(), shootings_nyc['Longitude'].mean()], zoom_start=10.5)
heat_data = [[row['Latitude'], row['Longitude']] for index, row in shootings_nyc.iterrows() if math.isnan(row["Latitude"]) == False]
HeatMap(heat_data).add_to(m)

m.save("heatmap.html")
