
import reverse_geocoder as rg # to find out the location from which IP recieved
import geocoder # to ip adress


my_ip = geocoder.ip('me') # get the ip address of my device
# print(f"Latitude: {ipadderess.lat}\nLogitude: {ipadderess.lng}"

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) # get the location
    
    # returns the name of the place...
    return result 


if __name__ == '__main__': 
      
    # Giving the cordinates
    coordinates =(my_ip.lat, my_ip.lng) 
    print(reverseGeocode(coordinates))
