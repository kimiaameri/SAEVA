#!/usr/bin/env python

################################################################
## For a given list of proteins single out only the interactions
## which have experimental evidences and print out their score
################################################################

import sys
import urllib3
import urllib3.exceptions

inputFile = sys.argv[1]
output = sys.argv[2]

string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "network"

f = open(inputFile)
my_genes = []
for line in f.readlines():
    line = line.strip()
    my_genes.append(line)   
    
f.close()

#my_genes = inputFile

species = "1280"
my_app  = "www.awesome_app.org"

## Construct the request

request_url = string_api_url + "/" + output_format + "/" + method + "?"
request_url += "identifiers=%s" % "%0d".join(my_genes)
request_url += "required_score=" + "0.15"
request_url += "&" + "species=" + species
request_url += "&" + "caller_identity=" + my_app


http = urllib3.PoolManager()
try:
    response = http.request('GET',request_url)
except urllib3.exceptions.NewConnectionError as err:
    error_message = err.read()
    print (error_message)
    sys.exit()
    
## Read and save the results
line = response.data
f = open(output,'wb')
f.write(line)
f.close()



