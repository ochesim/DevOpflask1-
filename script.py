# import urllib library 

from urllib.request import urlopen 

  
# import json 

import json 
# store the URL in url as  
# parameter for urlopen 

url = "http://127.0.0.1:5000/data"

  
# store the response of URL 

response = urlopen(url) 

  
# storing the JSON response  
# from url in data 

data_json = json.loads(response.read()) 

  
# print the json response 

print(data_json)
for data in data_json['samples']:
    with open('files/'+data['id']+'.txt', 'w') as a:
        a.write(data['name']+'\t ')
