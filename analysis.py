import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
    "PM2.5":[104.5,64.66,402.5,334.66,124],
    "PM10":[128.5,84,299.5,246.66,143],
    "SO2" :[25,12.66,21,32.66,25],
    "CO": [46,25.66,84.5,73.6,40],
}
    #creating dataframe
df = pd.DataFrame(data, index=["winter", "spring", "summer", "autumn","monsoon"])
#calculate correlation matrix
corr_matrix= df.corr()

#ploting
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
vmin=-1,
vmax=1,
linewidth=0.5,
)

plt.title("correlation matrix of air pollutants", fontsize=14, pad=15)
plt.tight_layout()
plt.show()
