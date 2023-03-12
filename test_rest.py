from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users/1').json())