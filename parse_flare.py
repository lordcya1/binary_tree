import urllib
#import re
import json


json_data=open("/Users/Matrix001/Desktop/JS/binary_tree/flare.json").read()

data = json.loads(json_data)


#print data['name']
print "--------------------------------------------------------------------"
print data['children'][0]


#///////ddd
#this is the change2