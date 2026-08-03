import requests 

response =  requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(response.status_code)  # Printing the status code of the response

data = response.json()

print(data)








# status code = 200
# error = 404