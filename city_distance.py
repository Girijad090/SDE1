
from geopy.distance import  geodesic

city1 = ( 51.5074, 0.1278)
city2 = (48.8566, 2.3522)

distance = geodesic(city1, city2).kilometers

print("City 1: 51.5074 N, 0.1278 W")
print("City 2: 48.8566 N, 2.3522 E")
print("Output: City 1 and City 2 are {:.2f}".format(distance) +" km apart" )

