#Importing modules
import os
import json
import requests
import base64
from dotenv import load_dotenv

#loading and defining the environment variable stored at .env
load_dotenv()
apiKey = os.getenv("GITHUB_APIKEY")

#Define headers:
headers = {"Authorization":f"token {apiKey}"}

#Making the request to the github api to get the root content
url = "https://api.github.com/repos/ironhack-datalabs/scavenger/contents/"
res = requests.get(url, headers = headers)
root = res.json()

#The content of each file is encoded in base64, this function decodes and re-encode the strings into ascii code
def decoding(s):  
    bytes = s.encode('ascii')
    s_base64 = base64.b64decode(bytes)
    string = s_base64.decode('ascii')
    return string

##Loop that navigates the root. If there is a dir, the loop goes into the directory, then check for the file names
# and if scavenger is in the name, then it request the file and extract the file name and the content (decoded and coded in ascii) in a tuple.
lst = []
for e in root:
    if e['type']=='dir':
        n_url = url + e['path']
        res = requests.get(n_url, headers = headers)
        fold = res.json()
        for file in fold:
            if 'scavengerhunt' in file['name']:
                n_url = url + file['path']
                res = requests.get(n_url, headers = headers)
                scab = res.json()
                lst.append((scab['name'],decoding(scab['content'])))

#Handling the resulting list:
lst.sort()
message = [e for i,e in lst]
print(' '.join(message[i]+message[i+1] for i in range(0,len(message),2)))

##Empecé haciéndolo también navegando el repositorio 'tree', pero el código era prácticamente igual, así que lo dejé.

##Para el bonus, he intentado añadir un fichero desde la terminal usando el siguiente comando, pero no hace nada, ni siquiera me lanza un error...:
# curl -u DavidCarricondo:$GITHUB_APIKEY -X PUT \
#       -d'{"message": "my commit message", \
#             "committer": { "name": "Jhon the revelator", "email": "arroba@github.com" },\
#                "content": "bXkgbmUgY29udGVudHM="}'\
#        http://api.github.com/repos/DavidCarricondo/test-ironhack/test.txt 
