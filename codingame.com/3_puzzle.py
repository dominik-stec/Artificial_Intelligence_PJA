import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())

defi_list = []
for i in range(n):
    defib = input()
    defi_item = defib.rsplit(';')
    defi_list.append(defi_item)

lon = lon.replace(',', '.')
lat = lat.replace(',', '.')
lon = float(lon)
lat = float(lat)    

lon_r = (lon*2*math.pi) / 360
lat_r = (lat*2*math.pi) / 360

distance_list = []
for data in defi_list:

    lon_b = data[-2]
    lat_b = data[-1]

    lon_b = lon_b.replace(',', '.')
    lat_b = lat_b.replace(',', '.')
    lon_b = float(lon_b)
    lat_b = float(lat_b) 

    lon_b_r = (lon_b*2*math.pi) / 360
    lat_b_r = (lat_b*2*math.pi) / 360
    x = (lon_b_r - lon_r) * math.cos((lat + lat_b_r) / 2)
    y = lat_b_r - lat_r
    distance = math.sqrt(math.pow(x,2) + math.pow(y,2)) * 6371
    distance_list.append(distance)

min = min(distance_list)
idx = distance_list.index(min)

desc = defi_list[idx][1]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(desc)
