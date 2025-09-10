#request is third party module in python that allows to send the request on web to get webs data
#through the HTTP
#Https works with four 
#get, post, put and update, delete

import requests

#1. Get --> get the data of website or kisi server sa data lena
url = 'https://jsonplaceholder.typicode.com/posts'
respone = requests.get(url)
print(respone.status_code)  #--> if it's 200 then response successfull if 404 response nahi aya
print(respone.json())

#2. Query Parameters (URL me data bhejna) we can filter specific Id data.
url1 = 'https://jsonplaceholder.typicode.com/posts'
params = {
    "userId" : 1,
    "id" : 7
}
#now url convert into the https://jsonplaceholder.typicode.com/posts?UserId=1&id=7
response = requests.get(url1, params=params)  
print(response.json())



#3. Post method means send the data to server using urls.
url2 = 'https://jsonplaceholder.typicode.com/posts'
data = {
    "userId" : 1,
    'id' : 11,
    "title" : "Usama's Post",
    "body" : "I am learning a Python Language requests module"
}
response = requests.post(url2, json=data)
print(response.status_code)
print(response.json())



#4. Put and Patch method --> for updating the data on server for specific id.
#--> put update the whole data body and patch update the selected field you want to update.

url3 = 'https://jsonplaceholder.typicode.com/posts/1'  
data = {
    'title' : 'Full Update Body',
    'body'  : 'Updated Content',
    'Id' : 1
}
#put() method --> update data fully
respone = requests.put(url3, json=data)
print(respone.status_code, 'Data Updated Fully for Id 1')
#patch() method --> update some fields
respone = requests.patch(url3, json={'title':'Partially Updated'})
print(respone.status_code, 'Data Updated Partially for Id 1')


#5. Delete data using delete() method for specific Id
url4 = 'https://jsonplaceholder.typicode.com/posts/1'  
response = requests.delete(url4)
print(response.status_code, "Data delete for Id 1")  #200 or 204 success code













