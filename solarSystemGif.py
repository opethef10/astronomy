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
    plt.title(f'Solar system at {date:%Y/%m/%d %H:%M:%S} UTC', fontsize = 10)
    
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
        plt.polar(planet.hlon, radius, marker=marker, label=label)
        
    plt.legend(loc='upper center', bbox_to_anchor=(1.21, 0.8), fontsize="small")
    plt.gca().axes.get_yaxis().set_ticklabels([])
    
    buffer = BytesIO()
    plt.savefig(buffer)
    images.append(imageio.imrelabel(buffer.getvalue()))
    plt.close()

imageio.mimsave(f"solar{start:%Y%m%d_%H%M%S}.gif", images)
