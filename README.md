# fastmapper
This is a command line utility for quickly mapping a set of addresses.

Begin by setting up a [Google Maps API
key](https://developers.google.com/places/web-service/get-api-key) and
saving the key as a text file in the working directory. Then add the
addresses of interest to a CSV file in the format as shown:

```
name,street,city,state,zip
Tmobile Park,1250 1st Ave S,Seattle,WA,98134
Cheney Stadium,2502 South Tyler Street,Tacoma,WA,98405
Funko Field,3900 Broadway,Everett,WA,98201
Avista Stadium,602 N. Havana Street,Spokane,WA,99202
Paul Thomas Sr. Stadium,300 Fifth St.,Wenatchee,WA,98801

```

The main script geolocates all the addresses, writes them to a
[GeoJSON](https://geojson.org/) file which is then mapped to a [Leaflet map](https://leafletjs.com/) in
a new browser window.

![](https://i.imgur.com/0yZ5Bgo.png)
