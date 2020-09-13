import geocoder

ipadderess = geocoder.ip('me') # get the ip address

print(f"Latitude: {ipadderess.lat}\nLogitude: {ipadderess.lng}")
