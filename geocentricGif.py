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
    plt.title(f'Geocentric view at {tarih:%Y/%m/%d %H:%M:%S} UTC',fontsize=10)

    for r, gezegen in enumerate(gezegenler):
        gezegen.compute(tarih)
        mark='o'
        if gezegen.name=="Moon":
            mark='x'
            r=0.5
        elif gezegen.name=="Sun":
            mark='*'
        plt.polar(gezegen.ra,r,mark,label = gezegen.name)
    plt.legend(loc='upper center',bbox_to_anchor=(1.21, 0.8),fontsize="small")
    plt.gca().axes.get_yaxis().set_ticklabels([])
    
    buffer = BytesIO()
    plt.savefig(buffer)
    resimler.append(imageio.imread(buffer.getvalue()))
    plt.close()

imageio.mimsave(f"geo{başlangıç:%Y%m%d_%H%M%S}.gif", resimler)