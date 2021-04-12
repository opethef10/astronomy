#!python -i
from math import ceil

from ephem import *

TIME = now()

def derece(radyan,ondalık=2):
    sonuç=round(radyan * 180/pi,ondalık)
    return f"{sonuç}°"

def location(name):
    o = Observer()
    o.name = name
    o.lat, o.lon, o.elevation = CITIES[name]
    o.date=TIME
    o.compute_pressure()
    return o

CITIES = {
    'Didim': ('37:24', '27:15', 85),
    'Yenikent': ('40:01:00', '32:31:50', 850), 
    'Metu': ('39:54', '32:47', 700),
    "Elbląg": ('54:11','19:25',0),
    "Gdańsk": ('54:25','18:35',0),
    "Greenwich": ('51:30','0',0)
    }   

SYNODIC_MONTH = 29.530588867
LUNATION_BASE = Date("1923/1/17 02:40:50")
lunation = ceil((TIME - LUNATION_BASE) / SYNODIC_MONTH)
GSIDTIME=location("Greenwich").sidereal_time()

yerler = location("Yenikent"),
gökCisimleri = Sun(),Moon(),Venus(),Mars(),Jupiter(),Saturn()

print(f"Date&Time: {TIME} UTC")
print(f"Julian Date: {julian_date(TIME)}")
print(f"Lunation: {lunation}")
print(f"Islamic Lunation: {lunation+16085}")
print(f"Greenwich sidereal time: {GSIDTIME}")
print()

for şehir in yerler:
    sidTime=şehir.sidereal_time()
    print(f'{şehir.name.upper()} {"-"*6} {derece(şehir.lat)}' 
          f'{derece(şehir.lon)} {"-"*6} {hours((sidTime-GSIDTIME)%(2*pi))}')
    print(f"sidereal time: {sidTime}")
    
    for cisim in gökCisimleri:
        cisim.compute(şehir)
        print("name:", cisim.name)
        print("altitude:", derece(cisim.alt))
        print("azimuth:",derece(cisim.az))
        print("RA:",cisim.ra,"/",derece(cisim.ra))
        print("dec:",derece(cisim.dec))
        print("hour angle:",hours(sidTime-cisim.ra))
        print("elong:",derece(cisim.elong))
        print("parlaklık:",cisim.mag)
        print("size:",round(cisim.size,1),"arcseconds/",derece(2*cisim.radius,3))
        print("constellation:",constellation(cisim)[1])
        try:
            print("Sun distance:",round(cisim.sun_distance,2),"AU")
            print("Earth distance:",round(cisim.earth_distance,2),"AU")
            print("phase: %",round(cisim.phase,1),sep="")
            print("hlon:",derece(cisim.hlon))
            print("hlat:",derece(cisim.hlat))
        except:
            pass
        try:
            print("next rising:",şehir.next_rising(cisim),"UTC")
            print("next transit:",şehir.next_transit(cisim),"UTC")
            print("next setting:",şehir.next_setting(cisim),"UTC")
        except:
            print("next rising: N/A")
            print("next transit:",şehir.next_transit(cisim),"UTC")
            print("next setting: N/A")
        print()

print("Next Equinox:",next_equinox(TIME),"UTC")
print("Next Solstice:",next_solstice(TIME),"UTC")
print()
print("Previous New Moon:",previous_new_moon(TIME),"UTC")
print("Next New Moon:",next_new_moon(TIME),"UTC")
print("Next First Quarter:",next_first_quarter_moon(TIME),"UTC")
print("Next Full Moon:",next_full_moon(TIME),"UTC")
print("Next Last Quarter:",next_last_quarter_moon(TIME),"UTC")
print("Age of Moon:",round(TIME-previous_new_moon(TIME),2),"days")
print("separation of Moon and Sun:", derece(separation(Moon(TIME),Sun(TIME))))
