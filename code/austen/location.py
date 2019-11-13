import geopy
import pandas 
from geopy.geocoders import Nominatim

#key = API_KEYAIzaSyAp1NuI0yxZGV5PwhGNo9Mx5UKIVH_gvf4
def main():
    file = pandas.read_csv("climbing.csv", index_col= None, header=0, sep=",")
    # print(type(file))
    print(file)
    def latitude(x):
        return x.latitude

    def longitude(x):
        return x.longitude
    
    def geocoder(place):
        #print(place)
        return place
    
    geolocator = Nominatim(user_agent="my-application", timeout = 10)

    geolocate_column = file['Places'].apply(geolocator.geocode)
    file['latitude'] = geolocate_column.apply(latitude)
    file['longitude'] = geolocate_column.apply(longitude)
    file.to_csv("climbing2.csv")

main()

