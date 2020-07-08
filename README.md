# fastmapper
This is a command line utility for quickly mapping a set of addresses.

Begin by setting up a [Google Maps API
key](https://developers.google.com/places/web-service/get-api-key) and
saving the key as a text file in the working directory. Then add the
addresses of interest to a CSV file in the format as shown:

```
name,street,city,state,zip
Tmobile Park,1250 1st Ave S,Seattle,WA,98134
CenturyLink Field,800 Occidental Ave S, Seattle, WA,98134
Key Arena,305 Harrison St, Seattle, WA,98109
McCarthey Center,801 N Cincinnati St, Spokane, WA,99258
```

The main script geolocates all the addresses, writes them to a
[GeoJSON](https://geojson.org/) file which is then mapped to a [Leaflet map](https://leafletjs.com/) in
a new browser window.

![](https://i.imgur.com/XEe5dOY.png)
