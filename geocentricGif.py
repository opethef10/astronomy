#! usr/bin/env python
from datetime import datetime, timedelta
from io import BytesIO

from ephem import *
import imageio
import matplotlib.pyplot as plt

planets = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()
start = datetime.utcnow()
dateGenerator = (start + timedelta(day) for day in range(0, 1000, 5))
images = []

for date in dateGenerator:
    plt.axes(projection='polar')
    plt.title(f'Geocentric view at {tarih:%Y/%m/%d %H:%M:%S} UTC',fontsize=10)

    for radius, planet in enumerate(planets):
        planet.compute(date)
        marker = 'o'
        if planet.name=="Moon":
            marker = 'x'
            radius = 0.5
        elif planet.name=="Sun":
            mark = '*'
        plt.polar(planet.ra, radius, marker=marker, label=planet.name)
    
    plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
    plt.gca().axes.get_yaxis().set_ticklabels([])
    
    buffer = BytesIO()
    plt.savefig(buffer)
    images.append(imageio.imread(buffer.getvalue()))
    plt.close()

imageio.mimsave(f"geo{start:%Y%m%d_%H%M%S}.gif", images)
