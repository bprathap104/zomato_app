from Zomatopy.zomatopy import zomatopy
import ast
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="saranazure")
location = geolocator.geocode("S Block, Anna Nagar, Chennai")
# location = geolocator.geocode("DLF IT Park, Ramapuram")

config={
  "user_key":""
}

zomato = zomatopy.initialize_app(config)
out = zomato.get_nearby_restaurants(location.latitude, location.longitude)
for keys in out.keys():
  res=zomato.get_restaurant(keys)
  print(res.name)
  print(res.location)
  print(res.city)
  print(res.user_rating)
  print('----------')