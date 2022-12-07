#! usr/bin/env python
from ephem import *
import matplotlib.pyplot as plt

date = now() #Date("2013/5/26 17:00:00")
planets = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()

plt.axes(projection='polar')
plt.title(f'Solar system at {date} UTC', fontsize=10)

for radius, planet in enumerate(planets):
    planet.compute(date)
    marker = 'o'
    label = planet.name
    if label == "Moon":
        marker = '*'
        label = "Sun"
    elif label == "Sun":
        marker = 'x'
        label = "Earth"
    plt.polar(planet.hlon, radius, marker = marker, label = label)

plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
plt.gca().axes.get_yaxis().set_ticklabels([])
plt.show()
