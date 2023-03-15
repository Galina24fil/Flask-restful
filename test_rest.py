from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users/1').json())

print(get('http://localhost:5000/api/v2/users/15').json()) # несуществующий id

print(get('http://localhost:5000/api/v2/users/q').json()) # id не инт

print(get('http://localhost:5000/api/v2/users').json())
print(delete("http://localhost:5000/api/v2/users/25").json()) #удаление
print(post("http://localhost:5000/api/v2/users",
           json={"surname": "Фамилия", "name": "name",
            "age": 2, "position": "position", "speciality": "speciality",
            "address": "address", "email": "email25@email",
            "password": "Qazqwer25"}).json())

print(get('http://localhost:5000/api/v2/users').json()) # добавился

print(post("http://localhost:5000/api/v2/users",
           json={"surname": "Фамилия"}).json()) # недостаточно данных

print(post("http://localhost:5000/api/v2/users", # добавление уже существующего
           json={"id": 25, "surname": "Фамилия", "name": "name",
            "age": 2, "position": "position", "speciality": "speciality",
            "address": "address", "email": "email25@email",
            "password": "Qazqwer25"}).json())

print(delete('http://localhost:5000/api/v2/users/q').json()) # не int
print(delete('http://localhost:5000/api/v2/users/100').json()) #удаление не существующего
