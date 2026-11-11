import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Seasonal names 
seasons = ['Summer', 'Monsoon', 'Autumn', 'Winter', 'Spring']

# PM2.5 data
pm25_rk_puram = [104.5, 64.66, 402.5, 334.66, 124]
pm25_karol_bagh = [88.5, 46.66, 362.5, 334, 148]
pm25_lawrence_road = [138, 66.33, 433, 351, 134.5]

# PM10 data
pm10_rk_puram = [128.5, 84, 299.5, 246.66, 143]
pm10_karol_bagh = [126.5, 106.33, 269, 263.33, 218.5]
pm10_lawrence_road = [201, 141, 425, 311.66, 169.5]

# Meteorological data (provided in the order: Summer, Monsoon, Autumn, Winter, Spring)
temp_c = [33.2, 29.8, 23.4, 14.8, 25.1]
humidity_percent = [41.5, 77.8, 55.3, 71.2, 43.4]
wind_speed_kmh = [8.3, 7.3, 5.8, 5.5, 6.4]

# Creating a DataFrame
data = {
    'Season': seasons * 3, # Repeat seasons for each location
    'Location': ['RK Puram'] * 5 + ['Karol Bagh'] * 5 + ['Lawrence Road'] * 5,
    'PM2.5': pm25_rk_puram + pm25_karol_bagh + pm25_lawrence_road,
    'PM10': pm10_rk_puram + pm10_karol_bagh + pm10_lawrence_road,
    'Temperature_C': temp_c * 3,
    'Humidity_percent': humidity_percent * 3,
    'WindSpeed_kmh': wind_speed_kmh * 3
}

df_seasonal = pd.DataFrame(data)
display(df_seasonal)
