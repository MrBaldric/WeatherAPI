import urllib2
import xml.etree.ElementTree as et

url = "ftp://ftp.bom.gov.au/anon/gen/fwo/IDQ60920.xml"
response = urllib2.urlopen(url).read()
stationList = []
root = et.fromstring(response)

for a in root.iter("observations"):
    ct1 = 0
    while ct1 < len(a):
        ct1 += 1
z = 0
while z < (len(a)):
    location = (a[z].attrib)['description']
    if (location == 'Warwick'):
        print location
        print "Time of record : {}".format((a[z][0].attrib['time-local']))
        fields =  len(a[z][0][0])
        f = 0
        while f < fields:
            key = (a[z][0][0][f].attrib).keys()[0]#.keys gets keys from dict and puts in a list thus [0] is first postion in list
            if key == 'units':
                print (a[z][0][0][f].attrib['type']),(a[z][0][0][f].text),(a[z][0][0][f].attrib['units'])
            f += 1
        print "==============================================="
    if (location == 'Brisbane'):
        print location
        print "Time of record : {}".format((a[z][0].attrib['time-local']))
        fields =  len(a[z][0][0])
        f = 0
        while f < fields:
            key = (a[z][0][0][f].attrib).keys()[0]#.keys gets keys from dict and puts in a list thus [0] is first postion in list
            if key == 'units':
                print (a[z][0][0][f].attrib['type']),(a[z][0][0][f].text),(a[z][0][0][f].attrib['units'])
            f += 1
        print "==============================================="

    z += 1


