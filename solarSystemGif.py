from io import BytesIO
from datetime import datetime, timedelta

from ephem import *
import matplotlib.pyplot as plt
import imageio

gezegenler = Moon(), Mercury(), Venus(), Sun(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune()
başlangıç = datetime.utcnow()
tarihÜreteci = (başlangıç + timedelta(gün) for gün in range(0, 1000, 5))
resimler = []

for tarih in tarihÜreteci:
    plt.axes(projection='polar')
    plt.title(f'Solar system at {tarih:%Y/%m/%d %H:%M:%S} UTC', fontsize = 10)
    for yarıçap, gezegen in enumerate(gezegenler):
        gezegen.compute(tarih)
        simge='o'
        ad = gezegen.name
        if ad == "Moon":
            simge='*'
            ad = "Sun"
        elif ad == "Sun":
            simge='x'
            ad = "Earth"
        plt.polar(gezegen.hlon, yarıçap, marker = simge, label = ad)
    plt.legend(loc='upper center', bbox_to_anchor=(1.21, 0.8), fontsize="small")
    plt.gca().axes.get_yaxis().set_ticklabels([])
    
    buffer = BytesIO()
    plt.savefig(buffer)
    resimler.append(imageio.imread(buffer.getvalue()))
    plt.close()

imageio.mimsave(f"solar{başlangıç:%Y%m%d_%H%M%S}.gif", resimler)