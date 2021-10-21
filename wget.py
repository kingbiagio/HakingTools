#!/usr/bin/python3

import requests, sys

url = sys.argv[1]
print('Download Starting...')
 
r = requests.get(url, allow_redirects=True)
filename = url.split('/')[-1] # this will take only -1 splitted part of the url
 
with open(filename,'wb') as output_file:
    output_file.write(r.content)
 
print('Download Completed!!!')
