import mmh3
import requests
import codecs

favicon=input("Enter the URL with the Favicon Hash (Format - https://domain.com/favicon.ico)\n-->")
response = requests.get(favicon)
   
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)