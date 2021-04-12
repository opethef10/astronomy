from ephem import *
import matplotlib.pyplot as plt

tarih = now() #Date("2013/5/26 17:00:00")
gezegenler = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()

plt.axes(projection='polar')
plt.title(f'Solar system at {tarih} UTC', fontsize=10)

for r, gezegen in enumerate(gezegenler):
    gezegen.compute(tarih)
    simge = 'o'
    ad = gezegen.name
    if ad == "Moon":
        simge = '*'
        ad = "Sun"
    elif ad == "Sun":
        simge = 'x'
        ad = "Earth"
    plt.polar(gezegen.hlon, r, marker = simge, label = ad)

plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
plt.gca().axes.get_yaxis().set_ticklabels([])
plt.show()