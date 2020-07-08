import googlemaps
import csv
import sys
import argparse
import webbrowser
import SimpleHTTPServer
import BaseHTTPServer
import thread
import time
from geojson import Feature, FeatureCollection, Point

def start_server():
    httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 3600), SimpleHTTPServer.SimpleHTTPRequestHandler)
    httpd.serve_forever()

parser = argparse.ArgumentParser(description="""Command line utility to geolocate and map a text file of addresses""")
parser.add_argument('-i', help="Input file of complete mailing addesses")
parser.add_argument('-key', help="Text file with Google Maps API key", type=argparse.FileType("r"))

args = parser.parse_args()

outfile = "mapped_addresses.csv"

raw_key = args.key.read().rstrip("\n")
gmaps = googlemaps.Client(key= raw_key)

features = []
with open(args.i) as csvfile:
    csvfile.next()
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        base_address = row[1] + "," + row[2] + ", " + row[3] + ", " + row[4]
        print base_address
        try:
            gr = gmaps.geocode(base_address)
            latitude = gr[0]['geometry']['location']['lat']
            longitude = gr[0]['geometry']['location']['lng']
        except IndexError:
            latitude, longitude = '', ''
        features.append(
            Feature(
                geometry = Point((longitude,latitude)),
                properties = {
                    'name': row[0],
                    'address': row[1]
                    }
                )
        )

collection = FeatureCollection(features)
with open("map.geojson", "w") as f:
    f.write('%s' % collection)

thread.start_new_thread(start_server,())
url = 'http://127.0.0.1:3600'
webbrowser.open_new(url)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
