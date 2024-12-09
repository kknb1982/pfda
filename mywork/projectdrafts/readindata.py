import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from datetime import datetime

#date = "Date"
#tavg = "Average air temperature in Celsius"
#tmin = "Minimum air temperature in Celsius"
#tmax = "Maximum air temperature in Celsius"

# Step 1: Load Data
url = "https://bulk.meteostat.net/v2/daily/0CNUO.csv.gz"
df = pd.read_csv(url, compression='gzip', usecols=[0,1,2,3], names =["date", "tavg", "tmin", "tmax"])
df.info()

# Step 2: Select First Four Columns
#df = df[0,1,2,3]

# Step 3: Handle Missing Values
df.dropna(inplace=True)

# Step 4: Add Cyclical Features for Date
df['date'] = pd.to_datetime(df['date'])
df['day_of_year'] = df['date'].dt.dayofyear
df['sin_day'] = np.sin(2 * np.pi * df['day_of_year'] / 365.0)
df['cos_day'] = np.cos(2 * np.pi * df['day_of_year'] / 365.0)

# Step 5: Prepare Data for Clustering
features = ['tavg', 'tmin', 'tmax', 'sin_day', 'cos_day']
X = StandardScaler().fit_transform(df[features])

# Step 6: Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Step 7: Visualize Clusters
plt.figure(figsize=(10, 6))
for cluster in range(kmeans.n_clusters):
    cluster_data = df[df['cluster'] == cluster]
    plt.scatter(cluster_data['day_of_year'], cluster_data['tavg'], label=f'Cluster {cluster}')
    
plt.title('KMeans Clustering of Weather Data')
plt.xlabel('Day of Year')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.show()


#parallel_plot(P[P['air_temp'] > 0.5])