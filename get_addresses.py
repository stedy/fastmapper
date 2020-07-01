import googlemaps
import csv
import os
import argparse

parser = argparse.ArgumentParser(description="""Command line utility to geolocate and map a text file of addresses""")
parser.add_argument('-i', help="Input file of complete mailing addesses")
parser.add_argument('-key', help="Text file with OMDb API key", type=argparse.FileType("r"))

args = parser.parse_args()

outfile = "mapped_addresses.csv"

raw_key = args.key.read().rstrip("\n")
gmaps = googlemaps.Client(key= raw_key)

csvre = csv.reader(open(args.i, "rb"))

t = (csvre,)
csvre.next()

with open(outfile, 'wb') as csvfile:
    for t in csvre:
        base_address = t[1] + ", " + t[2] + ", " + t[3] + ", " + t[4]
        try:
            gr = gmaps.geocode(base_address)
            lat = gr[0]['geometry']['location']['lat']
            lon = gr[0]['geometry']['location']['lng']
        except IndexError:
            lat, lon = '', ''
        csvfile.write(t[0] + ', ' + base_address + ', ' + str(lat) + ', ' +  str(lon) + "\n")
