import requests
import emoji
url = 'https://api.github.com/users/'
user = str(input('Username: ')).strip()
response = requests.get(url + user)

github = {
    "login": response.json()["login"],
    "name": response.json()["name"],
    "followers": response.json()["followers"],
    "following": response.json()["following"],
    "bio": response.json()["bio"]

}

# Mostrar os repositórios 
def repos(user):
    repositorios = requests.get(url + user + '/repos').json()
    print('### REPOSITÓRIOS ###')
    for ReposName in repositorios:
        print()
        print(f'{ReposName["name"]}\t' + emoji.emojize(':star:'), f'{ReposName["stargazers_count"]}')

# Mostrando as Informações
print('#' * 30)
print(f'{github["name"]} | {github["login"]}')
print(f'followers: {github["followers"]} Following {github["following"]}')
print(f'Bio: {github["bio"]}')
repos(user) # Chamando a função 