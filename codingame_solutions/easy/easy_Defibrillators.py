__author__ = 'Amin'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def calc_distance(latitudeA, longitudeA, latitudeB, longitudeB):
    x = (longitudeB - longitudeA) * math.cos((latitudeA + latitudeB) / 2)
    y = latitudeB - latitudeA
    d = math.sqrt(x*x + y*y) * 6371
    return d

LON = raw_input()
LAT = raw_input()
N = int(raw_input())

defibrillators = []
for i in xrange(N):
    DEFIB = raw_input()
    defibrillators.append(DEFIB)

user_longitude = float(LON.replace(",", "."))
user_latitude = float(LAT.replace(",", "."))

min_distance = 999999
closest_defib_name = "xxx"

for defibrillator in defibrillators:
    defib_id, defib_name, defib_address, defib_phone, \
    defib_longitude, defib_latitude = defibrillator.split(";")

    current_distance = calc_distance(
        user_latitude,
        user_longitude,
        float(defib_latitude.replace(",", ".")),
        float(defib_longitude.replace(",", "."))
    )

    if(current_distance < min_distance):
        min_distance = current_distance
        closest_defib_name = defib_name

    print >> sys.stderr, defib_name

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print >> sys.stderr, user_longitude
print >> sys.stderr, user_latitude

print closest_defib_name