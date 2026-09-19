import requests
from ..models import User

def get_users() -> list[User]:
  response = requests.get("https://randomuser.me/api/?page=3&results=20&seed=dfe")
  if response.status_code != 200:
    print(f'Error al obtener los usuarios: {response.status_code}')
    return []
  
  return response.json()['results']

def load_users():
  if User.objects.count():
    return f'Ya existen {User.objects.count()} usuarios'
  
  users = get_users()
  for user in users:
    User.objects.create(
      first_name=user['name']['first'],
      last_name=user['name']['last'],
      title=user['name'][ 'last'],
      gender=user['gender'],
      email=user['email'],
      phone=user['phone'],
      location=user['location']['city'],
      image=user['picture']['large'],
    )

  return f'Se cargaron {User.objects.count()} usuarios'

