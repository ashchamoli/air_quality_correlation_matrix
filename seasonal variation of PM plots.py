import pandas as pd
import matplotlib.pyplot as plt


data={
    "Season":["Summer", "Monsoon", "Autumn", "Winter", "Spring"],
    "PM2.5":[104.5,64.66,402.5,334.66,124],
    "PM10":[128.5,84,299.5,246.66,143],
}
#convert to dataframe
df= pd.DataFrame(data)
#plot settings
plt.figure(figsize=(8,8))
#plot both pollutants on same graph
plt.plot(df["Season"],df["PM2.5"], marker='o', linewidth=2, color='#d95f02', label=r'$\mathrm{PM}_{2.5}$')
plt.plot(df["Season"], df["PM10"], marker='s', linewidth=2, color='#7570b3', label=r'$\mathrm{PM}_{10}$')
plt.title("Seasonal variation of particulate matter concentrations",fontsize=14, pad=15, fontweight='bold')
plt.xlabel("Season",fontsize=12)
plt.ylabel("Concentration ($\mu$g/$m^3$)",fontsize=12)
plt.legend(fontsize=11, frameon=True)
plt.tight_layout()
plt.show()
