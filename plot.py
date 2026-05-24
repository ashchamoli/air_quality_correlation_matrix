import matplotlib.pyplot as plt

seasons =['Summer','Monsoon','Autumn','Winter','Spring',]
Rk_puram =[104.5,64.66,402.5,334.66,124]
karol_bagh=[88.5,46.66,362.5,334,148]
lawrence_road=[138,66.33,433,351,134.5]

plt.plot(seasons,Rk_puram, marker='o',label='Rk Puram')
plt.plot(seasons,karol_bagh,marker='o',label='Karol Bagh')
plt.plot(seasons,lawrence_road,marker='o',label='Lawrence Road')

plt.title('PM 2.5 variation', fontweight='bold', pad=35)
plt.ylim(0,450)
plt.grid(axis='y', linestyle=':', alpha=0.6)

plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.12),ncol=3, frameon=False)
plt.tight_layout()
plt.savefig('simplified_plot.png')
