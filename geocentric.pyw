from ephem import *
import matplotlib.pyplot as plt

tarih = now() #Date("2013/5/26 17:00:00")
gezegenler = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()

plt.axes(projection='polar')
plt.title(f'Geocentric view at {tarih} UTC', fontsize=10)

for r, gezegen in enumerate(gezegenler):
    gezegen.compute(tarih)
    simge = 'o'
    if gezegen.name=="Moon":
        simge = 'x'
        r = 0.5
    elif gezegen.name=="Sun":
        simge = '*'
    plt.polar(gezegen.ra, r, marker = simge, label = gezegen.name)

plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
plt.gca().axes.get_yaxis().set_ticklabels([])
plt.show()