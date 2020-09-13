# importing necessary libraries 
import reverse_geocoder as rg 
import geocoder

ipadderess = geocoder.ip('me') # get the ip address

#print(f"Latitude: {ipadderess.lat}\nLogitude: {ipadderess.lng}"

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) # get the location
    
    for i in result:
        print(i,end="\n")
  
# The codinates of the IP adress and where it pints to
coordinates =(ipadderess.lat, ipadderess.lng) 

reverseGeocode(coordinates)
