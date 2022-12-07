#! usr/bin/env python
from ephem import *
import matplotlib.pyplot as plt

date = now()
planets = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()

plt.axes(projection='polar')
plt.title(f'Geocentric view at {date} UTC', fontsize=10)

for radius, planet in enumerate(planets):
    planet.compute(date)
    marker = 'o'
    if planet.name=="Moon":
        marker = 'x'
        radius = 0.5
    elif planet.name=="Sun":
        marker = '*'
    plt.polar(planet.ra, radius, marker = marker, label = planet.name)

plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
plt.gca().axes.get_yaxis().set_ticklabels([])
plt.show()
