import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('vardata.csv')

# Numerical Comparisons
# Penalties Awarded
x = data['Season']
y = data['Penalties Awarded']
plt.bar(x,y, color='green')
plt.xlabel('Season')
plt.ylabel('Penalties')
plt.title('Penalties by Season')

plt.show()

#Red Cards
x = data['Season']
y = data['Red Cards']
plt.bar(x,y, color='red')
plt.xlabel('Season')
plt.ylabel('Red Cards')
plt.title('Red Cards Shown')

plt.show()

#Offsides Called
x = data['Season']
y = data['Offsides']
plt.bar(x,y, color='orange')
plt.xlabel('Season')
plt.ylabel('Offsides Called')
plt.title('Number of Offsides Given')

plt.show()
# Rate Comparisons (stat/game)
#Penalties
x = data['Season']
y = data['PPG']
plt.bar(x,y, color='green')
plt.xlabel('Season')
plt.ylabel('Penalties Per Game')
plt.title('Penalty Awarding Rate')

plt.show()

#Red Cards
x = data['Season']
y = data['RPG']
plt.bar(x,y, color='red')
plt.xlabel('Season')
plt.ylabel('Red Cards Per Game')
plt.title('Red Cards Awarded Per Game')

plt.show()

#Offsides
x = data['Season']
y = data['OPG']
plt.bar(x,y, color='orange')
plt.xlabel('Season')
plt.ylabel('Offsides Per Game')
plt.title('Offsides Given Per Game')

plt.show()
